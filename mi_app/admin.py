from django.contrib import admin
from django.contrib.auth.models import User
from .models import News, Article, Comment, Image, TermsAndConditions, Services, Contact, BannerHome, About, Carousel, CarouselCursos, FAQ
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

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    fields = (
        'team_description',
        'team_image',
        'what_you_can_find',
        'why_we_do_it',
        'core_value_1',
        'core_value_2',
        'core_value_3',
        'core_value_4',
        'core_value_5',
        'contact_email',
        'facebook_url',
        'whatsapp_url',
        'footer_message',
    )
    

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question',)  # Muestra solo la pregunta en la lista
    search_fields = ('question',)  # Permite buscar por pregunta




admin.site.register(Carousel)
admin.site.register(CarouselCursos)
