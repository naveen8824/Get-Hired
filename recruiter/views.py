from django.shortcuts import render,redirect
from .models import Jobs
from django.contrib import messages
from .form import JobPostForm


# Create your views here.

def jobPost(request):
    if request.user.isRecruiter:
        if request.method == 'POST':
            jobPost = JobPostForm(request.POST)
            if jobPost.is_valid():
                form = Jobs.objects.create(
                    recruiter=request.user , 
                    jobTitle = jobPost["jobTitle"].value(),
                    jobDesc = jobPost["jobDesc"].value(),
                    jobLocation =  jobPost["jobLocation"].value()
                )
                # print(jobPost)
                # jobPost.save()
                messages.success(request , 'Job has been posted successfully!')
                return redirect('dashboard')
            else:
                messages.warning(request , 'Something Went Wrong!')
        
        else:
            form = JobPostForm()
            context = {'form':form}
            return render(request , 'jobs/jobForm.html' , context)
    else:
        messages.warning(request , 'Permission Denied!')
        redirect('applicant-dashboard')

def viewJobAds(request):
    if request.user.isRecruiter:
        return render(request , 'dashboards/recruiterDashboard.html')
    else:
        messages.warning(request , 'Permission Denied!')
        redirect('applicant-dashboard')
    
