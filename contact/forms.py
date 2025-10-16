from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "subject", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "subject": forms.TextInput(attrs={"class": "form-control"}),
            "message": forms.Textarea(
                attrs={
                    "rows": 6,
                    "class": "form-control",
                }
            ),
        }

    def clean_message(self):
        msg = self.cleaned_data.get("message", "")
        if len(msg.strip()) < 10:
            raise forms.ValidationError(
                "Message is too short — please provide more details."
            )
        return msg
