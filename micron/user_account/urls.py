from django.contrib.auth.decorators import login_required
from django.urls import path
from user_account.views import UserLoginView, UserRegistrationView, ResetPasswordView, ChangePasswordView
from django.contrib.auth import views as auth_views

app_name = 'user_account'

urlpatterns = [
    # Login page
    path('login/', UserLoginView.as_view(), name='login'),
    # Logout page
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # Registration page
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    # Password reset page
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    # Password change page
    path('password-change/', login_required(ChangePasswordView.as_view()), name='password_change'),
]