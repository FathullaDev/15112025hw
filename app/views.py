from django.shortcuts import render

from app.models import *


def index(request):
    categories=Categories.objects.all()
    suppliers=Suppliers.objects.all()
    products=Products.objects.all()

    context={
        'categories':categories,
        'suppliers':suppliers,
        'products':products
    }

    return render(request,'index.html',context)


def category_index(request,pk):
    categories = Categories.objects.all()
    suppliers = Suppliers.objects.all()
    context = {
        'categories': categories,
        'suppliers': suppliers
    }
    return render(request, 'suppliers.html', context)

def suppliers_index(request,pk):
    categories = Categories.objects.all()
    suppliers = Suppliers.objects.all()
    products = Products.objects.all()

    context = {
        'categories': categories,
        'suppliers': suppliers,
        'products': products
    }

    return render(request, 'products.html', context)
