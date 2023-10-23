from django.urls import path
from . import views

urlpatterns = [
    path('register-applicant/' , views.applicantRegistration , name= 'register-applicant'),
    path('register-recruiter/' , views.recruiterRegistration , name= 'register-recruiter'),
    path('login/' , views.loginUser , name = 'login'),
    path('logout/' , views.logoutUser , name='logout')

]