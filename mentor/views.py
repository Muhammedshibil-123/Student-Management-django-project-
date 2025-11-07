from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from students.forms import UserUpdateForm 
from .forms import MentorProfileUpdateForm
from django.contrib import messages
from students.models import StudentProfile


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

    profile = request.user.mentor_profile

    context = {
        'profile': profile
    }
    return render(request,'mentor/profile.html', context) 

@login_required
def mentor_edit(request):
    if not request.user.is_mentor():
        return redirect('login')
    
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = MentorProfileUpdateForm(request.POST, request.FILES,instance=request.user.mentor_profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('mentor_profile') 

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = MentorProfileUpdateForm(instance=request.user.mentor_profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    
    return render(request, 'mentor/edit.html', context)

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

@login_required
def mentor_request(request):
    if not request.user.is_mentor():
        return redirect('login')
    
    mentor_profile = request.user.mentor_profile

    pending_students = StudentProfile.objects.filter(
        department=mentor_profile.department,
        course=mentor_profile.course,
        year=mentor_profile.year,
        division_batch=mentor_profile.division_batch,
        approval_status='pending' 
    )
    
    context = {
        'pending_students': pending_students
    }
    return render(request,'mentor/request.html', context)

@login_required
def approve_student(request, profile_id):
    if not request.user.is_mentor():
        return redirect('login')
        
    student_profile = get_object_or_404(StudentProfile, id=profile_id)
    student_profile.approval_status = 'approved'
    student_profile.save()
    
    messages.success(request, f"Student '{student_profile.user.username}' has been approved.")
    return redirect('mentor_request')

@login_required
def decline_student(request, profile_id):
    if not request.user.is_mentor():
        return redirect('login')
        
    student_profile = get_object_or_404(StudentProfile, id=profile_id)
    user_to_delete = student_profile.user
    user_to_delete.delete()
    
    messages.error(request, f"Student '{user_to_delete.username}' has been declined and deleted.")
    return redirect('mentor_request')