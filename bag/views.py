from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import PrebuiltPC


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    product = get_object_or_404(PrebuiltPC, pk=item_id)

    if request.method == 'POST':
        quantity = request.POST.get('quantity', '')
    elif request.method == 'GET':
        quantity = request.GET.get('quantity', '')
    else:
        messages.error(request, 'Invalid request.')
        return redirect('products_details', product_id=item_id)

    if not quantity:
        messages.warning(request, 'Please enter a quantity.')
        return redirect('products_details', product_id=item_id)

    try:
        quantity = int(quantity)
        bag = request.session.get('bag', {})
        max_quantity = 10  # Adjust this value to set the maximum quantity

        if quantity <= 0:
            messages.warning(request, 'Quantity must be greater than zero.')
        elif quantity > max_quantity:
            messages.warning(request, f'Maximum quantity for {product.name} is {max_quantity}.')
        else:
            if item_id in bag:
                bag[item_id] += quantity
                messages.success(request, f'Updated quantity of {product.name} in your bag.')
            else:
                bag[item_id] = quantity
                messages.success(request, f'Added {product.name} to your bag.')

        request.session['bag'] = bag
        return redirect('view_bag')
    except ValueError:
        messages.warning(request, 'Invalid quantity value.')
        return redirect('products_details', product_id=item_id)


def adjust_bag(request, item_id):
    """ Adjust quantity of desired products in the cart """

    """ Adjust quantity of desired products in the cart """

    product = get_object_or_404(PrebuiltPC, pk=item_id)
    quantity = request.POST.get('quantity', '')

    if not quantity:
        messages.warning(request, 'Please enter a quantity.')
        return redirect('view_bag')

    try:
        quantity = int(quantity)
        bag = request.session.get('bag', {})
        max_quantity = 10  # Adjust this value to set the maximum quantity

        if quantity <= 0:
            messages.warning(request, 'Quantity must be greater than zero.')
        elif quantity > max_quantity:
            messages.warning(request, f'Maximum quantity for {product.name} is {max_quantity}.')
        else:
            if quantity == 0:
                bag.pop(item_id)
                messages.success(request, f'Removed {product.name} from your basket')
            else:
                bag[item_id] = quantity
                messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')

        request.session['bag'] = bag
    except ValueError:
        messages.warning(request, 'Invalid quantity value.')

    return redirect('view_bag')


def remove_from_bag(request, item_id):

    """ Remove item from the shopping bag """
    try:
        bag = request.session.get('bag', {})
        product = get_object_or_404(PrebuiltPC, pk=item_id)

        if item_id in bag:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')
        else:
            messages.error(request, f'{product.name} is not in your bag')

        request.session['bag'] = bag
        return HttpResponse(status=204)
    except Exception as e:
        messages.error(request, 'Error occurred while removing item from bag')
        return HttpResponse(status=400)
