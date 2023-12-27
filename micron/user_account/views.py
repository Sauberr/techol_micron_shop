from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from user_account.forms import UserLoginForm, UserRegistrationForm, PasswordChangingForm
from user_account.models import User
from django.views.generic import CreateView
from common.views import TitleMixin


class UserLoginView(TitleMixin, SuccessMessageMixin, LoginView):
    model = User
    template_name = 'user_account/login.html'
    form_class = UserLoginForm
    success_message = "You were successfully logged in"
    title = 'Login'

    def form_valid(self, form):
        remember_me = form.cleaned_data['remember_me']
        if not remember_me:
            self.request.session.set_expiry(0)
            self.request.session.modified = True
        return super(UserLoginView, self).form_valid(form)


class UserRegistrationView(TitleMixin, SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'user_account/registration/registration.html'
    success_url = reverse_lazy('user_account:login')
    success_message = "Your account was successfully created"
    title = 'Registration'


class ResetPasswordView(TitleMixin, SuccessMessageMixin, PasswordResetView):
    template_name = 'user_account/password/password_reset.html'
    email_template_name = 'user_account/password/password_reset_email.txt'
    subject_template_name = 'user_account/password/password_reset_subject.html'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('user_account:login')
    title = 'Reset Password'


class ChangePasswordView(TitleMixin, SuccessMessageMixin, PasswordChangeView):
    template_name = 'user_account/password/password_change.html'
    form_class = PasswordChangingForm
    success_message = "Your password was successfully changed"
    success_url = reverse_lazy('user_account:login')
    title = 'Change Password'



