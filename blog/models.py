from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    author = models.CharField(max_length=200)
    comments = models.PositiveIntegerField()
    desc = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='blog')
    created_at = models.DateTimeField(auto_now_add=True)
    main_image = models.FileField(upload_to='blog', blank=True, null=True)

    def __str__(self):
        return self.title

class BlogImages(models.Model):
    name = models.CharField(max_length=100)
    image = models.FileField(upload_to='blog')
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE, related_name='images')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name