from django.urls import path
from .views import HomePageView, SinglePortfolioView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('<int:pk>', HomePageView.as_view(), name='home'),
    path('portfolio/<int:pk>', SinglePortfolioView.as_view(), name='single')
]