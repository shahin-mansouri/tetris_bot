from django.shortcuts import redirect, HttpResponse
from google_auth_oauthlib.flow import Flow
import requests
import os
import json
from django.contrib.auth.decorators import login_required
from .models import Youtube
from home.models import Coin
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google.auth.exceptions import RefreshError
from datetime import datetime, timedelta
import logging
from django.contrib import messages

# تنظیمات
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'  # غیرفعال کردن بررسی HTTPS (فقط برای محیط توسعه)
CLIENT_SECRET_FILE = 'client_secret_494543870180-tslhthqke6fl70rrnll6cc124n0061jl.apps.googleusercontent.com.json'
REDIRECT_URI = 'http://127.0.0.1:8000/youtube-auth/callback/'
CHANNEL_ID = "UCvwZz0LSe3CRMdOgh-Jil4g"

# استخراج CLIENT_ID و CLIENT_SECRET از فایل client_secret.json
with open(CLIENT_SECRET_FILE) as f:
    client_secrets = json.load(f)
    CLIENT_ID = client_secrets['web']['client_id']
    CLIENT_SECRET = client_secrets['web']['client_secret']

# لاگ‌گیری
logger = logging.getLogger(__name__)

def login_with_google(request):
    """هدایت کاربر به صفحه احراز هویت Google."""
    flow = Flow.from_client_secrets_file(
        CLIENT_SECRET_FILE,
        scopes=['https://www.googleapis.com/auth/youtube.readonly'],
        redirect_uri=REDIRECT_URI
    )
    authorization_url, state = flow.authorization_url()
    request.session['state'] = state
    return redirect(authorization_url)

def check_subscription(access_token):
    """بررسی سابسکرایب کاربر به کانال YouTube."""
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(
        'https://www.googleapis.com/youtube/v3/subscriptions?part=snippet&mine=true',
        headers=headers
    )
    response.raise_for_status()
    data = response.json()

    # بررسی سابسکرایب
    return any(
        item['snippet']['resourceId']['channelId'] == CHANNEL_ID
        for item in data.get('items', [])
    )

def refresh_access_token(youtube_subscription):
    """رفرش توکن دسترسی با استفاده از توکن رفرش."""
    try:
        credentials = Credentials(
            token=youtube_subscription.access_token,
            refresh_token=youtube_subscription.refresh_token,
            token_uri='https://oauth2.googleapis.com/token',
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET
        )

        if credentials.expired:
            credentials.refresh(Request())

            # ذخیره توکن جدید در دیتابیس
            youtube_subscription.access_token = credentials.token
            if hasattr(credentials, 'token_expiry'):
                youtube_subscription.token_expiry = credentials.token_expiry
            else:
                # اگر token_expiry وجود نداشت، یک زمان پیش‌فرض تنظیم کنید
                youtube_subscription.token_expiry = datetime.now() + timedelta(hours=1)
            youtube_subscription.save()

        return credentials.token
    except RefreshError as e:
        logger.error(f"Failed to refresh access token: {str(e)}")
        return None

@login_required
def check_subscription_status(request):
    """بررسی وضعیت سابسکرایب کاربر و به‌روزرسانی آن."""
    user = request.user
    youtube_subscription = Youtube.objects.filter(user=user).first()

    if youtube_subscription:
        # بررسی سابسکرایب با استفاده از توکن دسترسی
        access_token = refresh_access_token(youtube_subscription)
        if access_token:
            is_subscribed = check_subscription(access_token)

            # به‌روزرسانی وضعیت سابسکرایب در دیتابیس
            youtube_subscription.is_sub = is_subscribed
            youtube_subscription.save()

            if is_subscribed:
                messages.success(request, "You have successfully subscribed to our channel!")
                user_coin, create = Coin.objects.get_or_create(user=request.user)
                user_coin.coin_amount += 10000
                user_coin.save()
                return redirect('home')  # بازگشت به صفحه اصلی
            else:
                messages.warning(request, "You have not subscribed to our channel yet.")
                return redirect('https://www.youtube.com/channel/UCvwZz0LSe3CRMdOgh-Jil4g')  # هدایت به چنل YouTube
        else:
            messages.error(request, "Failed to refresh access token. Please try again.")
            return redirect('home')
    else:
        messages.error(request, "You are not logged in with Google.")
        return redirect('home')

@login_required
def callback(request):
    """Callback برای دریافت توکن‌ها و بررسی سابسکرایب."""
    try:
        state = request.session.get('state')
        if not state:
            logger.error("State not found in session.")
            return HttpResponse("State not found in session. Please try again.", status=400)

        flow = Flow.from_client_secrets_file(
            CLIENT_SECRET_FILE,
            scopes=['https://www.googleapis.com/auth/youtube.readonly'],
            state=state,
            redirect_uri=REDIRECT_URI
        )
        flow.fetch_token(authorization_response=request.get_full_path())
        credentials = flow.credentials

        logger.info("Tokens fetched successfully.")

        # ذخیره توکن‌ها در دیتابیس
        youtube_subscription, created = Youtube.objects.get_or_create(user=request.user)
        youtube_subscription.access_token = credentials.token
        youtube_subscription.refresh_token = credentials.refresh_token

        # استفاده از token_expiry به جای expires_in
        if hasattr(credentials, 'token_expiry'):
            youtube_subscription.token_expiry = credentials.token_expiry
        elif hasattr(credentials, 'expires_in'):
            youtube_subscription.token_expiry = datetime.now() + timedelta(seconds=credentials.expires_in)
        else:
            # اگر هیچ‌کدام وجود نداشت، یک زمان پیش‌فرض تنظیم کنید
            youtube_subscription.token_expiry = datetime.now() + timedelta(hours=1)

        youtube_subscription.save()

        # بررسی سابسکرایب
        is_subscribed = check_subscription(credentials.token)

        # به‌روزرسانی وضعیت سابسکرایب
        youtube_subscription.is_sub = is_subscribed
        youtube_subscription.channel_url = f'https://www.youtube.com/channel/{CHANNEL_ID}' if is_subscribed else None
        youtube_subscription.save()

        if is_subscribed:
            if created:
                user_coin, create = Coin.objects.get_or_create(user=request.user)
                user_coin.coin_amount += 10000
                user_coin.save()
                return HttpResponse(
                    "You have followed the YouTube channel. You have been awarded 10,000 points. <a href='/home'>Home</a>"
                )
            return HttpResponse(
                "You have already followed the YouTube channel. <a href='/home'>Home</a>"
            )
        else:
            return HttpResponse(
                f"Please subscribe to the channel first. <a href='https://www.youtube.com/channel/{CHANNEL_ID}'>Channel</a>"
            )

    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        return HttpResponse(f"An error occurred: {str(e)}", status=500)