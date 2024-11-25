from django import forms
from .models import CallbackRequest

class CallbackRequestForm(forms.ModelForm):
    class Meta:
        model = CallbackRequest
        fields = ['full_name', 'phone_number', 'city']
        widgets = {
            'phone_number': forms.TextInput(attrs={'placeholder': '+7 (___) ___-__-__'}),
        }