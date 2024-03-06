from django.urls import path

from rest_framework_simplejwt.views import  TokenRefreshView
from account.views import AccountActivateView, AccountCreateView, LogOutView, LoginView, ResetPasswordView, VerifyPasswordEmailView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path("signup/", AccountCreateView.as_view(), name="sign_up"),
    path("activate/<str:token>", AccountActivateView.as_view(), name="acivate-account"),
    path("verify-email/", VerifyPasswordEmailView.as_view(), name="verify-email"),
    path("reset-password/<str:token>", ResetPasswordView.as_view(), name="reset-password"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]