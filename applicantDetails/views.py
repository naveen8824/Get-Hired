from django.shortcuts import render,redirect
from .models import ApplicantDetails,JobApplications
from users.models import User
from .form import ApplicantDetailsForm
from recruiterOrg.models import Organization
from django.contrib import messages
from recruiter.models import Jobs

# Create your views here.

def updateApplicantDetails(request):
    if request.user.isApplicant:
        resume = ApplicantDetails.objects.get(user = request.user)
        if request.method == "POST":
            form = ApplicantDetailsForm(request.POST , instance=resume)
            if form.is_valid():
                userForm = form.save(commit=False)
                applicant = User.objects.get(id = request.user.id)
                applicant.first_name = request.POST['first_name']
                applicant.last_name = request.POST['last_name']
                applicant.resumeUpdatedbyApplicant = True
                userForm.save()
                applicant.save()
                messages.success(request , 'Voila! Your details are submitted successfully. Starting Applying Now!')
                return redirect('applicant-dashboard')
            else:
                messages.warning(request , 'Uh, Oh! Something went wrong!')

        else:
            form = ApplicantDetailsForm(instance=resume)
            context = {'form':form}
            return render(request , 'applicantDetails/updateDetails.html' , context)
    else:
        messages.warning(request , 'Permission Denied')
        redirect('applicant-dashboard')
        

def applicantDetails(request):
    resume = ApplicantDetails.objects.get(user_id = request.user.id)
    context= {'form':resume}
    return render(request , 'applicantDetails/viewDetails.html' , context)

def viewJobs(request):
    if request.user.isApplicant:
        allJobs = Jobs.objects.all().values()
        allJobswithCompanyName = []
        for job in allJobs:
            company = Organization.objects.get(recruiter_id = job['recruiter_id'])
            company = company.org_name
            job['company'] = company
            allJobswithCompanyName.append(job)

        hasCompleteProfile = request.user.resumeUpdatedbyApplicant
        context = {'jobs' : allJobswithCompanyName , 'showDetails':hasCompleteProfile}
        return render(request , 'dashboards/applicantDashboard.html' , context)
    
def viewJobDetails(request, pk):
    job  = Jobs.objects.get(pk=pk)
    # print(job)
    company = Organization.objects.get(recruiter_id = job.recruiter_id)
    company = company.org_name
    job.company = company
    context = {'form':job , 'userid':request.user.id}
    return render(request , 'jobs/jobDetails.html' , context)

def applyJob(request , pk):
    try:
        job = Jobs.objects.get(pk=pk)
        print(job.id)
        allPostedJobApplications = JobApplications.objects.filter(job_id = job.id).values()
        print(allPostedJobApplications)
        jobAppliedAlready = False
        for jobApplication in allPostedJobApplications:
            print(jobApplication)
            if request.user.id == jobApplication['applicant_id']:
                jobAppliedAlready = True
        if jobAppliedAlready:
            messages.warning(request , 'Job Applied Already')
            return redirect('applicant-dashboard')
        else:
            JobApplications.objects.create(job = job , applicant = request.user)
            messages.success(request, 'You have successfully applied to the job')
            return redirect('applicant-dashboard')
    except Exception as e:
        messages.warning(request , 'Something Went Wrong!')
        return redirect('applicant-dashboard')
    
def userApplications(request):
    userJobs = JobApplications.objects.filter(applicant_id = request.user.id).values()
    alljobs = []
    for job in userJobs:
        userjob = Jobs.objects.get(id = job['job_id'])
        company = Organization.objects.get(recruiter_id = userjob.recruiter_id)
        company = company.org_name
        userjob.company = company
        alljobs.append(userjob)
    context = {'form':alljobs}
    return render(request , 'applicantDetails/applications.html' , context)




    

    


    

    

        


