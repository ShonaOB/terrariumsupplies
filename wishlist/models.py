from django.db import models
from products.models import Product
from profiles.models import User, UserProfile
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required


class UserWishlist(models.Model):
    product = models.ManyToManyField(Product, blank=True, related_name='products')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    wishlist_name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.wishlist_name


@receiver(post_save, sender=User)
def create_or_update_wishlist(sender, instance, created, **kwargs):
    """
    Create or update the wishlist
    """
    if created:
        UserWishlist.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userwishlist.save()
