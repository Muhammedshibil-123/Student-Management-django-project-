from django.urls import path
from . import views

urlpatterns = [
    path('profile/',views.mentor_profile,name='mentor_profile'),
    path('',views.mentor_dashboard,name='mentor_dashboard'),
    path('request/',views.mentor_request,name='mentor_request'),
    path('students/',views.mentor_students,name='mentor_students'),
    path('course/',views.mentor_course,name='mentor_course'),
    path('edit/',views.mentor_edit,name='mentor_edit'),
    path('approve/<int:profile_id>/', views.approve_student, name='approve_student'),
    path('decline/<int:profile_id>/', views.decline_student, name='decline_student'),
    path('student/edit/<int:profile_id>',views.mentor_edit_student,name='mentor_edit_student'),
    path('student/delete/<int:profile_id>/', views.mentor_delete_student, name='mentor_delete_student'),
]
