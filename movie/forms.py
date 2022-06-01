from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class meta:
        model = Comment
        fields = ('commentor_name', 'comment_body')
        widgets = {
            'commentor_name': forms.TextInput(attrs={'class': 'form-control'}),
            'comment_body': forms.Textarea(attrs={'class': 'form-control'}),
        }
