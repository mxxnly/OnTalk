from django.shortcuts import render
from posts_system.models import Post

def home_page(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'html/home.html', {'posts': posts})
