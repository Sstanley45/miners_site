import django


from django.forms import ModelForm
from .models import Mineral, Seller, Buyer

class BuyerForm(ModelForm):
    class Meta:
        model = Buyer
        fields = '__all__'