from django import forms
from auth_app.models import CustomUser
from .models import StudentProfile

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=CustomUser
        fields=['first_name','last_name','email']
    

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=StudentProfile
        fields=[
            'profile_picture', 
            'contact_number', 
            'date_of_birth', 
            'gender', 
            'blood_group', 
            'address', 
            'guardian_name', 
            'guardian_contact_number'
        ]
        widgets={
            'date_of_birth':forms.DateInput(attrs={'type':'date'}),
          'address':forms.Textarea(attrs={'rows':3})
        }