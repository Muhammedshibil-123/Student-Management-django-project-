from django import forms
from .models import MentorProfile

class MentorProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = MentorProfile
        fields = [
            'profile_picture', 
            'contact_number', 
            'date_of_joining'
        ]
        widgets = {
            'date_of_joining': forms.DateInput(attrs={'type': 'date'}),
        }