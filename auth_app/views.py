from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import StudentRegistrationForm,MentorRegistrationForm

from django.views.decorators.cache import cache_control
def never_cache(view_func):
    return cache_control(no_cache=True, must_revalidate=True, no_store=True)(view_func)

# Create your views here.
@never_cache
def register_page(request):
    
    if request.user.is_authenticated:
        if request.user.is_mentor():
            return redirect('mentor_dashboard')
        elif request.user.is_student():
            return redirect('student_profile')

    return render(request,'auth_pages/register.html')

@never_cache
def login_view(request):

    if request.user.is_authenticated:
        if request.user.is_mentor():
            return redirect('mentor_dashboard')
        elif request.user.is_student():
            return redirect('student_profile')

    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            
            if user.is_mentor():
                return redirect('mentor_dashboard')
            elif user.is_student():
                return redirect('student_profile')
        else:
            messages.error(request,'invalid username or password.')
    
    return render(request,'auth_pages/login.html')

@never_cache
def student_register(request):

    if request.user.is_authenticated:
        if request.user.is_mentor():
            return redirect('mentor_dashboard')
        elif request.user.is_student():
            return redirect('student_profile')

    if request.method=='POST':
        form=StudentRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Student account created.You can now log in now.')
            return redirect('login')
    else:
        form=StudentRegistrationForm()
    return render(request,'auth_pages/register_student.html',{'form':form})

@never_cache
def mentor_register(request):

    if request.user.is_authenticated:
        if request.user.is_mentor():
            return redirect('mentor_dashboard')
        elif request.user.is_student():
            return redirect('student_profile')


    if request.method=='POST':
        form=MentorRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Mentor account created.You can now log in now.')
            return redirect('login')
    else:
        form=MentorRegistrationForm()
    return render(request,'auth_pages/register_mentor.html',{'form':form})

@never_cache
def logout_view(request):
    logout(request)
    messages.success(request,'You have been log out.')
    return redirect('login')

        




