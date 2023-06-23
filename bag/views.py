from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

from products.models import PrebuiltPC


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = PrebuiltPC.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your basket')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust quantity of desired products in the cart """

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop(item_id)
    
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Remove an item from the shopping bag """
    
    bag = request.session.get('bag', {})
    
    if item_id in bag:
        del bag[item_id]
        request.session['bag'] = bag
        return HttpResponse(status=204)  # Return HTTP status 204 (No Content) for successful removal
    
    return HttpResponse(status=400)  # Return HTTP status 400 (Bad Request) if item not found in bag
