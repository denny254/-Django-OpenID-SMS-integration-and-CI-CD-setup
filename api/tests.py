
from django.test import TestCase
from rest_framework.test import APIClient
from .models import Customer, Order

class APITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.customer = Customer.objects.create(name="John Doe", code="JD001")

    def test_create_customer(self):
        response = self.client.post('/api/customers/', {'name': 'Jane Doe', 'code': 'JD002'})
        self.assertEqual(response.status_code, 201)

    def test_create_order(self):
        response = self.client.post('/api/orders/', {
            'item': 'Item 1',
            'amount': 100.50,
            'customer': self.customer.id
        })
        self.assertEqual(response.status_code, 201)

