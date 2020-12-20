from django.shortcuts import render
from django.shortcuts import render
from .models import Blog
from django.shortcuts import redirect, get_object_or_404


def home(request):
    context = {
        "blog": Blog.objects.all()
    }
    return render(request, 'blog.html', context)

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    context = {
        "blog" : blog
    }

    return render(request, 'detail.html', context)
