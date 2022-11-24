from django.shortcuts import render
from django.contrib import messages

from .forms import OrderForm



def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag, keep shopping!")
        return redirect(reverse('products0'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51A37E6LQ3VKxbQZy7xgllEfJFBscDKyPKONMfim9ajpL9gO9I8efQv1XweUKRT7kOivJtGQOoc8N9kYhk8vmZQ1W00efOJtTIJ',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
