from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

import json

from customer.models import Customer
from product.models import Product


class OrderTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.customer = Customer.objects.create(user=self.user, phone='1234567890')

        self.product1 = Product.objects.create(name='Product1', price=100, stock=10)
        self.product2 = Product.objects.create(name='Product2', price=150, stock=5)

    def test_create_order(self):
        order_data = {
            'items': [
                {'product': self.product1.id, 'quantity': 2},
                {'product': self.product2.id, 'quantity': 1},
            ]
        }

        response = self.client.post('/api/orders/', data=json.dumps(order_data), content_type='application/json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['total_price'], "350.00")

        # Verify that the stock has decreased
        self.product1.refresh_from_db()
        self.product2.refresh_from_db()

        self.assertEqual(self.product1.stock, 8)
        self.assertEqual(self.product2.stock, 4)
