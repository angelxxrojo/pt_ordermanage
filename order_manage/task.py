from celery import shared_task
from .models import Inventory

@shared_task
def update_inventory(item_id, quantity):
    try:
        item = Inventory.objects.get(id=item_id)
        item.quantity -= quantity
        item.save()
        print(f'Inventory updated successfully for item {item_id}')
    except Inventory.DoesNotExist:
        print(f'Item {item_id} does not exist.')
