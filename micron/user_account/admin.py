from django.contrib import admin
from django.utils.html import format_html
from user_account.models import Contact, EmailVerification, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html(
            '<img src="{}" width="40" style="border-radius: 50px;" />'.format(
                object.image.url
            )
        )

    thumbnail.short_description = "Photo"
    list_display = ("username", "thumbnail")
    list_display_links = ("username", "thumbnail")


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "message")


@admin.register(EmailVerification)
class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = ("user", "code", "expiration")
    fields = ("user", "code", "expiration", "created")
    readonly_fields = ("created",)
