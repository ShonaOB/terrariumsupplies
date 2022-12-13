from django.shortcuts import render
from products.models import Product


def all_reviews(request):
    reviews = Review.objects.all()
    sort = None
    direction = None

    context = {
        'reviews': reviews,
    }

    return render(request, 'reviews/reviews.html', context)
