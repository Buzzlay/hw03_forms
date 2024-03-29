from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Post, Group
from .forms import PostForm


def index(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, "index.html", {
        'page': page, 'paginator': paginator
    })


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    group_posts_list = group.posts.all()
    paginator = Paginator(group_posts_list, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, "group.html", {
        'group': group, 'page': page, 'paginator': paginator
    })


@login_required
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('index')
        return render(request, 'newpost.html', {'form': form})
    form = PostForm()
    return render(request, 'newpost.html', {'form': form})


def profile(request, username):

    author = User.objects.get(username=username)
    author_posts = Post.objects.filter(author__username=username)
    paginator = Paginator(author_posts, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'profile.html', {
        'author': author, 'author_posts': author_posts,
        'paginator': paginator, 'page': page
    })


def post_view(request, username, post_id):
    post = Post.objects.get(id=post_id)
    author = User.objects.get(username=username)
    author_posts = Post.objects.filter(author__username=username)
    return render(request, 'post.html', {
        'post': post, 'author': author, 'author_posts': author_posts
    })


@login_required
def post_edit(request, username, post_id):
    if request.user.username != username:
        return redirect(
            reverse(
                'post', kwargs={'username': username, 'post_id': post_id}
            )
        )
    target_post = get_object_or_404(Post, pk=post_id)
    form = PostForm(request.POST or None, instance=target_post)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'post_new.html', {
        'form': form, 'username': username, 'post_id': post_id
    })

