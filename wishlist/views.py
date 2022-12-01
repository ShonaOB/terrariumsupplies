from django.shortcuts import render

def view_wishlist(request):
    """ 
    A view to return the wishlist of the user
    """

    return render(request, 'wishlist/wishlist.html')
