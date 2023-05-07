from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):
    name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'placeholder': 'Имя','class': 'form-control'}))
    email = forms.EmailField(label='Почта', widget=forms.TextInput(attrs={'placeholder': 'Почта', 'class': 'form-control'}))
    specialization = forms.CharField(label='Специализация', widget=forms.TextInput(attrs={'placeholder': 'Специализация', 'class': 'form-control'}))
    mobile = forms.IntegerField(label='Номер телефона', widget=forms.TextInput(attrs={'placeholder': 'Номер телефона', 'class': 'form-control'}))
    address = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'placeholder': 'аддресс','class': 'form-control'}))
    photo = forms.ImageField(label='Фото', widget=forms.TextInput(attrs={'placeholder': 'фото','class': 'form-control'}))
    
    
    class Meta:
        model = Blog
        fields = ('name', 'email', 'specialization','mobile','address','photo')
