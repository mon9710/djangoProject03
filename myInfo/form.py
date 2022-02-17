from django import forms
from myInfo.models import *

class ProductFormCreate(forms.ModelForm):
    class Meta:
        model = Goods
        fields = ('goodsCategory', 'gid', 'name', 'brand', 'model', 'price', 'net', 'property')
        widgets = {
            'goodsCategory': forms.Select(attrs={'class': 'form-control'}),
            'gid': forms.TextInput({'class': 'form-control', 'required': 'required'}),
            'name': forms.TextInput({'class': 'form-control', 'required': 'required'}),
            'brand': forms.TextInput({'class': 'form-control', 'required': 'required'}),
            'model': forms.TextInput({'class': 'form-control', 'required': 'required'}),
            'price': forms.NumberInput({'class': 'form-control', 'required': 'required', 'Min': 1}),
            'net': forms.NumberInput({'class': 'form-control', 'required': 'required', 'Min': 0}),
            'property': forms.TextInput({'class': 'form-control', 'required': 'required'}),
        }
class ProductFormUpdate(forms.ModelForm):
    class Meta:
        model = Goods
        fields = ('goodsCategory', 'gid', 'name', 'brand', 'model', 'price', 'net', 'property')
        widgets = {
            'goodsCategory': forms.Select(attrs={'class': 'form-control'}),
            'gid': forms.TextInput({'class': 'form-control', 'readonly': 'readonly'}),
            'name': forms.TextInput({'class': 'form-control', 'required': 'required'}),
            'brand': forms.TextInput({'class': 'form-control', 'required': 'required'}),
            'model': forms.TextInput({'class': 'form-control', 'required': 'required'}),
            'price': forms.NumberInput({'class': 'form-control', 'required': 'required', 'Min': 1}),
            'net': forms.NumberInput({'class': 'form-control', 'required': 'required', 'Min': 0}),
            'property': forms.TextInput({'class': 'form-control', 'required': 'required'}),
        }
class CustomerFormCreate(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('cid', 'name', 'surname', 'address', 'telephone', 'gender', 'carreer', 'password')
        widgets = {
            'cid': forms.TextInput({'class': 'form-control', 'required': 'required'}),
            'name': forms.TextInput({'class': 'form-control', 'required': 'required'}),
            'surname': forms.TextInput({'class': 'form-control', 'required': 'required'}),
            'address': forms.TextInput({'class': 'form-control', 'required': 'required'}),
            'telephone': forms.TextInput({'class': 'form-control', 'required': 'required'}),
            'gender': forms.TextInput({'class': 'form-control', 'required': 'required'}),
            'carreer': forms.TextInput({'class': 'form-control', 'required': 'required'}),
            'password': forms.TextInput({'class': 'form-control', 'required': 'required'}),

        }
class CustomerFormUpdate(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('cid', 'name', 'surname', 'address', 'telephone', 'gender', 'carreer', 'password')
        widgets = {
            'cid': forms.TextInput({'class': 'form-control','readonly': 'readonly'}),
            'name': forms.TextInput({'class': 'form-control', 'required': 'required'}),
            'surname': forms.TextInput({'class': 'form-control', 'required': 'required'}),
            'address': forms.TextInput({'class': 'form-control', 'required': 'required'}),
            'telephone': forms.TextInput({'class': 'form-control', 'required': 'required'}),
            'gender': forms.TextInput({'class': 'form-control', 'required': 'required'}),
            'carreer': forms.TextInput({'class': 'form-control', 'required': 'required'}),
            'password': forms.TextInput({'class': 'form-control', 'required': 'required'}),
        }