from django import template
from core.models import Order

register = template.Library()  # Use "Library" with a capital "L"

@register.filter
def cart_item_count(user):
    if user.is_authenticated:  # Use "is_authenticated" instead of "authenticated"
        qs = Order.objects.filter(user=user, ordered=False)
        if qs.exists():  # Use "exists()" instead of "exist()"
            return qs[0].items.count()
    return 0
