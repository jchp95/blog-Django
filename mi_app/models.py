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
    image = models.ImageField(upload_to='banners/', blank=True, null=True)
    text = models.CharField(max_length=255, blank=True, null=True)  # Campo para el texto
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

class Carousel(models.Model):
    image = models.ImageField(upload_to='carousel_images/')

    def __str__(self):
        return f"Carousel {self.id}"

class CarouselCursos(models.Model):
    image = models.ImageField(upload_to='carousel_images/')

    def __str__(self):
        return f"CarouselCursos {self.id}"    


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

class About(models.Model):
    team_description = models.TextField()
    team_image = models.ImageField(upload_to='team_images/', null=True, blank=True) 
    what_you_can_find = models.TextField()  # Para almacenar una lista de elementos
    why_we_do_it = models.TextField()

    core_value_1 = models.CharField(max_length=255, default='Valor por defecto 1')  # Define un valor predeterminado
    core_value_2 = models.CharField(max_length=255, default='Valor por defecto 2')  # Define un valor predeterminado
    core_value_3 = models.CharField(max_length=255, default='Valor por defecto 3')  # Define un valor predeterminado
    core_value_4 = models.CharField(max_length=255, default='Valor por defecto 4')  # Define un valor predeterminado
    core_value_5 = models.CharField(max_length=255, default='Valor por defecto 5')  # Define un valor predeterminado
    
    contact_email = models.EmailField()
    facebook_url = models.URLField()
    whatsapp_url = models.URLField()
    footer_message = models.TextField()

    def __str__(self):
        return "About Page Content"


class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question





