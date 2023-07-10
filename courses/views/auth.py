from django.shortcuts import render , redirect
from django.contrib.auth import logout , login, authenticate
from courses.forms import RegistrationForm , LoginForm
from django.views.decorators.http import require_http_methods
from django.views import View
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import messages
from urllib.parse import urlencode
from django.http import HttpResponseRedirect

def signup(request):
    # print(request.POST)
    if request.method == 'POST':
        user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
        user.first_name = request.POST['fname']
        user.last_name = request.POST['lname']
        user.email = request.POST['email']
        user.save()
        return redirect('login')
    return render(request, 'courses/signup.html')
    
def login_view(request):
    message=[]
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        print(user)
        if user:
            login(request, user)
            login_success = 'Sign in successful! Welcome to ThreadAcademy'
            context = {
                'login_success': login_success
            }
            message.append(messages.success(request, 'Login successful!'))
            # messages.success(request, 'Login successful!')
            return redirect('home')

        else:
            message=[]
            error_message = 'Invalid credentials. Please try again.'
            context = {
                'error_message': error_message
            }

            return render(request, 'courses/login.html', context)
        
    show_signin_message = 'Please sign in to continue'
    context = {
        'show_signin_message': show_signin_message
    }
    return render(request, 'courses/login.html',context)


def signout(request ):
    logout(request)
    messages= None
    return redirect("home")

def become_creater(request):
    pass

