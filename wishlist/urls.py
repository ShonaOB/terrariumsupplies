from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_wishlist, name='view_wishlist'),
    path('wishlist_add/<item_id>/', views.add_to_wishlist, name='add_to_wishlist'),
]
