from django.urls import path
from .views import VerifyTokenView, Wellcome, verify_user

urlpatterns = [
    path('', VerifyTokenView.as_view(), name='verify-token'),
    path('wellcome', Wellcome.as_view(), name='wellcome'),
    path('verify-user', verify_user, name='verify_user'),
]

