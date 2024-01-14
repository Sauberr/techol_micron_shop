
from django.db.models import Avg
from django.shortcuts import get_object_or_404, render, redirect

from cart.forms import CartAddProductForm
from products.models import Category, Product, Review
from .forms import ReviewForm
from django.contrib import messages

from .utils import paginateprodcuts, searchproducts
from .recommender import Recommender
import logging


logger = logging.getLogger('main')


def products(request):
    logger.info('products')
    products, search_query = searchproducts(request)
    custom_range, products = paginateprodcuts(request, products, 3)
    context = {
        'title': 'Products',
        'products': products,
        'search_query': search_query,
        'custom_range': custom_range,
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug, available=True)
    cart_product_form = CartAddProductForm()
    r = Recommender()
    recommended_products = r.suggest_products_for([product], 4)
    reviews = Review.objects.filter(product=product)
    if reviews:
        average_stars = reviews.aggregate(Avg('stars'))['stars__avg']
    else:
        average_stars = None
    context = {
        'product': product,
        'title': 'Product detail page',
        'cart_product_form': cart_product_form,
        'recommended_products': recommended_products,
        'reviews': reviews,
        'average_stars': average_stars,
    }
    return render(request, 'products/single_product.html', context)


def categories(request):
    all_categories = Category.objects.all()
    return {'all_categories': all_categories}


def list_category(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    context = {'products': products, 'category': category}
    return render(request, 'products/list_category.html', context)


def add_to_favorite(request, product_id):
    if request.user.is_authenticated:
        try:
            product = Product.objects.get(pk=product_id)
            request.user.favorite_products.add(product)
        except Product.DoesNotExist:
            pass
        return redirect('products:products')


def favorite_products(request):
    if request.user.is_authenticated:
        favorite_products = request.user.favorite_products.all()
        context = {'favorite_products': favorite_products, 'title': 'Favorite products'}
        return render(request, 'products/favorite_products.html', context)
    else:
        return redirect('user_account:login')


def delete_from_favorites(request, product_id):
    if request.user.is_authenticated:
        try:
            product = Product.objects.get(pk=product_id)
            request.user.favorite_products.remove(product)
        except Product.DoesNotExist:
            pass
        return redirect('products:favorite_products')


def add_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    existing_review = Review.objects.filter(user=request.user, product=product).first()
    if existing_review:
        messages.error(request, 'You have already reviewed this product')
        return redirect('products:product_detail', product_slug=product.slug)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.product = product
            review.save()
            return redirect('products:product_detail', product_slug=product.slug)
    else:
        form = ReviewForm()
    return render(request, 'products/add_reviews.html', {'form': form, 'product': product})


def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)

    if request.user != review.user:
        messages.error(request, 'You do not have permission to delete this review')
        return redirect('products:product_detail', product_slug=review.product.slug)

    review.delete()
    messages.success(request, 'Review deleted successfully')
    return redirect('products:product_detail', product_slug=review.product.slug)


def update_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)

    if request.user != review.user:
        messages.error(request, 'You do not have permission to update this review')
        return redirect('products:product_detail', product_slug=review.product.slug)

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Review updated successfully')
            return redirect('products:product_detail', product_slug=review.product.slug)
    else:
        form = ReviewForm(instance=review)

    return render(request, 'products/update_review.html', {'form': form, 'product': review.product})