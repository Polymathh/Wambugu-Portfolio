from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('about/', views.about, name='About'),
    path('projects/', views.project, name='Projects'),
    path('blog/', views.blog, name='blog'),
]