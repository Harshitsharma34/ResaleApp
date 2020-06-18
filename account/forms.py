from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from product.models import Product

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields= ['username', 'email' , 'password1' , 'password2']

class AdForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','image','description','price','category','condition']
