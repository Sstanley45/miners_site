from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Mineral, Seller, Buyer
from django.contrib.auth.models import User
from .forms import BuyerForm

# Create your views here.

def home(request):
    mineral = Mineral.objects.all()
    context = {
        'minerals': mineral}
    return render(request, 'home.html', context)
    

def index(request,amount):
    buyer = Buyer.objects.all()
    form = BuyerForm()
    form.amount = amount
    context = {'form': form}
    return render(request, 'index.html', context)



def buy(request,amount,name):
    buy = Buyer.objects.create(amount=amount,name=str(request.user.username),bought_from=Seller.objects.filter(mineral__exact=name)[0])
    buy.save()
    
    return HttpResponseRedirect('/')
def Seller(request):
    Seller = Seller.objects.all()
    context = {
        'sellers': Seller
        }
    return render(request, 'Seller.html', context)
    
        
        
