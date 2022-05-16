from django.urls import path
from . import views

urlpatterns=[
    
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('buy/<int:amount>/<slug:name>/',views.buy,name='buy'),
    path('Seller/',views.Seller,name='Seller'),
]



