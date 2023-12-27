from django.urls import path, include
from products.views import products, product_detail, list_category

app_name = 'products'

urlpatterns = [
    # Main page
    path('', products, name='products'),
    # Detail product page
    path('product-detail/<slug:product_slug>/', product_detail, name='product_detail'),
    # Individual category
    path('category/<slug:category_slug>/', list_category, name='list_category'),
]