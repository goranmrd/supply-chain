from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from rest_framework.response import Response

from .models import Order, OrderItem
from .serializers import OrderCreateSerializer, OrderSerializer
from customer.models import Customer
from product.models import Product


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderCreateSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Order.objects.none()  # Return an empty queryset during schema generation

        if self.request.user.is_authenticated:
            return Order.objects.filter(customer__user=self.request.user)
        else:
            raise PermissionDenied("You must be authenticated to access this resource")

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return OrderSerializer
        return OrderCreateSerializer

    def create(self, request, *args, **kwargs):
        with transaction.atomic():
            customer = Customer.objects.get(user=self.request.user)
            data = request.data
            items = data.pop('items', None)

            if not items:
                return Response({
                    'error': 'At least one item must be provided'
                }, status=status.HTTP_400_BAD_REQUEST)


            order = Order.objects.create(customer=customer, total_price=0)

            total_price = 0

            # Iterate through the items to create OrderItem instances
            for item in items:
                product = Product.objects.get(id=item['product'])
                if product.stock < item['quantity']:
                    return Response({
                        'error': 'Insufficient stock for product {}'.format(product.name)
                    }, status=status.HTTP_400_BAD_REQUEST)

                product.stock -= item['quantity']
                product.save()

                order_item = OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=item['quantity'],
                    price=product.price
                )

                total_price += order_item.price * order_item.quantity

            # Set the total price before final save
            order.total_price = total_price
            order.save()

            return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)
