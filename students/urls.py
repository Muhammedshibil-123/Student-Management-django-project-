
from django.urls import path
from . import views


urlpatterns = [
    path('profile/', views.student_profile, name='student_profile'),
    path('',views.student_dashboard,name='student_dashboard'),
    path('course',views.student_course,name='student_course'),
    path('edit/',views.student_edit,name='student_edit')
]