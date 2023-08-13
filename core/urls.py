from django.urls import path
from .views import CustomLoginView
from . views import (
    HomeView,
    ItemDetailView,
    add_to_cart,
    remove_from_cart,
    OrderSummeryView,
    
)



app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='index_home'),
    path('accounts/login/', CustomLoginView.as_view(), name='account_login'),
    path('order-summary/',OrderSummeryView.as_view(), name='order-summary'),
    path('product/<slug>/',ItemDetailView.as_view(), name='product'),
    path('add_to_cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove_from_cart/<slug>/', remove_from_cart, name='remove-from-cart')
    
    
    
    
    
    

    
    
]


