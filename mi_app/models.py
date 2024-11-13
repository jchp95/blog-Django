from django import forms  
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.utils import timezone

# Asegúrate de que el modelo de usuario esté bien definido
User  = get_user_model()

class CustomUser_CreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

class Meta:
    model = User
    fields = ('username', 'email', 'password1', 'password2')

class BannerHome(models.Model):
    image = models.ImageField(upload_to='banners/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Banner Home {self.id}"

class Article(models.Model):  
    title = models.CharField(max_length=200)  
    content = models.TextField()  
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.title  


class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='news/')  # Campo para la imagen
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)  # Campo para likes
    dislikes = models.IntegerField(default=0)  # Campo para dislikes
    
    def __str__(self):
        return f"{self.user.username}: {self.content[:20]}"

class Reply(models.Model):
    comment = models.ForeignKey(Comment, related_name='replies', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Image(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')  # Asegúrate de tener Pillow instalado
    link = models.URLField(max_length=200, blank=True, null=True)  # Campo para el enlace
    
    def __str__(self):
        return self.title

class TermsAndConditions(models.Model):
    title = models.CharField(max_length=255)
    last_updated = models.DateField(auto_now=True)
    acceptance = models.TextField()
    content_usage = models.TextField()
    intellectual_property = models.TextField()
    third_party_links = models.TextField()
    modifications = models.TextField()
    contact = models.TextField()

    def __str__(self):
        return self.title

class Services(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name


class Contact(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()     
    

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Mensaje de {self.name} - {self.created_at}'

