from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Artwork

class ArtworkForm(forms.ModelForm):
    description = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = Artwork
        fields = [
            "title",
            "slug",
            "artist",
            "price",
            "is_available",
            "image_url",
            "video_url",
            "description",
            "tags",
        ]
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }