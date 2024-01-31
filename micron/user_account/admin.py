from django.contrib import admin

from user_account.models import EmailVerification, User, Contact


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username",)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')


@admin.register(EmailVerification)
class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = ("user", "code", "expiration")
    fields = ("user", "code", "expiration", "created")
    readonly_fields = ("created",)
