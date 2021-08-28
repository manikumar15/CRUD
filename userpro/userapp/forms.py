from django.core import validators
from django import forms
from .models import User


class user_form(forms.ModelForm):
	class Meta:
		model = User
		fields = ['product_name','volume','market_capital','credit_rating']
		widgets = {
		'product_name': forms.TextInput(attrs={'class':'form-control'}),
		'volume': forms.TextInput(attrs={'class':'form-control'}),
		'market_capital': forms.TextInput(attrs={'class':'form-control'}),
		'credit_rating': forms.TextInput(attrs={'class':'form-control'}),
		}
