from django.urls import path, include
from cart.views import cart_summary, cart_add, cart_remove, cart_clear

app_name = 'cart'

urlpatterns = [
    path('', cart_summary, name='cart_summary'),
    path('add/<int:product_id>/', cart_add, name='cart_add'),
    path('remove/<int:product_id>/', cart_remove, name='cart_remove'),
    path('clear/', cart_clear, name='cart_clear')
]