from decimal import Decimal
from django.conf import settings
from products.models import Product


class Cart:

    def __init__(self, request):
        """Create a cart"""
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            """Save empty cart in session"""
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        """ Loop through the shopping
         cart items and
         get products from the database.
         """
        product_ids = self.cart.keys()
        # get product objects and add them to cart
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """Count all goods in cart"""
        return sum(item['quantity'] for item in self.cart.values())

    def add(self, product, quantity, override_quantity=False):
        """Add goods in cart or update it quantity"""
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        # Mark that session like 'updated'
        # that ensure its preservation
        self.session.modified = True

    def remove(self, product):
        """Remove goods from cart"""
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity']
                   for item in self.cart.values())

    def clear(self):
        # Remove all from session
        del self.session[settings.CART_SESSION_ID]
        self.save()