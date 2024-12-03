from django.contrib import admin
from .models import Project,Post,Category

# Register your models here.
admin.site.register(Project)
admin.site.register(Post)
admin.site.register(Category)

