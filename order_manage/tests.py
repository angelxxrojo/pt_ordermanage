from django.test import TestCase
from .models import Inventory, Order

class OrderTestCase(TestCase):
    def setUp(self):
        self.item = Inventory.objects.create(item="Laptop", quantity=10)

    def test_create_order(self):
        response = self.client.post('/api/create-order/', {
            'item_id': self.item.id,
            'quantity': 5,
            'customer': 'John Doe'
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Order.objects.count(), 1)

    def test_not_enough_inventory(self):
        response = self.client.post('/api/create-order/', {
            'item_id': self.item.id,
            'quantity': 15,
            'customer': 'Jane Doe'
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json().get('error'), 'Not enough inventory')
    
    def test_update_order_status(self):
        order = Order.objects.create(
            customer="John Doe",
            item=self.item,
            quantity=5,
            status='PENDING'
        )
        response = self.client.post(f'/api/update-order/{order.id}/', {
            'status': 'COMPLETED'
        })
        self.assertEqual(response.status_code, 200)
        order.refresh_from_db()
        self.assertEqual(order.status, 'COMPLETED')
