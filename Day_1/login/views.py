from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def home(request):
    return render(request, 'login/base.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
