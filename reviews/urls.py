from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_reviews, name='all_reviews'),
    path('review_form', views.review_form, name='review_form'),
    path('update_review/<review_id>', views.update_review, name='update_review'),
    path('delete_review/<review_id>', views.delete_review, name='delete_review'),
]
