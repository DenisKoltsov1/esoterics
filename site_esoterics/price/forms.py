from django import forms
from .models import Price



class PriceForm(forms.ModelForm):

    title = forms.CharField(label='Название услуги ', widget=forms.TextInput(attrs={'placeholder': 'Название услуги','class': 'form-control'}))
    content = forms.CharField(label='Описание услуги', widget=forms.Textarea(attrs={'placeholder': 'Описание услуги', 'class': 'form-control'}))
    price = forms.IntegerField(label='Цена услуги', widget=forms.TextInput(attrs={'placeholder': 'Цена услуги', 'class': 'form-control'}))
    
    class Meta:
        model = Price
        fields = ('title', 'content', 'price')