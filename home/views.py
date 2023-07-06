from django.shortcuts import render

# Create your views here.


def index(request):

    """ Render the Home Page """

    return render(request, 'home/index.html')
