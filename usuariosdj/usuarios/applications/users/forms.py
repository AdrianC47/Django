from django import forms
from .models import User


class UserRegisterForm(forms.ModelForm):

    class Meta:
        """Meta definition for UserRegisterform."""

        model = User
        fields = ('__all__')# si quiero que muestre todos los atributos
