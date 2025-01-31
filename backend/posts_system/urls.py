from django.urls import path
from .views import create_post, post_detail
urlpatterns = [
    path('create_post', create_post, name='create_post'),
    path('post/<int:post_id>', post_detail, name='post_detail')
]
