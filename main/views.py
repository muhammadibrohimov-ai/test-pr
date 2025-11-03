from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from .models import (
    Clients,
    Services,
    People,
    PortfolioCategory,
    Portfolio,
    PortfolioImages,
    Team,
    Pricing,
    Extra
)

# Create your views here.

class HomePageView(ListView):
    model = Clients
    template_name = 'main/index.html'
    context_object_name = 'clients'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['services'] = Services.objects.all()
        if self.kwargs.get('pk'):
            data['portfolio'] = Portfolio.objects.filter(category__pk = self.kwargs.get('pk'))
        else:
            data['portfolio'] = Portfolio.objects.all()
        data['people'] = People.objects.all()
        data['categories'] = PortfolioCategory.objects.all()
        data['team'] = Team.objects.all()
        data['pricing'] = Pricing.objects.all()
        data['que'] = Extra.objects.all()

        return data


class SinglePortfolioView(DetailView):
    model = Portfolio
    template_name = 'main/portfolio-details.html'
    context_object_name = 'item'

