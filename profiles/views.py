from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from products.models import PrebuiltPC
from .models import UserProfile, Wishlist
from .forms import UserProfileForm
from checkout.models import Order


@login_required
def profile(request):
    """ Display the user's profile. """

    profile = get_object_or_404(UserProfile, user=request.user)

    # Get the user's wishlist, or create a new one if it doesn't exist
    try:
        wishlist = Wishlist.objects.get(user=request.user)
    except Wishlist.DoesNotExist:
        wishlist = None

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'wishlist': wishlist,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    """ Display a past order confirmation. """

    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}.'
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def add_to_wishlist(request, product_id):

    """ Add a product to the user's wishlist """

    product = get_object_or_404(PrebuiltPC, id=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)

    if product not in wishlist.products.all():
        wishlist.products.add(product)
        messages.success(request, 'Product added to wishlist.')
    else:
        messages.info(request, 'Product is already in wishlist.')

    return redirect('products_details', product_id=product_id)


@login_required
def remove_from_wishlist(request, product_id):

    """ Remove a product from the user's wishlist """

    product = get_object_or_404(PrebuiltPC, id=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)

    product = get_object_or_404(PrebuiltPC, id=product_id)
    wishlist = Wishlist.objects.get(user=request.user)

    if product in wishlist.products.all():
        wishlist.products.remove(product)
        messages.success(request, 'Product removed from wishlist.')
    else:
        messages.info(request, 'Product is not in wishlist.')

    return redirect('products_details', product_id=product_id)
