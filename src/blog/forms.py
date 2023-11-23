from django import forms
from django.forms import ModelForm, Textarea, TextInput
from django.utils.translation import gettext_lazy as _

from .models import Author, Article, Subscriber, Category


class ArticleForm(ModelForm):
    author = forms.ModelChoiceField(
        queryset=Author.objects.all().order_by('first_name'),
        empty_label='Оберіть автора...',
        widget=forms.Select(attrs={
            "class": "form-control",
        }),
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all().order_by('name'),
        empty_label='Оберіть категорію...',
        widget=forms.Select(attrs={
            "class": "form-control",
        }),
    )

    class Meta:
        model = Article
        fields = ["title", "description", "content", "author", "category"]
        widgets = {
            "title": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Название article",
            }),
            "description": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Краткое article",
            }),
            "content": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Содержимое",
            })
        }


class SubscriberForm(ModelForm):
    author_id = forms.ModelChoiceField(
        queryset=Author.objects.all().order_by('first_name'),
        empty_label='Выберите автора...',
        widget=forms.Select(attrs={
            "class": "form-control",
        }),
    )

    class Meta:
        model = Subscriber
        fields = ["name", "email_to", "author_id"]
        widgets = {
            "name": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Name подписчика"
            }),
            "email_to": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Email подписчика",
            })
        }
