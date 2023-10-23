from django.urls import path
from . import views

urlpatterns= [
    path('update-details/' , views.updateApplicantDetails , name='update-details' ),
    path('details/' , views.applicantDetails , name = 'applicant-details'),
    path('dashboard' , views.viewJobs , name='applicant-dashboard'),
    path('jobDetails/<int:pk>/' , views.viewJobDetails , name='view-job'),
    path('jobDetails/<int:pk>/apply/' , views.applyJob , name='apply-job'),
    path('myApplications' , views.userApplications , name='user-applications'),
    path('download/' , views.download_file , name='download')
]