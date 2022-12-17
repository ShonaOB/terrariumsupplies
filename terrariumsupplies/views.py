from django.shortcuts import render


def error_404(request, exception):
    """"
    Handles HTTP 404 errors
    """

    return render(request, '/terrariumsupplies/templates/errors/404.html')


def error_500(request,):
    """"
    Handles HTTP 500 errors
    """

    return render(request, '/terrariumsupplies/templates/errors/500.html')
