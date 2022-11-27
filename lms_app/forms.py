from django import forms
from .models import *
class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name',]
        widgets = {
        'name' : forms.TextInput(attrs={'class' : 'form-control'})
    }

class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'image',
            'image_author',
            'pages',
            'price',
            'rental_price',
            'rental_period',
            'rental_total',
            'status',
            'category',     
            'active',
        ]
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control'}),
            'author' : forms.TextInput(attrs={'class' : 'form-control'}),
            'image' : forms.FileInput(attrs={'class' : 'form-control'}),
            'image_author' : forms.FileInput(attrs={'class' : 'form-control'}),
            'pages' : forms.NumberInput(attrs={'class' : 'form-control'}),
            'price' : forms.NumberInput(attrs={'class' : 'form-control'}),
            'rental_price' : forms.NumberInput(attrs={'class' : 'form-control', 'id' : 'rentalprice'}),
            'rental_period' : forms.NumberInput(attrs={'class' : 'form-control', 'id' : 'rentalperiod'}),
            'rental_total' : forms.NumberInput(attrs={'class' : 'form-control' , 'id' : 'rentaltotal'}),
            'status' : forms.Select(attrs={'class' : 'form-control'}),
            'category' : forms.Select(attrs={'class' : 'form-control'}),
            'active' : forms.CheckboxInput(attrs={'class' : 'form-control'}),
        }
