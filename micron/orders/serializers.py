from rest_framework import serializers
from orders.models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
        class Meta:
            model = OrderItem
            fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = '__all__'

    def get_items(self, obj):
        items = obj.items.all()
        serializer = OrderItemSerializer(items, many=True)
        return serializer.data