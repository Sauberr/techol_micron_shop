from django.urls import path

from products.views import list_category, product_detail, products, add_to_favorite, delete_from_favorites, favorite_products, add_review, delete_review, update_review
app_name = 'products'

urlpatterns = [
    # Main page
    path('', products, name='products'),
    # Detail product page
    path('product-detail/<slug:product_slug>/', product_detail, name='product_detail'),
    # Individual category
    path('category/<slug:category_slug>/', list_category, name='list_category'),
    # Add to favorite
    path('add-to-favorites/<int:product_id>/', add_to_favorite, name='add_to_favorites'),
    # Favorite products
    path('favorite-products/', favorite_products, name='favorite_products'),
    # Delete from favorite
    path('delete-from-favorites/<int:product_id>/', delete_from_favorites, name='delete_from_favorites'),
    # Add reviews
    path('add-review/<int:product_id>/', add_review, name='add_review'),
    path('delete-review/<int:review_id>/', delete_review, name='delete_review'),
    path('update-review/<int:review_id>/', update_review, name='update_review'),
]
