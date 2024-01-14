from rest_framework.viewsets import ModelViewSet
from products.models import Category, Product
from products.serializers import CategorySerializer, ProductSerializer
from orders.serializers import OrderSerializer
from orders.models import Order
from .permissions import IsAdminOrReadOnly
from rest_framework.permissions import IsAuthenticated


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly, IsAuthenticated)


class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly, IsAuthenticated)


class OrderModelViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAdminOrReadOnly, IsAuthenticated)



