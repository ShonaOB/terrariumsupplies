from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

from products.models import Product


def view_bag(request):
    """
    A view to return the shopping bag
    """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """
    A view to add items to the shopping bag
    """
    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request, f'Added {product.name} x {quantity} to your bag')
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} x {quantity} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """
    A view to adjust items in the bag
    """
    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request, f'Added another {product.name} to your bag. Total number in bag: {quantity}!')
    else:
        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag')
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    product = Product.objects.get(pk=item_id)
    bag = request.session.get('bag', {})

    try:
        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from to your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
        messages.error(request, f'Oops! An error occured. Please try again.')
