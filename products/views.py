from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.paginator import Paginator
from .models import PrebuiltPC, Category
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .forms import ProductForm
# Create your views here.


def products_prebuiltpc(request):
    """ A view to show the list of products along with search and sorting """

    # Retrieve all products
    products = PrebuiltPC.objects.all()
    query = request.GET.get('q')
    category_values = request.GET.getlist('category')
    sort = 'name'  # Initialize sort with default value
    direction = 'asc'
    categories = None

    # Filter products based on search query
    if query:
        queries = Q(name__icontains=query) | Q(graphics_card__icontains=query) | Q(processor__icontains=query) | Q(
            ram__icontains=query) | Q(storage__icontains=query)
        products = products.filter(queries)

    # Filter products based on selected categories
    if category_values:
        category_values = category_values[0].split(',') if ',' in category_values[0] else category_values
        category_values = [value for value in category_values if value]
        if category_values:
            categories = Category.objects.filter(name__in=category_values)
            products = products.filter(category__in=categories)

    # Sort products
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
        'current_categories_str': ','.join([cat.name for cat in categories]) if categories else '',
    }

    return render(request, 'products/products.html', context)


def prebuiltpc_details(request, product_id):

    """ A view to show individual product details """

    product = get_object_or_404(PrebuiltPC, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/products_details.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('products_details', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(PrebuiltPC, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('products_details', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(PrebuiltPC, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
