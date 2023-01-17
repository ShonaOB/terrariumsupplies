from django.urls import path
from . import views


urlpatterns = [
    path('', views.contact, name='contact'),
    path('stallholder_application',
         views.StallholderApplication, name='stallholderapplication'),
]
