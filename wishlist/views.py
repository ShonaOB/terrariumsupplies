from django.shortcuts import render, redirect
from django.contrib import messages

from products.models import Product
from profiles.models import User, UserProfile
from .models import UserWishlist


def view_wishlist(request):
    """
    A view to return the wishlist of the user
    """
    user = UserProfile.objects.get(user__id=request.user.id)
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
    # get the wishlist
    wishlist = UserWishlist.objects.filter(user__id=request.user.id)
    # create the product
    product = Product.objects.get(pk=item_id)
    # add the product
    wishlist.product.add(product)
    # save the wishlist
    wishlist.save()
