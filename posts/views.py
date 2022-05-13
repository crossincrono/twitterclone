
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Post
from .forms import PostForm
from django import forms
from urllib import request


def index(request):

#If the method is POST 
    #If the form is valid 
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        # Yes, Save 
        if form.is_valid():
            form.save()
        # Redirect to home
            return HttpResponseRedirect('/')

        else:
            #No, Show Error
            return HttpResponseRedirect(form.errors.as_json())
        
    #Get all posts, limit = 20
    posts = Post.objects.all().order_by("-created_at")

    #Show
    return render ( request, 'posts.html', {'posts': posts})

def delete(request, post_id):

    post =Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')

def LikeView(request,post_id):
    post=Post.objects.get(id=post_id)
    new_value=post.likes +1
    post.likes=new_value
    post.save()
    return HttpResponseRedirect("/")

def edit(request,post_id):
    post=Post.objects.get(id=post_id)
    if request.method == 'POST':
        form=PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form=PostForm(PostForm)
        return render(request,'edit.html', {'post':post, 'form':form})
    