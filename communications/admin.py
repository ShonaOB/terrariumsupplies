from django.contrib import admin
from .models import Contact, StallholderApplication


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Displays the fields and values
    for Contact Model in Django admin.
    """
    list_display = (
        'name', 'email', 'subject',
        'message', 'date_submitted'
        )
    search_fields = [
        'name', 'subject', 'message',
        'date_submitted'
        ]
    list_filter = (
        'name', 'date_submitted'
        )


@admin.register(StallholderApplication)
class ApplicationAdmin(admin.ModelAdmin):
    """
    Displays the fields and values
    for Application Model in Django admin.
    """
    list_display = (
        'name', 'email', 'comapny_name',
        'product_type', 'date_submitted'
        )
    search_fields = [
        'name', 'comapny_name', 'product_type',
        'date_submitted'
        ]
    list_filter = (
        'name', 'date_submitted'
        )
