from django.urls import path
from . import views

urlpatterns = [
    path('',views.landing_page,name='landing'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('regiter/student/',views.student_register,name='student_register'),
    path('register/mentor/',views.mentor_register,name='mentor_register')
]
