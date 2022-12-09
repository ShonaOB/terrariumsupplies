from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from .forms import ContactForm


def contact(request, *args, **kwargs):
    """
    Displays Contact Us page form.
    Uses Post method to send contact form.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name'],
            email = form.cleaned_data['email'],
            subject = form.cleaned_data['subject'],
            message = form.cleaned_data['message'],
            form.save()

            messages.success(
               request, 'Thank you for contacting us \
                - we will reply within 24 hours!')

            # redirect to home page
            return redirect(reverse('products'))
        else:
            messages.error(
                request, 'Something went wrong with your submission.\
                Please try again.'
            )
    # blank form created if any other method is used
    else:
        form = ContactForm()

    return render(request, 'communications.html', {'form': form})
