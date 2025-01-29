from django.urls import path
from .views import VerifyTokenView, Wellcome

urlpatterns = [
    path('', VerifyTokenView.as_view(), name='verify-token'),
    path('wellcome', Wellcome.as_view(), name='wellcome'),
]

