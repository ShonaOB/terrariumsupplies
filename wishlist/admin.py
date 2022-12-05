from django.contrib import admin
from .models import UserWishlist


class WishlistAdmin(admin.ModelAdmin):
    list_display = (
        'wishlist_name',
        'user',
    )

    ordering = ('product',)


admin.site.register(UserWishlist, WishlistAdmin)
