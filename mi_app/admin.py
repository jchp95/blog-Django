from django.contrib import admin
from django.contrib.auth.models import User
from .models import News, Article, Comment, Image, TermsAndConditions, Services, Contact, BannerHome, About, Carousel
from .models import ContactMessage




admin.site.register(TermsAndConditions)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')  # Asegúrate de usar atributos válidos

@admin.register(BannerHome)
class BannerHomeAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at')


admin.site.register(News, NewsAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'created_at')
    search_fields = ('user__username', 'content')
    list_filter = ('created_at',)

    

admin.site.register(Comment, CommentAdmin)

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'link')  # Campos que se mostrará
    fields = ('title', 'description', 'image', 'link')

# Nueva clase para el modelo Servicio
@admin.register(Services)  # Registra el modelo Servicio
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Campos que se mostrarán en la lista
    search_fields = ('name',)  # Permite buscar por nombre

admin.site.register(ContactMessage)
# Nueva clase para el modelo COntacto
@admin.register(Contact)  # Registra el modelo Servicio
class ContactAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')  # Campos que se mostrarán en la lista
    fields = ('title', 'description')  # Permite buscar por nombre

admin.site.register(About)
admin.site.register(Carousel)