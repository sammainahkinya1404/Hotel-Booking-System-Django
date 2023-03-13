from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.conf import settings
# from http.client import HTTPResponse
import os
import string
from urllib import response

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User
from Hotel.models import Customers

# Create your views here.
def home(request):
    return render(request, 'Index.html')

def Login(request):
      if request.method == 'POST':
        uName = request.POST['uName']
        pass1 = request.POST['pass1']

        user = auth.authenticate(username=uName, password=pass1)
        if user is not None:
            auth.login(request, user)
            print('login success')
            return redirect('Profile')
        else:
            print('Invalid login details')
            return redirect('Login')
      return render(request, 'Login.html')
            
def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        email= request.POST['email']
        uName = request.POST['uName']
        pass1= request.POST['pass1']
        pass2= request.POST['pass2']
# check IF USER Already Exists
        if User.objects.filter(username=uName).exists():
            print("Username Exists already ")
            return redirect('Register.html')
        if Customers.objects.filter(email=email).exists():
            print("Username already exists")
            return redirect('Register.html')
           
        else:
            user =User.objects.create_user(username=uName, password=pass1)
            user.save()
            user1 =Customers(user=user, fname=fname, email=email)
            user1.save()
            print('user created')
            return redirect('Login.html')
        

    return render(request, 'Register.html')
def Profile(request):
    content=Customers.objects.all()
    return render(request, 'Profile.html')