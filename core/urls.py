from django.urls import path
from .views import item_list, fashion, electronics, jewellery
app_name = 'core'

urlpatterns = [
    path('', item_list, name='item-list'),
    path('fashion/', fashion, name='fashion'),
    path('electronics/', electronics, name='electronics'),
    path('jewellery/', jewellery, name='jewellery'),
    
]


