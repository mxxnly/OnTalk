from django.urls import path
from .views import create_post
urlpatterns = [
    path('create_post', create_post, name='create_post'),
]
