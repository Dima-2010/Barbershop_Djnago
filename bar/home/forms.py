from django import forms
from django.forms import TextInput, FileInput, Textarea, CheckboxInput

from home.models import comment


class ReverseForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ['text']
        widgets = {
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Написать отзыв...',
                'rows': 3,
                'style': 'max-width: 360px',
            }),
        }