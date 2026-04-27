from django import forms
from .models import Page
from accounts.models import Profile


# 📄 FORM DE PAGES
class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = '__all__'


# 👤 FORM DE PERFIL
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio']