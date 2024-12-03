from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import Project, Post , Category
from .forms import ContactForm

# Create your views here.

def home(request):
    return render(request, 'portfolio/home.html')



def about(request):
    return render(request, 'portfolio/about.html')




def project(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects':projects})



def blog(request):
    posts = Post.objects.all()
    return render(request, 'portfolio/blog.html', {'posts':posts})




def contact(request):
    if request.method == 'GET':
        form = ContactForm()
        return render(request, 'portfolio/contact.html', {'form':form})
    
    elif request.method =='POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():
            send_mail(
                subject= f"Message from {form.cleaned_data['name']}",
                message= form.cleaned_data['message'],
                from_email= form.cleaned_data['email'],
                recipient_list= [settings.EMAIL_HOST_USER],                
            )
            return render(request, 'portfolio/thabk_you.html')
        
        else:
            form = ContactForm

    return render(request,'portfolio/contact.html', {'form':form})


