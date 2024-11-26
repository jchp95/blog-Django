from django import template
import os


register = template.Library()

@register.filter
def add_class(field, css_class):
    return field.as_widget(attrs={"class": css_class})

@register.filter
def highlight(text, query):
    """Resalta las palabras de la consulta en el texto."""
    if not query:
        return text
    return text.replace(query, f'<span class="highlight">{query}</span>')
