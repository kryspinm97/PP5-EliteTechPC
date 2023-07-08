from django.shortcuts import render


def handler404(request, exception):
    """ "
    Handles HTTP 404 errors
    """

    return render(request, "errors/404.html")
