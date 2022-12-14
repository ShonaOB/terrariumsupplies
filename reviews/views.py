from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from products.models import Product
from .forms import ReviewForm
from reviews.models import Review


def all_reviews(request, product):
    product = Product.name
    reviews = Review.objects.filter(product)
    sort = None
    direction = None

    context = {
        'reviews': reviews,
        'product': product,
    }

    return render(request, 'reviews/reviews.html', context)


@login_required()
def review_form(request, *args, **kwargs):
    """
    Displays review form.
    Uses Post method to send review form.
    """
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        user = request.user
        if form.is_valid():
            form.instance.User = request.user
            form.save()
            messages.success(request, 'Thank you for your review!')

            # redirect to home page
            return redirect(reverse('products'))
        else:
            messages.error(
                request, 'Something went wrong with your submission.\
                Please try again.'
            )
    # blank form created if any other method is used
    else:
        form = ReviewForm()

    return render(request, 'reviews.html', {'form': form})


@login_required
def update_review(request, review_id):
    """
    updating a review for user without accessing admin
    """
    review = Review.objects.get(id=review_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.instance.User = request.user
            form.save()
            messages.success(request, 'Successfully updated your review!')
            return redirect(reverse('products'))
        else:
            messages.error(request, 'Oops'
                           'that did not work, please check your form again')
    else:
        form = ReviewForm(instance=review)
        messages.info(request, f'You are updating your review')

    template = 'update_review.html'
    context = {
        'form': form,
        'review': review,
    }

    return render(request, template, context)


@login_required
def delete_review(request, review_id):
    """
    updating a review for user without accessing admin
    """
    review = Review.objects.get(id=review_id)
    review.delete()

    messages.success(request, 'You have deleted your review')

    return redirect('profile')
