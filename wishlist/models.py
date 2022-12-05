from django.db import models
from products.models import Product
from profiles.models import User, UserProfile

from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required


class UserWishlist(models.Model):
    product = models.ForeignKey(Product, blank=True, null=False, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    wishlist_name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.wishlist_name
