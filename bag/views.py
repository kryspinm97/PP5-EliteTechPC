from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import PrebuiltPC


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    product = get_object_or_404(PrebuiltPC, pk=item_id)

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        bag = request.session.get('bag', {})

        if item_id in bag:
            bag[item_id] += quantity
            messages.success(request, f'Updated quantity of {product.name} in your bag.')
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag.')

        request.session['bag'] = bag
        return redirect('view_bag')
    elif request.method == 'GET':
        quantity = int(request.GET.get('quantity', 1))
        bag = request.session.get('bag', {})
        
        if item_id in bag:
            bag[item_id] += quantity
            messages.success(request, f'Updated quantity of {product.name} in your bag.')
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag.')

        request.session['bag'] = bag
        return redirect('view_bag')
    else:
        messages.error(request, 'Invalid request.')

    return redirect('products_details', product_id=item_id)


def adjust_bag(request, item_id):
    """ Adjust quantity of desired products in the cart """

    product = get_object_or_404(PrebuiltPC, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(
            request, f'Updated {product.name} quantity to {bag[item_id]}')
    else:
        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your basket')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Remove an item from the shopping bag """

    product = get_object_or_404(PrebuiltPC, pk=item_id)
    bag = request.session.get('bag', {})

    if item_id in bag:
        del bag[item_id]
        request.session['bag'] = bag
        messages.success(request, f'Removed {product.name} from your basket')
        # Return HTTP status 204 (No Content) for successful removal
        return HttpResponse(status=204)

    # Return HTTP status 400 (Bad Request) if item not found in bag
    return HttpResponse(status=400)
