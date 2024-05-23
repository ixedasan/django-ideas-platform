from django import forms
from .models import Ideas, Comments


class IdeasForm(forms.ModelForm):
    class Meta:
        model = Ideas
        fields = ['title', 'summary', 'goal', 'description']
        labels = {
            'title': 'Title',
            'summary': 'Summary',
            'goal': 'Goal',
            'description': 'Description'
        }
        widgets = {
            'title': forms.TextInput(),
            'summary': forms.Textarea(),
            'goal': forms.Textarea(),
            'description': forms.Textarea(),
        }


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment']
