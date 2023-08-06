from django.shortcuts import render
from .models import Item

# Create your views here.

def item_list(request):
    
    context = {
        'items': Item.objects.all()
    }
    return render(request, "index.html", context)


def fashion(request):
    return render(request, 'fashion.html')

def electronics(request):
    return render(request, 'electronic.html')

def jewellery(request):
    return render(request, 'jewellery.html')




