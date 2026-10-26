from django import forms
from .models import MediaItem


class MediaItemForm(forms.ModelForm):
    class Meta:
        model = MediaItem
        fields = ['title', 'description', 'media_type', 'category', 'media_file', 'thumbnail']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Sunset in Lagos'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Tell us about this media...'}),
            'media_type': forms.Select(attrs={'class': 'form-select'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'media_file': forms.FileInput(attrs={'class': 'form-control'}),
            'thumbnail': forms.FileInput(attrs={'class': 'form-control'}),
        }
