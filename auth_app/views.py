from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import StudentRegistrationForm,MentorRegistrationForm


# Create your views here.
def landing_page(request):
    return render(request,'landing.html')


def login_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            
            if user.is_mentor():
                return redirect('mentor_profile')
            elif user.is_student():
                return redirect('student_profile')
        else:
            messages.error(request,'invalid username or password.')
    
    return render(request,'login.html')

def student_register(request):
    if request.method=='POST':
        form=StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Student account created.You can now log in now.')
            return redirect('login')
    else:
        form=StudentRegistrationForm()
    return render(request,'register_student.html',{'form':form})

def mentor_register(request):
    if request.method=='POST':
        form=MentorRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Mentor account created.You can now log in now.')
            return redirect('login')
    else:
        form=MentorRegistrationForm()
    return render(request,'register_mentor.html',{'form':form})

def logout_view(request):
    logout(request)
    messages.success(request,'You have been log out.')
    return redirect('landing')

        




