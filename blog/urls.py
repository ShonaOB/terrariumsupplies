from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='blog'),
    path('add_post/', views.add_post, name='add_post'),
]
