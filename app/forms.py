import re

from django import forms
from django.core.exceptions import ValidationError

from app.models import *
# class CategoryForm(forms.ModelForm):
#     class Meta:
#         model = Categories
#         fields = '__all__'
#         widgets = {
#             'category_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
#             'picture': forms.FileInput(attrs={'class': 'form-control'}),
#         }


class CategoryForm(forms.Form):
    category_name = forms.CharField(
        label="Category name",
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    description = forms.CharField(
        label="Description",
        required=False,
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "rows": 5
        })
    )

    picture = forms.ImageField(label="Picture")


# class SupplierForm(forms.ModelForm):
#     class Meta:
#         model = Suppliers
#         fields = '__all__'
#         widgets = {
#             'company_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'contact_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'contact_title': forms.TextInput(attrs={'class': 'form-control'}),
#             'address': forms.TextInput(attrs={'class': 'form-control'}),
#             'city': forms.TextInput(attrs={'class': 'form-control'}),
#             'region': forms.TextInput(attrs={'class': 'form-control'}),
#             'postal_code': forms.TextInput(attrs={'class': 'form-control'}),
#             'country': forms.TextInput(attrs={'class': 'form-control'}),
#             'phone': forms.TextInput(attrs={'class': 'form-control'}),
#             'fax': forms.TextInput(attrs={'class': 'form-control'}),
#             'homepage': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
#         }

from django import forms

class SupplierForm(forms.Form):
    company_name = forms.CharField(
        label="Company Name",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    contact_name = forms.CharField(
        label="Contact Name",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    contact_title = forms.CharField(
        label="Contact Title",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    address = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    city = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    region = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    postal_code = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    country = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    phone = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    fax = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    homepage = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 3})
    )


# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = Products
#         fields = '__all__'
#         widgets = {
#             'product_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'supplier': forms.Select(attrs={'class': 'form-control'}),
#             'category': forms.Select(attrs={'class': 'form-control'}),
#             'quantity_per_unit': forms.NumberInput(attrs={'class': 'form-control'}),
#             'unit_price': forms.NumberInput(attrs={'class': 'form-control'}),
#             'units_in_stock': forms.NumberInput(attrs={'class': 'form-control'}),
#             'units_on_order': forms.NumberInput(attrs={'class': 'form-control'}),
#             'reorder_level': forms.NumberInput(attrs={'class': 'form-control'}),
#             'discontinued': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
#         }


from django import forms
from .models import Suppliers, Categories

class ProductForm(forms.Form):
    product_name = forms.CharField(
        label="Product name",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    supplier = forms.ModelChoiceField(
        queryset=Suppliers.objects.all(),
        label="Supplier",
        widget=forms.Select(attrs={"class": "form-control"})
    )

    category = forms.ModelChoiceField(
        queryset=Categories.objects.all(),
        label="Category",
        widget=forms.Select(attrs={"class": "form-control"})
    )

    quantity_per_unit = forms.IntegerField(
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )

    unit_price = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )

    units_in_stock = forms.IntegerField(
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )

    units_on_order = forms.IntegerField(
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )

    reorder_level = forms.IntegerField(
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )

    discontinued = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"})
    )
