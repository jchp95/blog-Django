from haystack import indexes
from .models import Article, News, Comment, Image, Services, Contact, About, Cursos, TermsAndConditions

class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    content = indexes.CharField(model_attr='content')
    created_at = indexes.DateTimeField(model_attr='created_at')

    def get_model(self):
        return Article

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

class NewsIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    content = indexes.CharField(model_attr='content')
    created_at = indexes.DateTimeField(model_attr='created_at')
    image = indexes.CharField(model_attr='image')

    def get_model(self):
        return News

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

class CommentIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    content = indexes.CharField(model_attr='content')
    created_at = indexes.DateTimeField(model_attr='created_at')
    user = indexes.CharField(model_attr='user__username')

    def get_model(self):
        return Comment

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

# Repite esto para los demás modelos, agregando los campos que consideres necesarios

class ImageIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Image

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

class ServicesIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    description = indexes.CharField(model_attr='description')

    def get_model(self):
        return Services

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

class ContactIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Contact

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

class AboutIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return About

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

class CursosIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Cursos

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

class TermsAndConditionsIndex(indexes.SearchIndex, indexes.Indexable):
    # Definimos el campo que se utilizará para buscar
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        # Devuelve el modelo que estamos indexando
        return TermsAndConditions

    def index_queryset(self, using=None):
        # Devuelve el conjunto de datos que se indexará
        return self.get_model().objects.all()