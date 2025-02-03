from django.urls import path
from . import views
from .views import video_demo
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('video-demo/<int:project_id>/', video_demo, name='video_demo'),
    path('', views.portfolio, name= 'portfolio'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('portfolio/<str:category_name>/', views.category_projects, name='category_projects'),
    path('blog/', views.blog, name='blog'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
