from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=30, blank=True, null=True, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    about = models.TextField(max_length=800, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    slug = models.SlugField(null=False)
    logo = models.ImageField(default="default.png")
    welcome = models.CharField(blank=True, null=True, default="Welcome", max_length=200)

    def __str__(self):
        return self.company


class WhyUs(models.Model):
    company = models.OneToOneField(Company, on_delete=models.CASCADE)
    title1 = models.CharField(max_length=25, blank=True, null=True)
    reason1 = models.TextField(max_length=100, blank=True, null=True)
    title2 = models.CharField(max_length=25, blank=True, null=True)
    reason2 = models.TextField(max_length=100, blank=True, null=True)
    title3 = models.CharField(max_length=25, blank=True, null=True)
    reason3 = models.TextField(max_length=100, blank=True, null=True)
    
class New(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=100)
    image = models.ImageField(default="default.png")
    text = models.TextField(max_length=300, blank=True, null=True)

class MainNew(models.Model):
    company = models.OneToOneField(Company, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=100)
    image = models.ImageField(default="default.png")
    text = models.TextField(max_length=300, blank=True, null=True)

class Service(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=25)
    desc = models.TextField(max_length=100, blank=True, null=True)
    

class Product(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default=None)
    image = models.ImageField(default="default.png")
    price = models.FloatField()
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

class Plan(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=25)
    price = models.FloatField()
    desc = models.TextField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.title

class Separator(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=800)
    image = models.ImageField(default="default.png")
    def __str__(self):
        return self.title

class Employer(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    funcion = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField(default="default.png")
    
    def __str__(self):
        return self.name











