from decimal import Decimal
from django.shortcuts import get_object_or_404
from shop.models import Product

def bag_contents(request):
    bag_items = []
    total = 0
    product_count = 0

    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        grand_total = total
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
        }
        
    return context