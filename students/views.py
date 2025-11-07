from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserUpdateForm ,ProfileUpdateForm

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
    
    profile=request.user.student_profile

    context={
        'changes_profile':profile
    }
    
    return render(request,'student/course.html',context)

@login_required
def student_edit(request):
    if not request.user.is_student():
        return redirect('login')
    
    if request.method=="POST":
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.student_profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('student_profile') 
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.student_profile)

    context={
        'u_form':u_form,
        'p_form':p_form
    }

    return render(request,'student/edit.html',context)