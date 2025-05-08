# forms.py
from django import forms
from .models import ContactMessage, CustomUser as User
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

User = get_user_model()

class ContactForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())

    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'phone', 'password', 'zip_code', 'referral_code']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password'])  # Hash password
        if commit:
            user.save()
        return user