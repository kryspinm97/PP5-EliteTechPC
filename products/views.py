from django.shortcuts import render, get_object_or_404
from .models import PrebuiltPC
# Create your views here.


def products_prebuiltpc(request):

    """ A view to show the list of products along with search and sorting """

    products = PrebuiltPC.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def prebuiltpc_details(request, product_id):

    """ A view to show individual product details """

    product = get_object_or_404(PrebuiltPC, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/products_details.html', context)