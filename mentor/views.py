from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from students.forms import UserUpdateForm ,ProfileUpdateForm
from .forms import MentorProfileUpdateForm,StudentSemesterUpdateForm
from django.contrib import messages
from students.models import StudentProfile
from django.conf import settings
from auth_app.models import CustomUser
from django.core.mail import EmailMessage
from django.forms import modelformset_factory

from django.views.decorators.cache import cache_control
def never_cache(view_func):
    return cache_control(no_cache=True, must_revalidate=True, no_store=True)(view_func)

# Create your views here.
@never_cache
@login_required
def mentor_dashboard(request):
    if not request.user.is_mentor():
        return redirect('login')

    mentor_profile = request.user.mentor_profile

    total_students = CustomUser.objects.filter(user_type='student').count()
    total_mentors = CustomUser.objects.filter(user_type='mentor').count()
    
    assigned_students_count = StudentProfile.objects.filter(
        department=mentor_profile.department,
        course=mentor_profile.course,
        year=mentor_profile.year,
        division_batch=mentor_profile.division_batch,
        approval_status='approved'
    ).count()
    
    pending_requests_count = StudentProfile.objects.filter(
        department=mentor_profile.department,
        course=mentor_profile.course,
        year=mentor_profile.year,
        division_batch=mentor_profile.division_batch,
        approval_status='pending'
    ).count()
    
    
    context = {
        'mentor_profile': mentor_profile,
        'user': request.user,
        'total_students': total_students,
        'total_mentors': total_mentors,
        'assigned_students_count': assigned_students_count,
        'pending_requests_count': pending_requests_count,
    }
    
    return render(request,'mentor/dashboard.html', context)

@never_cache
@login_required
def mentor_profile(request):
    if not request.user.is_mentor():
        return redirect('login')

    profile = request.user.mentor_profile

    context = {
        'profile': profile
    }
    return render(request,'mentor/profile.html', context) 

@never_cache
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

@never_cache
@login_required
def mentor_request(request):
    if not request.user.is_mentor():
        return redirect('login')
    
    return render(request,'mentor/request.html')

@never_cache
@login_required
def mentor_students(request):
    if not request.user.is_mentor():
        return redirect('login')
    
    mentor_profile = request.user.mentor_profile
    approved_students = StudentProfile.objects.filter(
        department=mentor_profile.department,
        course=mentor_profile.course,
        year=mentor_profile.year,
        division_batch=mentor_profile.division_batch,
        approval_status='approved'
    ).order_by('user__first_name')

    context = {
        'approved_students': approved_students
    }
    return render(request,'mentor/students.html', context)

@never_cache
@login_required
def mentor_edit_student(request, profile_id):
    if not request.user.is_mentor():
        return redirect('login')
    
    student_profile = get_object_or_404(StudentProfile, id=profile_id)
    student_user = student_profile.user

    mentor_profile = request.user.mentor_profile
    if not (student_profile.department == mentor_profile.department and
            student_profile.course == mentor_profile.course and
            student_profile.year == mentor_profile.year and
            student_profile.division_batch == mentor_profile.division_batch):
        messages.error(request, "You are not authorized to edit this student.")
        return redirect('mentor_students')

    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=student_user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=student_profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Profile for {student_user.username} updated successfully.")
            return redirect('mentor_students') 
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        u_form = UserUpdateForm(instance=student_user)
        p_form = ProfileUpdateForm(instance=student_profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'student_profile': student_profile
    }
    return render(request, 'mentor/edit_student.html', context)
    
@never_cache
@login_required
def mentor_course(request):
    if not request.user.is_mentor():
        return redirect('login')

    mentor_profile = request.user.mentor_profile

    StudentSemesterFormSet = modelformset_factory(
        StudentProfile,
        form=StudentSemesterUpdateForm,
        extra=0 
    )

    students_queryset = StudentProfile.objects.filter(
        department=mentor_profile.department,
        course=mentor_profile.course,
        year=mentor_profile.year,
        division_batch=mentor_profile.division_batch,
        approval_status='approved'
    ).order_by('user__first_name')

    if request.method == 'POST':
        formset = StudentSemesterFormSet(request.POST, queryset=students_queryset)
        
        if formset.is_valid():
            formset.save()  
            messages.success(request, 'Student semester statuses updated successfully!')
            return redirect('mentor_course')    

    else:
        formset = StudentSemesterFormSet(queryset=students_queryset)

    context = {
        'formset': formset,
        'profile': mentor_profile
    }
    return render(request,'mentor/course.html', context)

@never_cache
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

@never_cache
@login_required
def approve_student(request, profile_id):
    if not request.user.is_mentor():
        return redirect('login')
        
    student_profile = get_object_or_404(StudentProfile, id=profile_id)
    student_profile.approval_status = 'approved'
    student_profile.save()

    mentor = request.user
    student = student_profile.user
        
    subject = 'Your Account Has Been Approved!'
    message = f'Hi {student.first_name},\n\n' \
              f'Congratulations! Your account has been approved by your mentor, {mentor.first_name} {mentor.last_name}.\n\n' \
              f'You’re now officially enrolled in your courses, and you can access them by logging into your SLMS account. Take a moment to explore your dashboard, view your course materials, and get started with your learning journey.\n\n' \
              f'If you have any questions, you can reply directly to this email.\n\n' \
              f'Regards,\n{mentor.first_name} {mentor.last_name}'
    email_from = settings.EMAIL_HOST_USER
        
    recipient_list = [student.email]
       
    headers = {'Reply-To': mentor.email}
       
    email = EmailMessage(
            subject,
            message,
            email_from,
            recipient_list,
            headers=headers
     )
    email.send()
        

    return redirect('mentor_request')

@never_cache
@login_required
def decline_student(request, profile_id):
    if not request.user.is_mentor():
        return redirect('login')
        
    student_profile = get_object_or_404(StudentProfile, id=profile_id)
    user_to_delete = student_profile.user
    user_to_delete.delete()
    
    messages.error(request, f"Student '{user_to_delete.username}' has been declined and deleted.")
    return redirect('mentor_request')

@never_cache
@login_required
def mentor_delete_student(request, profile_id):
    if not request.user.is_mentor():
        return redirect('login')

    student_profile = get_object_or_404(StudentProfile, id=profile_id)
    mentor_profile = request.user.mentor_profile
    if not (student_profile.department == mentor_profile.department and
            student_profile.course == mentor_profile.course and
            student_profile.year == mentor_profile.year and
            student_profile.division_batch == mentor_profile.division_batch):
        messages.error(request, "You are not authorized to delete this student.")
        return redirect('mentor_students')
    
    username = student_profile.user.username
    
    student_profile.user.delete()

    messages.success(request, f"Student '{username}' has been successfully deleted.")
    return redirect('mentor_students')