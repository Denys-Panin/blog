from django import forms
from django.forms import ModelForm, Textarea, TextInput
from django.utils.translation import gettext_lazy as _

from .models import Author, Post, Subscriber


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "description", "content"]
        widgets = {
            "title": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Название поста",
            }),
            "description": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Краткое описание",
            }),
            "content": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Содержимое",
            })
        }
        error_messages = {
            "title": {
                "max_length": _("This writer's name is too long."),
            },
        }


class SubscriberForm(ModelForm):
    author_id = forms.ModelChoiceField(
        queryset=Author.objects.all().order_by('name'),
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
