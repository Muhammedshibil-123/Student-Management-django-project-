from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

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
    class Meta(UserCreationForm.Meta):
        model=CustomUser
        fields=('username','first_name','last_name','email')

        def save(self,commit=True):
            user=super().save(commit=False)
            user.user_type='mentor'

            if commit:
                user.save()
            return user