from django.db import models
from django.conf import settings

# Create your models here.
class Department(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Course(models.Model):
    name=models.CharField(max_length=100)
    Department=models.ForeignKey(Department,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name} ({self.Department.name})"

class MentorProfile(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='mentor_profile')

    department=models.ForeignKey(Department,on_delete=models.SET_NULL,null=True,blank=True)
    course=models.ForeignKey(Department,on_delete=models.SET_NULL,null=True,blank=True)
    year_semester=models.CharField(max_length=20,blank=True,null=True)
    division_batch=models.CharField(max_length=20,blank=True,null=True)
    contact_number=models.CharField(max_length=20,blank=True,null=True)
    date_of_joining=models.DateField(null=True,blank=True)
    profile_picture=models.models.ImageField( upload_to='porfile_pics/mentors/',null=True,blank=True)

    def __str__(self):
        return f"profile of {self.user.username}"