from django.urls import path
from . import views

urlpatterns = [
    path('profile/',views.mentor_profile,name='mentor_profile'),
]
