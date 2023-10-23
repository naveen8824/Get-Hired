from django.urls import path
from . import views

urlpatterns = [
    path('update-org-details/' , views.UpdateOrgDetails , name='update-org-details'),
    path('org-details/' , views.OrgDetails , name = 'org-details'),
    path('postAd/' , views.jobPost , name='post-job'),
    path('dashboard/' , views.viewJobAds, name='recruiter-dashboard'),
    path('dashboard/showApplicants/<int:id>/' , views.showApplicants , name = 'show-applicants')
]