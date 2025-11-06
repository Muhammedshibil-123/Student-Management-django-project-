from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def student_profile(request):
    if not request.user.is_student():
        return redirect('login')
    
    profile=request.user.student_profile

    context={
        'profile':profile
    }
    
    return render(request,'student/profile.html',context)

@login_required
def student_dashboard(request):
    if not request.user.is_student():
        return redirect('login')
    
    return render(request,'student/dashboard.html')

@login_required
def student_course(request):
    if not request.user.is_student():
        return redirect('login')
    
    return render(request,'student/course.html')

@login_required
def student_edit(request):
    if not request.user.is_student():
        return redirect('login')
    
    return render(request,'student/edit.html')