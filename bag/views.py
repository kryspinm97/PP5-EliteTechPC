from django.shortcuts import render


def view_bag(request):

    """ View for rendering the bag page """

    return render(request, 'bag/bag.html')