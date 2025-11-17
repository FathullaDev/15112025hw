from django.db import models


class Categories(models.Model):
    category_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    picture=models.ImageField(upload_to='photos/%Y/%m/%d')

    def __str__(self):
        return self.category_name

class Products(models.Model):
    product_name=models.CharField(max_length=100)
    supplier=models.ForeignKey('Suppliers',on_delete=models.CASCADE)
    category=models.ForeignKey('Categories',on_delete=models.CASCADE)
    quantity_per_unit=models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    units_in_stock=models.IntegerField()
    units_on_order=models.IntegerField()
    reorder_level=models.IntegerField()
    discontinued=models.BooleanField()

    def __str__(self):
        return self.product_name

class Suppliers(models.Model):
    company_name = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=100)
    contact_title = models.CharField(max_length=100)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    fax = models.CharField(max_length=50, blank=True, null=True)
    homepage = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.company_name