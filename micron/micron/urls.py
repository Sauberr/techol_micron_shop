from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    # Products App
    path('', include('products.urls', namespace='products')),
    # User App
    path('user_account/', include('user_account.urls', namespace='user_account')),
    # Cart App
    path('cart/', include('cart.urls', namespace='cart')),
    # Orders App
    path('orders/', include('orders.urls', namespace='orders')),
    # Captcha App
    path('captcha/', include('captcha.urls')),
    # Social account
    path('social-auth/',
         include('social_django.urls', namespace='social')),
    # Password reset
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='user_account/password/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='user_account/password/password_reset_complete.html'),
         name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns.append(path('__debug__/', include('debug_toolbar.urls')))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
