from django.urls import path
from . import views

urlpatterns = [
    path('', views.products_prebuiltpc, name='products'),
    path('<product_id>', views.prebuiltpc_details, name='products_details'),
]