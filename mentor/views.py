from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def mentor_profile(request):
    if not request.user.is_mentor():
        return redirect('student_profile')
    
    return render(request,'mentor/profile.html')