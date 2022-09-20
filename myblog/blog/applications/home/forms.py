from django import forms

# models
from .models import Subscribers, Contact

class SubscribersForm(forms.ModelForm):
    """Form definition for Subscribers."""


    class Meta:
        """Meta definition for Subscribersform."""

        model = Subscribers
        fields = ('email',)
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Correo Electrónico .....',
                }
            )
        }


class ContactForm(forms.ModelForm):
    """Form definition for Contact."""

    class Meta:
        """Meta definition for Contactform."""

        model = Contact
        fields = ('__all__')
