from django.shortcuts import render, redirect

def home(request):
    if request.method =='GET':
        return render(request , 'home/home.html')
