from django.urls import path
from . import views

urlpatterns = [
    path('postAd/' , views.jobPost , name='post-job'),
    path('dashboard/' , views.viewJobAds, name='recruiter-dashboard')
]