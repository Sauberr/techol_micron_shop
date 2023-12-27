from .models import Product
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def searchproducts(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET['search_query']

    products = Product.objects.distinct().filter(
        Q(name__icontains=search_query)
        )
    return products, search_query


def paginateprodcuts(request, products, results):
    page = request.GET.get('page')
    paginator = Paginator(products, results)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        products = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        products = paginator.page(page)
    leftindex = (int(page) - 4)
    if leftindex < 1:
        leftindex = 1
    rightindex = (int(page) + 5)
    if rightindex > paginator.num_pages:
        rightindex = paginator.num_pages + 1
    custom_range = range(leftindex, rightindex)
    return custom_range, products