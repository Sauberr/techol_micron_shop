from django import forms
from django.utils.translation import gettext_lazy as _


class CouponApplyForm(forms.Form):
    code = forms.CharField(
        label=_("Coupon"),
        widget=forms.TextInput(
            attrs={
                "class": "form-control py-2 w-25 ml-auto",
                "placeholder": "Enter coupon code",
            }
        ),
    )
