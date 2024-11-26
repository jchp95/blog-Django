from django import forms
from .models import TermsAndConditions, Services, Contact, ContactMessage



class TermsAndConditionsForm(forms.ModelForm):
    class Meta:
        model = TermsAndConditions
        fields = ['title', 'acceptance', 'content_usage', 'intellectual_property', 'third_party_links', 'modifications', 'contact' ]  # Reemplaza con los campos reales de tu modelo

class ServicesForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = ['name', 'description']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['title', 'description']

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']


