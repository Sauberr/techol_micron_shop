from django.shortcuts import render, get_object_or_404
from products.models import Product, Category
from cart.forms import CartAddProductForm
from .utils import searchproducts, paginateprodcuts


def products(request):
    products, search_query = searchproducts(request)
    custom_range, products = paginateprodcuts(request, products, 3)
    context = {
         'title': 'Products', 'products': products, 'search_query': search_query, 'custom_range': custom_range
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_slug):
    cart_product_form = CartAddProductForm()
    context = {
        'product': get_object_or_404(Product, slug=product_slug, available=True), 'title': 'Product detail page',
        'cart_product_form': cart_product_form
    }
    return render(request, 'products/single_product.html', context)


def categories(request):
    all_categories = Category.objects.all()
    return {'all_categories': all_categories}


def list_category(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    context = {
        'products': products, 'category': category
    }
    return render(request, 'products/list_category.html', context)
