from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, CommentForm
from django.urls import reverse
from .models import Post


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


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all
    form = CommentForm()
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', post_id=post_id)
        
    return render(request, 'html/detail_post.html', {'post':post, 
                                                     'comments':comments, 
                                                     'form':form})