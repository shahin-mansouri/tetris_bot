from django.urls import path
from .views import VerifyTokenView, Wellcome, verify_user
from .views import waiting_to_login

urlpatterns = [
    path('', VerifyTokenView.as_view(), name='verify-token'),
    path('wellcome', waiting_to_login, name='wellcome'),
    path('wellcome2', Wellcome.as_view(), name='wellcome2'),
    path('verify-user', verify_user, name='verify_user'),
]

