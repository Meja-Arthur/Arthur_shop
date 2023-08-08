from django.urls import path
from . views import (
    HomeView,
    ItemDetailView,
    
)



app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='index_home'),
   
    path('product/<slug>/',ItemDetailView.as_view(), name='product')
    
    #path('fashion/', views.fashion, name='fashion'),
    #path('electronics/', views.electronics, name='electronics'),
    #path('jewellery/', views.jewellery, name='jewellery'),
    
    
]


