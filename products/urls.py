from django.urls import path
from . import views

urlpatterns = [
    path('', views.products_prebuiltpc, name='products'),
    path('products_details/<int:product_id>/',
         views.prebuiltpc_details, name='products_details'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/',
         views.delete_product, name='delete_product'),
]
