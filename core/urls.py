from django.urls import path
from . views import (
    HomeView,
    
)



app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='index_home'),
    
    #path('fashion/', views.fashion, name='fashion'),
    #path('electronics/', views.electronics, name='electronics'),
    #path('jewellery/', views.jewellery, name='jewellery'),
    
    
]


