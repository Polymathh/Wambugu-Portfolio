# Generated by Django 5.1.2 on 2024-12-29 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog_images/')),
                ('video', models.FileField(blank=True, null=True, upload_to='blog_videos/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
