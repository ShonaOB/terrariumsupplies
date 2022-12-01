from django.shortcuts import render, redirect
from django.contrib import messages

from products.models import Product


def view_wishlist(request):
    """
    A view to return the wishlist of the user
    """

    return render(request, 'wishlist/wishlist.html')


def add_to_wishlist(request, item_id):
    """
    A view to add items to the wishlist
    """
    product = Product.objects.get(pk=item_id)
    quantity = 1
    redirect_url = request.POST.get('redirect_url')
    wishlist = request.session.get('wishlist', {})

    if item_id in list(wishlist.keys()):
        messages.success(request, f'This product ({product.name}) is already in your wishlist')
    else:
        wishlist[item_id] = quantity
        messages.success(request, f'Added {product.name} to your wishlist!')

    request.session['wishlist'] = wishlist
    print(request.session['wishlist'])

    return redirect(redirect_url)
