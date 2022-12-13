from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_reviews, name='all_reviews'),
    path('review_form', views.review_form, name='review_form'),

]
