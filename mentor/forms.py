from django import forms
from .models import MentorProfile
from students.models import StudentProfile

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

class StudentSemesterUpdateForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = [
            'semester1_status',
            'semester2_status',
            'semester3_status',
            'semester4_status',
            'semester5_status',
            'semester6_status',
        ]
        widgets = {
            'semester1_status': forms.Select(attrs={'class': 'py-1 px-2 border border-gray-300 rounded-md shadow-sm text-sm'}),
            'semester2_status': forms.Select(attrs={'class': 'py-1 px-2 border border-gray-300 rounded-md shadow-sm text-sm'}),
            'semester3_status': forms.Select(attrs={'class': 'py-1 px-2 border border-gray-300 rounded-md shadow-sm text-sm'}),
            'semester4_status': forms.Select(attrs={'class': 'py-1 px-2 border border-gray-300 rounded-md shadow-sm text-sm'}),
            'semester5_status': forms.Select(attrs={'class': 'py-1 px-2 border border-gray-300 rounded-md shadow-sm text-sm'}),
            'semester6_status': forms.Select(attrs={'class': 'py-1 px-2 border border-gray-300 rounded-md shadow-sm text-sm'}),
        }