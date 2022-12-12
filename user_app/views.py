from django.shortcuts import render,redirect
from user_app import models

def index(request):
    return render(request,'index.html')

def create_Users(request):
    if request.method == 'POST':
       models.create_User(request)
    return redirect('/display_Users')

def display_Users(request):
    data = models.get_Users(request)
    context = {
        'data' : data
    }
    return render(request,'index.html',context)


