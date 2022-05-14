from django.db import models


# Create your models here.
class Mineral(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', blank=True , null=True)
    price = models.IntegerField()
    description = models.TextField(max_length=300)
    
    def __str__(self):
        return self.name
    
    
class Seller(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    mineral = models.ForeignKey(Mineral,on_delete=models.CASCADE)
    amount = models.IntegerField(null=True,blank=True)
    def __str__(self):
        return self.name
    
class Buyer(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField(null=True,blank=True)
    bought_from = models.ForeignKey(Seller,on_delete=models.CASCADE,default=None,null=True,blank=True)
    def reduceSeller(self):
        balance = Seller.objects.get(name='pato')
        balance.amount = balance.amount - self.amount
        balance.save()
    def __str__(self):
        return self.name
 