from django.urls import path
from . views import (
    HomeView,
    ItemDetailView,
    add_to_cart,
    remove_from_cart,
    
)



app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='index_home'),
    path('product/<slug>/',ItemDetailView.as_view(), name='product'),
    path('add_to_cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove_from_cart/<slug>/', remove_from_cart, name='remove-from-cart')
    
    
    
    
    
    
    #path('fashion/', views.fashion, name='fashion'),
    #path('electronics/', views.electronics, name='electronics'),
    #path('jewellery/', views.jewellery, name='jewellery'),
    
    
]


