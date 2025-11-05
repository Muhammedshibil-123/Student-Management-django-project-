from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms
from mentor.models import Department,Course,MentorProfile
from students.models import StudentProfile

class StudentRegistrationForm(UserCreationForm):
    
    #personal
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    gender = forms.ChoiceField(choices=StudentProfile.GENDER_CHOICES, required=False)
    contact_number = forms.CharField(max_length=15, required=False)
    guardian_name = forms.CharField(max_length=100, required=False)
    guardian_contact_number = forms.CharField(max_length=15, required=False)
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=False)
    profile_picture = forms.ImageField(required=False)
    blood_group = forms.CharField(max_length=10,required=False)

    # Academic 
    admission_no = forms.CharField(max_length=20, required=True)
    department = forms.ModelChoiceField(queryset=Department.objects.all(), empty_label="Select Department", required=False)
    course = forms.ModelChoiceField(queryset=Course.objects.all(), empty_label="Select Course", required=False)
    year = forms.ChoiceField(choices=StudentProfile.YEAR_CHOICES, required=False)
    division_batch = forms.ChoiceField(choices=StudentProfile.DIVISION_CHOICES, required=False)
    roll_number = forms.CharField(max_length=10, required=False)
    date_of_admission = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)   

    class Meta(UserCreationForm.Meta):
        model=CustomUser
        fields=('username','first_name','last_name','email')
    
    def save(self,commit=True):
            user=super().save(commit=False)
            user.user_type='student'
            if commit:
                user.save()
            
            profile_data = {
            'date_of_birth': self.cleaned_data.get('date_of_birth'),
            'gender': self.cleaned_data.get('gender'),
            'contact_number': self.cleaned_data.get('contact_number'),
            'guardian_name': self.cleaned_data.get('guardian_name'),
            'guardian_contact_number': self.cleaned_data.get('guardian_contact_number'),
            'address': self.cleaned_data.get('address'),
            'profile_picture': self.cleaned_data.get('profile_picture'),
            'blood_group': self.cleaned_data.get('blood_group'),
            
            'admission_no': self.cleaned_data.get('admission_no'),
            'department': self.cleaned_data.get('department'),
            'course': self.cleaned_data.get('course'),
            'year': self.cleaned_data.get('year'),
            'division_batch': self.cleaned_data.get('division_batch'),
            'roll_number': self.cleaned_data.get('roll_number'),
            'date_of_admission': self.cleaned_data.get('date_of_admission'),
            }

            if commit:
                 StudentProfile.objects.create(user=user,**profile_data)
            return user
        

class MentorRegistrationForm(UserCreationForm):
     
    MENTOR_CODE='123456'

    department=forms.ModelChoiceField(queryset=Department.objects.all(),required=True ,empty_label="Select Department")
    course=forms.ModelChoiceField(queryset=Course.objects.all(),required=True,empty_label="Select Course")
    year = forms.ChoiceField(
        choices=[('', 'Select Year')] + MentorProfile.YEAR_CHOICES, 
        required=False
    )
    division_batch=forms.ChoiceField(
         choices=[('','Select Division')]+MentorProfile.DIVISIONS,
         required=False
    )
    mentor_code=forms.CharField(max_length=10,required=True,help_text="Enter the official mentor code.")
    contact_number=forms.CharField(max_length=20,required=False)
    date_of_joining=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}),required=False)
    profile_picture=forms.ImageField(required=False)



    class Meta(UserCreationForm.Meta):
        model=CustomUser
        fields=('username','first_name','last_name','email')

    def clean_mentor_code(self):
         code=self.cleaned_data.get('mentor_code')

         if code != self.MENTOR_CODE:
              raise forms.ValidationError('Invalid Mentor Code.')
         return code
         

    def save(self,commit=True):
            user=super().save(commit=False)
            user.user_type='mentor'

            if commit:
                user.save()

            profile_data = {
            'department': self.cleaned_data.get('department'),
            'course': self.cleaned_data.get('course'),
            'year': self.cleaned_data.get('year'),
            'division_batch': self.cleaned_data.get('division_batch'),
            'mentor_code':self.cleaned_data.get('mentor_code'),
            'contact_number': self.cleaned_data.get('contact_number'),
            'date_of_joining': self.cleaned_data.get('date_of_joining'),
            'profile_picture': self.cleaned_data.get('profile_picture'),
            }
        
            if commit:
                MentorProfile.objects.create(user=user, **profile_data)

            return user
    
