from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Item,OrderItem, Order
from django.shortcuts import redirect
from django.utils import timezone
from allauth.account.views import LoginView
from django.urls import reverse_lazy

# Create your views here.

class CustomLoginView(LoginView):
    # You can customize behavior here if needed
    template_name = 'account/login.html'
    



class HomeView(ListView):
    model = Item
    template_name= "index.html"
    
    
class ItemDetailView(DetailView):
    model = Item
    template_name = "productdetails.html"

def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )

    # check if the user has an order
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        #check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "Item quantity was updated.")
            return redirect("core:product", slug=slug)       
        else:
            messages.info(request, "Item add to the cart.")
            order.items.add(order_item)  
            return redirect("core:product", slug=slug) 
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item) 
        messages.info(request, "Item add to the cart.")
        return redirect("core:product", slug=slug)  


def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    
    if order_qs.exists():
        order = order_qs[0]
        #check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.get_or_create(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item) 
            messages.info(request, "Item was removed from the cart.")
            return redirect("core:product", slug=slug) 
        else:
            #add a message saying the order does not has items 
            messages.info(request, "Item was not in the cart.")
            return redirect("core:product", slug=slug) 
                
        
            
    else:
        #add a message saying the user has no order
        messages.info(request, "You have no active order.")
        return redirect("core:product", slug=slug)       
    
      
    
    
 
    
 






