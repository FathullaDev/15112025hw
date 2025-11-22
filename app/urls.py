from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from app.views import *

# urlpatterns = [
#     path('index/',index),
#     path("category/<int:pk>/",supplier_views,name="suppliers"),
#     path("suppliers/<int:pk>/",product_views,name="products"),
#
# ]

urlpatterns = [
    path('', index, name='home'),  # categorylar ro'yxati
    path('category/<int:category_id>/suppliers/', suppliers_by_category, name='suppliers_by_category'),
    path('category/<int:category_id>/supplier/<int:supplier_id>/products/', products_by_supplier_and_category, name='products_by_supplier_and_category'),
    path('add_supplier/',add_supplier,name="add_supplier"),
    path('add_category/',add_category,name="add_category"),
    path('add_product/',add_product,name="add_product"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)