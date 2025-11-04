from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms
from mentor.models import Department,Course,MentorProfile

class StudentRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=CustomUser
        fields=('username','first_name','last_name','email')
    
    def save(self,commit=True):
            user=super().save(commit=False)
            user.user_type='student'
            if commit:
                user.save()
            return user
        

class MentorRegistrationForm(UserCreationForm):

    department=forms.ModelChoiceField(queryset=Department.objects.all(),required=True ,empty_label="Select Department")
    course=forms.ModelChoiceField(queryset=Course.objects.all(),required=True,empty_label="Select Course")
    year_of_semester=forms.CharField(max_length=20,required=False)
    division_batch=forms.CharField(max_length=20,required=False)
    contact_number=forms.CharField(max_length=12,required=False)
    date_of_joining=forms.ImageField(required=False)


    class Meta(UserCreationForm.Meta):
        model=CustomUser
        fields=('username','first_name','last_name','email')

    def save(self,commit=True):
            user=super().save(commit=False)
            user.user_type='mentor'

            if commit:
                user.save()

            profile_data = {
            'department': self.cleaned_data.get('department'),
            'course': self.cleaned_data.get('course'),
            'year_semester': self.cleaned_data.get('year_semester'),
            'division_batch': self.cleaned_data.get('division_batch'),
            'contact_number': self.cleaned_data.get('contact_number'),
            'date_of_joining': self.cleaned_data.get('date_of_joining'),
            'profile_picture': self.cleaned_data.get('profile_picture'),
            }
        
            if commit:
                MentorProfile.objects.create(user=user, **profile_data)

            return user
    
