# forms.py
from django import forms
from .models import ContactMessage, Driver
from django.contrib.auth.hashers import make_password

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']

class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['first_name', 'last_name', 'email', 'phone', 'password', 'zip_code', 'referral_code']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def save(self, commit=True):
        driver = super().save(commit=False)
        driver.password = make_password(self.cleaned_data['password'])  # Hash password
        if commit:
            driver.save()
        return driver