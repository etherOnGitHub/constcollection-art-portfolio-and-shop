from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Artwork, Tag

class ArtworkForm(forms.ModelForm):
    new_tags = forms.CharField(
        required=False,
        help_text="Comma-separated tags to add",
        widget=forms.TextInput(attrs={'placeholder': 'Enter new tags separated by commas'})
    )

    class Meta:
        model = Artwork
        fields = ['title', 'artist', 'price', 'is_available', 'image_url', 'description', 'tags']
        widgets = {
            'description': SummernoteWidget(),  # Use Summernote for description
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
            self.save_m2m()
            new_tags = self.cleaned_data.get('new_tags')
            if new_tags:
                for name in new_tags.split(','):
                    name = name.strip()
                    if name:
                        tag, _ = Tag.objects.get_or_create(name=name)
                        instance.tags.add(tag)
        return instance