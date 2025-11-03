from django.urls import path
from .views import BlogPageView, SingleBlogView

urlpatterns = [
    path('', BlogPageView.as_view(), name = 'blog'),
    path('<int:pk>', BlogPageView.as_view(), name = 'blog'),
    path('single/<int:pk>', SingleBlogView.as_view(), name = 'single'),
]