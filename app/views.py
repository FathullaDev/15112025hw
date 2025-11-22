from django.shortcuts import render, get_object_or_404, redirect
from app.forms import *
from app.models import *


def index(request):
    categories = Categories.objects.all()
    return render(request, 'index.html', {'categories': categories})


def suppliers_by_category(request, category_id):
    category = get_object_or_404(Categories, pk=category_id)
    suppliers = Suppliers.objects.all()
    return render(request, 'suppliers.html', {
        'category': category,
        'suppliers': suppliers,
    })

def products_by_supplier_and_category(request, category_id, supplier_id):
    category = get_object_or_404(Categories, pk=category_id)
    supplier = get_object_or_404(Suppliers, pk=supplier_id)
    products = Products.objects.filter(category=category, supplier=supplier)
    return render(request, 'products.html', {
        'category': category,
        'supplier': supplier,
        'products': products,
    })


def add_category(request):
    if request.method=="POST":
        form=CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            # form.save()
            category=Categories.objects.create(**form.cleaned_data)
            return redirect('home')
    else:
        form=CategoryForm()
    return render(request,'add_category.html',{'form':form})

def add_supplier(request):
    if request.method=="POST":
        form=SupplierForm(request.POST, request.FILES)
        if form.is_valid():
            # form.save()
            supplier = Suppliers.objects.create(**form.cleaned_data)
            return redirect('home')
    else:
        form=SupplierForm()
    return render(request,'add_supplier.html',{'form':form})

def add_product(request):
    if request.method=="POST":
        form=ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # product=Products.objects.create(**form.cleaned_data)
            return redirect('home')
    else:
        form=ProductForm()
    return render(request,'add_product.html',{'form':form})