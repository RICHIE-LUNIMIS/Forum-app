from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
#from AppFacePlant.forms import PostForm
from .models import Post
from .forms import PostForm


def say_hello(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
           form.save()
           return HttpResponseRedirect('/')
        else:
           return HttpResponseRedirect(form.error.as_json())
    posts = Post.objects.all().order_by('-created_at')[:20]
    return render(request, 'posts.html',{'posts':posts})       


def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')
