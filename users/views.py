from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
from .models import User
from .userform import UserRegistrationForm
from recruiterOrg.models import Organization
from applicantDetails.models import ApplicantDetails
from django.views.decorators.cache import cache_control

import sys
# Create your views here.

# Login an User    
def loginUser(request):
    if request.method =='POST':
        print(request.method)
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request , username = email , password = password)

        if user != None and user.is_active:
            login(request , user)
            if request.user.isApplicant:
                return redirect('applicant-dashboard')
            else:
                return redirect('recruiter-dashboard')
        else:
            messages.warning(request , 'Uh, Oh! Something went wrong!')
            print('Uh, Oh! Something went wrong')
            return redirect('login')
    else:
        return render(request , 'users/login.html')


# Applicant Registration
def applicantRegistration(request):
    if request.method =='POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userForm  = form.save(commit=False)
            userForm.isApplicant = True
            userForm.username = userForm.email
            userForm.save()
            ApplicantDetails.objects.create(user = userForm)
            messages.success(request , 'Welcome Aboard Applicant!')
            return redirect('login')
        else:
            messages.warning(request,'Uh, Oh! Something went wrong!')
            return redirect ('register-applicant')
    else:
        form = UserRegistrationForm()
        context = {'form':form}
        return render(request , 'users/registerApplicant.html' ,context)
    
#Recruiter Registration
def recruiterRegistration(request):
    if request.method =='POST':
        form = UserRegistrationForm(request.POST)
        print(form)
        if form.is_valid():
            userForm  = form.save(commit=False)
            userForm.isRecruiter = True
            userForm.username = userForm.email
            userForm.save()
            Organization.objects.create(recruiter=userForm)
            messages.success(request , 'Welcome Aboard Recruiter!')
            return redirect('login')
        else:
            messages.warning(request, 'Uh, Oh! Something went wrong!')
            return redirect ('register-recruiter')
    else:
        form = UserRegistrationForm()
        context = {'form':form}
        return render(request , 'users/registerRecruiter.html' ,context)
    

@cache_control(no_cache=True, must_revalidate=True)
def logoutUser(request):
    logout(request)
    messages.info(request,"You have been logged out!")
    return redirect('login')

