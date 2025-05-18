from django.shortcuts import render, get_object_or_404
from .models import BlogPost

def home(request):
    recent_posts = BlogPost.objects.order_by('-created_on')[:3]  # Show 3 recent posts
    return render(request, 'index.html', {'recent_posts': recent_posts})

def blog_list(request):
    posts = BlogPost.objects.all().order_by('-created_on')
    return render(request, 'list.html', {'posts': posts})

def blog_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'details.html', {'post': post})