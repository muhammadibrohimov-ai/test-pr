from django.db import models

# Create your models here.

class Clients(models.Model):
    fullname = models.CharField(max_length=100)
    image = models.FileField(upload_to='clients')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname


class Services(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class People(models.Model):
    fullname = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    desc = models.TextField()
    image = models.FileField(upload_to='people')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname

class PortfolioCategory(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    client = models.ForeignKey('Clients', on_delete=models.CASCADE, related_name='portfolio')
    project_url = models.CharField(max_length=120)
    title = models.CharField(max_length=100)
    desc = models.TextField()
    main_image = models.FileField(upload_to='portfolio')
    category = models.ForeignKey('PortfolioCategory', on_delete=models.CASCADE, related_name='portfolio')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class PortfolioImages(models.Model):
    name = models.CharField(max_length=100)
    image = models.FileField(upload_to='portfolio')
    portfolio = models.ForeignKey('Portfolio', on_delete=models.CASCADE, related_name='images')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

class Team(models.Model):
    fullname = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.FileField(upload_to='people')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname


class Pricing(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    desc = models.TextField()

    def __str__(self):
        return self.name


class Extra(models.Model):
    que = models.TextField()
    ans = models.TextField()

    def __str__(self):
        return self.que

