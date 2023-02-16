from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='blog'),
    path('add_post/', views.AddPost.as_view(), name='add_post'),
    path('<post_id>/', views.post_detail, name='post_detail'),
    path('edit_post/<int:post_id>', views.edit_post, name='edit_post'),

]
