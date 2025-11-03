from django.shortcuts import render
from django.views.generic import ListView, TemplateView

# Create your views here.


class BlogPageView(TemplateView):
    template_name = 'blog/blog.html'