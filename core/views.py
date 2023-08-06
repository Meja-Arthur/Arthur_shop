from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Item

# Create your views here.
class HomeView(ListView):
    model = Item
    template_name= "index.html"
    
    






#def fashion(request):
    #return render(request, 'fashion.html')
    
#def electronics(request):
    #return render(request, 'electronic.html')

#def jewellery(request):
    #return render(request, 'jewellery.html')






