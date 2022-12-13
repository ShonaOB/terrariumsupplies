from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Review(models.Model):
    """
    Model fields for adding product reviews
    """
    created_on = models.DateTimeField(auto_now_add=True)
    User = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    message = models.TextField(help_text='Add your review here')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'Review {self.message} by {self.User}'
