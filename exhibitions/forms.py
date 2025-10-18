from .models import Exhibition
from django import forms

class ExhibitionForm(forms.ModelForm):
    class Meta:
        model = Exhibition
        fields = ['title', 'cover_image', 'video', 'description', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'summernote'}),
        }

        labels = {
            'title': 'Exhibition Title',
            'cover_image': 'Cover Image',
            'video': 'Promotional Video',
            'description': 'Description',
            'start_date': 'Start Date',
            'end_date': 'End Date',
        }
        help_texts = {
            'cover_image': 'Upload an image to represent the exhibition.',
            'video': 'Optional: Upload a promotional video for the exhibition.',
        }
        error_messages = {
            'title': {
                'max_length': 'The title is too long. Please limit it to 200 characters.',
            },
            'end_date': {
                'invalid': 'Please enter a valid date for the end date.',
            },
        }
    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date and end_date and start_date > end_date:
            self.add_error('end_date', 'End date must be after start date.')
        return cleaned_data
    