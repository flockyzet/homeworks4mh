from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django import forms

from posts.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "text", "is_published"]


def hello_world(request):
    return HttpResponse("<h1>Hello World!</h1>")


def my_name(request):
    name = "Anvar"
    return HttpResponse(f"<h2>Hello</h2><h1>{name}</h1>")


def say_name(request, name):
    return HttpResponse(f"<h2>Hello</h2><h1>{name}</h1>")


def post_list(request):
    posts = Post.objects.filter(is_published=True)
    return render(request, "list_posts.html", {"posts": posts})


@login_required
def my_posts(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, "my_posts.html", {"posts": posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "post_detail.html", {"post": post})


@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        post.delete()
        return redirect("post_list")

    return render(request, "post_delete.html", {"post": post})


@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            return redirect("post_list")
    else:
        form = PostForm()

    return render(request, "create_post.html", {"form": form})
