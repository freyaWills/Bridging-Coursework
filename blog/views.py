from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import HttpResponse
from .models import Post
from .models import Item
from .forms import PostForm
from .forms import ItemForm
from django.shortcuts import redirect

# Create your views here.

def welcome_page(request):
    return render(request, 'blog/welcome_page.html', {})

def cv_edit(request):

    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            return redirect('/cv/edit')
    else:
        form = ItemForm()

    return render(request, 'blog/cv_edit.html', {'form': form})

def cv_view(request):
    items = Item.objects.all().order_by('-endDate') 
    return render(request, 'blog/cv_view.html', {'items': items})

def post_list(request):
    #Publish blog posts sorted by publish date
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

