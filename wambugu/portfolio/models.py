from django.db import models

# Create your models here.

from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    category = models.CharField(
        max_length=50,
        choices=[
            ('Mobile Apps', 'Mobile Apps'),
            ('Web Apps', 'Web Apps'),
            ('Graphic Design', 'Graphic Design'),
        ]
    )
    live_demo_url = models.URLField(blank=True, null=True)  
    video_demo = models.FileField(upload_to='project_videos/', blank=True, null=True)  

    def __str__(self):
        return self.title

    

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    video = models.FileField(upload_to='blog_videos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

