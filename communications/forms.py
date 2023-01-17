from django import forms
from .models import Contact, StallholderApplication


class ContactForm(forms.ModelForm):
    """
    Fields used for Contact Us
    form from Contact Model
    """
    name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        max_length=150,
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    subject = forms.CharField(
        max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    message = forms.CharField(
        widget=forms.Textarea(
                attrs={'class': 'form-control',
                       'placeholder': 'Add your message here'}))

    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'message')


class ApplicationForm(forms.ModelForm):
    """
    Fields used for application Us
    form from Stallholder Application Model
    """
    name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        max_length=150,
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    company_name = forms.CharField(
        max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    product_type = forms.CharField(
        widget=forms.Textarea(
                attrs={'class': 'form-control',
                       'placeholder': 'What products do you sell? '}))

    class Meta:
        model = StallholderApplication
        fields = ('name', 'email', 'company_name', 'product_type')
