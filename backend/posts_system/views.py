from django.shortcuts import render, redirect
from .forms import PostForm
from django.urls import reverse

def create_post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(reverse('home'))
    else:
        post_form = PostForm()

    return render(request, 'html/create_post.html', {'post_form': post_form})
