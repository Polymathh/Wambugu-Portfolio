from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio, name= 'portfolio'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('portfolio/<str:category_name>/', views.category_projects, name='category_projects'),
    path('blog/', views.blog, name='blog'),
    
]