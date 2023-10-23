from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Organization
from users.models import User
from .form import OrganizationDetails
from recruiter.models import Jobs
from django.contrib import messages
from recruiter.form import JobPostForm
from applicantDetails.models import JobApplications

# Create your views here.

#update org details

def UpdateOrgDetails(request):
    print (request.user)
    userOrg = Organization.objects.get(recruiter=request.user)
    if request.method == "POST":
        form = OrganizationDetails(request.POST , instance=userOrg)
        if form.is_valid():
            userForm = form.save(commit=False)
            user = User.objects.get(username = request.user)
            user.orgUpdatedbyRecruiter = True
            userForm.save()
            user.save()
            messages.success(request , 'Voila! Your organization is now active on Get Hired!')
            return redirect('recruiter-dashboard')
        else:
            messages.warning(request , 'Uh, Oh! Something went wrong!')
        
    else:
        form = OrganizationDetails(instance=userOrg)
        context = {'form':form}
        return render(request , 'recruiterOrg/updateOrgDetails.html' , context) 


#view org details

def OrgDetails(request):
    org = Organization.objects.get(recruiter_id = request.user.id)
    print(org)
    context = {'form':org}
    return render(request , 'recruiterOrg/viewDetails.html' , context)

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
                return redirect('recruiter-dashboard')
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
        allJobs = Jobs.objects.filter(recruiter_id = request.user.id).values()
        print(allJobs)
        jobsPosted = False
        allJobsWithCount = []
        if allJobs is not None:
            jobsPosted = True
            for job in allJobs:
                totalApplicants = JobApplications.objects.filter(job_id = job['id']).values()
                totalApplicants = totalApplicants.count()
                job['totalApplicants'] = totalApplicants
                allJobsWithCount.append(job)
        print(allJobsWithCount)
        context = {'alljobs':allJobsWithCount , 'jobsPosted':jobsPosted}
        return render(request , 'dashboards/recruiterDashboard.html' , context)
    else:
        messages.warning(request , 'Permission Denied!')
        redirect('applicant-dashboard') 

def showApplicants(request , id):
    allApplications = JobApplications.objects.filter(job_id = id).values()
    allApplicants = []
    for app in allApplications:
        applicant = User.objects.get(id = app['applicant_id'])
        allApplicants.append(applicant)
    
    print(allApplicants)

    context = {'applicants':allApplicants}
    return render(request , 'recruiterOrg/showApplicants.html' , context)



