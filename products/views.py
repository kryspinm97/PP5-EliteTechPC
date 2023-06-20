from django.shortcuts import render
from .models import PrebuiltPC
# Create your views here.


def products_prebuiltpc(request):

    """ A view to show the list of products along with search and sorting """

    products = PrebuiltPC.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)