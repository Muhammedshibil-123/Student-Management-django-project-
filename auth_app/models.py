from django.db import models 
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    USER_TYPE_CHOICES=(
        ('student','Student'),
        ('mentor','Mentor'),
    )
    user_type=models.CharField( max_length=11,choices=USER_TYPE_CHOICES)

    def is_studnet(self):
        return self.user_type == 'student'
    
    def is_mentor(self):
        return self.user_type == 'mentor'