from django.shortcuts import render, get_object_or_404
from .models import Project, BlogPost
from django.core.mail import send_mail


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def blog(request):
    return render(request, 'blog.html')


def video_demo(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'video_demo.html', {'project': project})


def portfolio(request):
    categories = [
        {"name":"Mobile Apps", "description":"Explore mobile applications that I've built with innovative designs and efficient functionality."},
        {"name":"Web Apps", "description":"A showcase of modern, responsive, and user-friendly websites."},
        {"name": "Graphic Design", "description": "Creative graphic design projects showcasing branding and artistic skills."}
    ]
    return render(request, 'portfolio.html', {'categories': categories})



def category_projects(request, category_name):
    projects = Project.objects.filter(category=category_name)
    return render(request, 'category_projects.html', {'category_name': category_name, 'projects': projects})




def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        send_mail(
            f"Portfolio Contact: {name}",
            message,
            email,
            ['wambuguworking@gmail.com'],  
        )    

        return render(request, 'contact.html', {'success': True})

    return render(request, 'contact.html')



def blog(request):
    posts = BlogPost.objects.all().order_by('created_at')
    return render(request, 'blog.html', {'posts':posts})

