from django.urls import path
from . import views

urlpatterns=[
    
    path('',views.home,name='home'),
    path('index/',views.index,name='index'),
    path('buy/<int:amount>/<slug:name>/',views.buy,name='buy'),
    path('Seller/',views.Seller,name='Seller'),
]