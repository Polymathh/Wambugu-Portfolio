from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length= 100)
    image = models.ImageField(upload_to='portfolio/images')
    description = models.TextField()
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
    


class Category(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name
    
    

class Post(models.Model):
    title = models.CharField(max_length=50)
    image =models.ImageField(upload_to= 'portfolio/images', blank=True)
    content = models.TextField(blank=True)
    date_posted = models.DateTimeField(auto_now_add= True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title