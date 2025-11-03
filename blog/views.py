from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView

from .models import (
    Blog, BlogImages, Category
)
# Create your views here.


class BlogPageView(ListView):
    model = Blog
    template_name = 'blog/blog.html'
    context_object_name = 'blogs'
    ordering = "-created_at"


    def get_context_data(self, **kwargs):


        data = super().get_context_data(**kwargs)
        if self.kwargs.get('pk'):
            data['blogs'] = Blog.objects.filter(category__pk = self.kwargs.get('pk'))
        data['categories'] = Category.objects.all()
        return data

class SingleBlogView(DetailView):
    model = Blog
    template_name = 'blog/blog-single.html'
    context_object_name = 'blog'

