from django.shortcuts import render, redirect
from django.contrib import messages

from products.models import Product
from profiles.models import User, UserProfile
from .models import UserWishlist


def view_wishlist(request):
    """
    A view to return the wishlist of the user
    """
    user = UserProfile.user
    wishlist = UserWishlist.objects.all()
    context = {
        'user': user,
        'wishlist': wishlist, 
    }

    return render(request, 'wishlist/wishlist.html', context)


def add_to_wishlist(request, item_id):
    """
    A view to add items to the wishlist
    """
    user = request.user
    product = Product.objects.get(pk=item_id)
    quantity = 1
    redirect_url = request.POST.get('redirect_url')
    wishlist = UserWishlist()

    wishlist[product] = quantity
    messages.success(request, f'Added {product.name} to your wishlist!')

    request['wishlist_contents'] = wishlist
    print(request.session['wishlist'])

    return redirect(redirect_url)
