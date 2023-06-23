from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.paginator import Paginator
from .models import PrebuiltPC, Category
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
# Create your views here.


def products_prebuiltpc(request):
    """ A view to show the list of products along with search and sorting """
    products = PrebuiltPC.objects.all()
    query = request.GET.get('q')
    category_values = request.GET.getlist('category')
    sort = 'name'  # Initialize sort with default value
    direction = 'asc'
    categories = None

    if query:
        queries = Q(name__icontains=query) | Q(graphics_card__icontains=query) | Q(processor__icontains=query) | Q(
            ram__icontains=query) | Q(storage__icontains=query)
        products = products.filter(queries)

    if category_values:
        categories = Category.objects.filter(name__in=category_values)
        products = products.filter(category__in=categories)

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

    # Pagination
    paginator = Paginator(products, 6)  # Display 6 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    current_sorting = f'{sort}_{direction}'

    context = {
        'page_obj': page_obj,
        'search_term': query,
        'current_categories': categories if category_values else None,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def prebuiltpc_details(request, product_id):

    """ A view to show individual product details """

    product = get_object_or_404(PrebuiltPC, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/products_details.html', context)