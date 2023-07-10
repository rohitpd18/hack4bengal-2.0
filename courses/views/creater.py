from django.shortcuts import render , redirect, HttpResponse
from django.contrib.auth.models import User

def creater(request):
    user= User.objects.get(username=request.user)
    return render(request, 'creater/dashboard.html', {'user':user})