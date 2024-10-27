from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Order, Inventory
from django.core.cache import cache

@csrf_exempt
@transaction.atomic
def create_order(request):
    item_id = request.POST.get('item_id')
    quantity = int(request.POST.get('quantity'))
    
    with transaction.atomic():
        item = Inventory.objects.select_for_update().get(id=item_id)
        if item.quantity >= quantity:
            order = Order.objects.create(
                customer=request.POST.get('customer'),
                item=item,
                quantity=quantity,
                status='PENDING'
            )
            item.quantity -= quantity
            item.save()
            return JsonResponse({'message': 'Order created successfully', 'order_id': order.id})
        else:
            return JsonResponse({'error': 'Not enough inventory'}, status=400)

@csrf_exempt
@transaction.atomic
def update_order(request, order_id):
    status = request.POST.get('status')
    order = get_object_or_404(Order, id=order_id)

    with transaction.atomic():
        order.status = status
        order.save()
        return JsonResponse({'message': f'Order {order_id} updated successfully'})
    

def get_inventory(request):
    inventory = cache.get('inventory')
    if not inventory:
        inventory = list(Inventory.objects.all().values('item', 'quantity'))
        cache.set('inventory', inventory, timeout=60*15)  # Cachea por 15 minutos
    return JsonResponse(inventory, safe=False)
   
