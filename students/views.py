from django.shortcuts import render

# Create your views here.
def student_d(request):
    return render(request,'student/profile.html')
