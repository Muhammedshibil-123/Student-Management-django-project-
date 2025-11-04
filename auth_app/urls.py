from django.urls import path
from . import views

urlpatterns = [
    path('',views.register_page,name='register'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('register/student/',views.student_register,name='student_register'),
    path('register/mentor/',views.mentor_register,name='mentor_register')
]
