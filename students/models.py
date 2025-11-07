from django.db import models
from django.conf import settings
from mentor.models import Department,Course

# Create your models here.
class StudentProfile(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='student_profile')

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
    ]
    approval_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
   
    date_of_birth=models.DateField(null=True,blank=True)
    GENDER_CHOICES=[
        ('','Select Gender'),
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other')
    ]
    gender=models.CharField(max_length=10,choices=GENDER_CHOICES,null=True,blank=True)
    contact_number = models.CharField(max_length=15, null=True, blank=True)
    guardian_name = models.CharField(max_length=100, null=True, blank=True)
    guardian_contact_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/students/', null=True, blank=True)
    blood_group=models.CharField(max_length=10 ,null=True,blank=True)

   
    admission_no = models.CharField(max_length=20, unique=True, null=True, blank=True)
    department=models.ForeignKey(Department,on_delete=models.SET_NULL,null=True,blank=True)
    course=models.ForeignKey(Course,on_delete=models.SET_NULL,null=True,blank=True)
    YEAR_CHOICES=[
        ('', 'Select Year'),
        ('1st Year', '1st Year'),
        ('2nd Year', '2nd Year'),
        ('3rd Year', '3rd Year'),
        ('4rd Year','4rd Year')
    ]
    year=models.CharField(max_length=10,choices=YEAR_CHOICES,null=True,blank=True)
    DIVISION_CHOICES = [
        ('', 'Select Division'),
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
     ]
    division_batch = models.CharField(max_length=5, choices=DIVISION_CHOICES, null=True, blank=True)
    roll_number = models.CharField(max_length=10, null=True, blank=True)
    date_of_admission = models.DateField(null=True, blank=True)

    SEMESTER_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('finished', 'Finished'),
    ]

    semester1_status = models.CharField(max_length=10, choices=SEMESTER_STATUS_CHOICES, default='pending')
    semester2_status = models.CharField(max_length=10, choices=SEMESTER_STATUS_CHOICES, default='pending')
    semester3_status = models.CharField(max_length=10, choices=SEMESTER_STATUS_CHOICES, default='pending')
    semester4_status = models.CharField(max_length=10, choices=SEMESTER_STATUS_CHOICES, default='pending')
    semester5_status = models.CharField(max_length=10, choices=SEMESTER_STATUS_CHOICES, default='pending')
    semester6_status = models.CharField(max_length=10, choices=SEMESTER_STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Profile of {self.user.username}"