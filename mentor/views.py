from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def mentor_dashboard(request):
    if not request.user.is_mentor():
        return redirect('login')
    
    return render(request,'mentor/dashboard.html')

@login_required
def mentor_profile(request):
    if not request.user.is_mentor():
        return redirect('login')
    
    return render(request,'mentor/profile.html')

@login_required
def mentor_edit(request):
    if not request.user.is_mentor():
        return redirect('login')
    
    return render(request,'mentor/edit.html')

@login_required
def mentor_request(request):
    if not request.user.is_mentor():
        return redirect('login')
    
    return render(request,'mentor/request.html')

@login_required
def mentor_students(request):
    if not request.user.is_mentor():
        return redirect('login')
    
    return render(request,'mentor/students.html')

@login_required
def mentor_course(request):
    if not request.user.is_mentor():
        return redirect('login')
    
    return render(request,'mentor/course.html')