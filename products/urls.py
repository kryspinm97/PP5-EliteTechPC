from django.urls import path
from . import views

urlpatterns = [
    path('', views.products_prebuiltpc, name='products'),
    path('<int:product_id>/', views.prebuiltpc_details, name='products_details'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
]
