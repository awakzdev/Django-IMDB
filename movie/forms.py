from django import forms
from . import models
from .models import Comment


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-outline form-white',
        'placeholder': 'comment here ...',
        'rows': '5',
        'cols': '161',
    }))

    class Meta:
        model = Comment
        fields = ('content', )