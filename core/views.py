from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/blog_list.html', {'blogs': blogs})

def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/blog_presentation.html', {'blog': blog})

