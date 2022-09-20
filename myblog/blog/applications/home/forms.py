from django import forms

# models
from .models import Subscribers

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
