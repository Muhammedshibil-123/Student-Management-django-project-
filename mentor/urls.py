from django.urls import path
from . import views

urlpatterns = [
    path('profile/',views.mentor_profile,name='mentor_profile'),
    path('',views.mentor_dashboard,name='mentor_dashboard'),
    path('request/',views.mentor_request,name='mentor_request'),
    path('students/',views.mentor_students,name='mentor_students'),
    path('course/',views.mentor_course,name='mentor_course'),
]
