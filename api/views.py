from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer
import africastalking

# Initialize Africa's Talking SMS
africastalking.initialize(username='sandbox', api_key='YOUR_API_KEY')
sms = africastalking.SMS

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        order = response.data
        customer = Customer.objects.get(id=order['customer'])
        self.send_sms_alert(customer.code, f"Order placed for {order['item']}")
        return response

    def send_sms_alert(self, phone_number, message):
        response = sms.send(message, [phone_number])
        return response

