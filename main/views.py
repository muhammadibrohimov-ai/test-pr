from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView


# Create your views here.

class HomePageView(TemplateView):
    template_name = 'main/index.html'
