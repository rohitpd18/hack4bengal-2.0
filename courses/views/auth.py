from django.shortcuts import render , redirect, HttpResponse
from django.contrib.auth import logout , login, authenticate
from courses.forms import RegistrationForm , LoginForm
from django.views.decorators.http import require_http_methods
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.models import Group

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
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        print(user)
        if user is not None:
            print("hi")
            login(request, user)
            login_success = 'Sign in successful! Welcome to ThreadAcademy'
            context = {
                'login_success': login_success
            }
            return redirect("home")
        else:

            error_message = 'Invalid credentials. Please try again.'
            context = {
                'error_message': error_message
            }
            print(context)

            return render(request, 'courses/login.html', context)
        
    show_signin_message = 'Please sign in to continue'
    context = {
        'show_signin_message': show_signin_message
    }
    return render(request, 'courses/login.html',context)


def signout(request ):
    logout(request)
    return redirect("home")

# user profile
def profile(request):
    user= request.user
    if user.is_authenticated is False:
        return redirect('login')
    is_creater= check_user_group(user, 'creater')
    return render(request, 'courses/profile.html',{is_creater:is_creater})

    

# funtion for setting a user as a creater
def add_user_to_group(user, group_name):
    try:
        group = Group.objects.get(name=group_name)
        group.user_set.add(user)
        print(f"User {user.username} added to group {group_name} successfully.")
    except Group.DoesNotExist:
        print(f"Group {group_name} does not exist.")


# checking user is creatar or not
def check_user_group(user, group_name):
    try:
        group = Group.objects.get(name=group_name)
        if group in user.groups.all():
            print(f"User {user.username} belongs to group {group_name}.")
            return True
        else:
            print(f"User {user.username} does not belong to group {group_name}.")
            return False

    except Group.DoesNotExist:
        print(f"Group {group_name} does not exist.")

def become_creater(request):
    group_name= "creater"
    user= request.user
    if user is "AnonymousUser":
        return redirect('/login')    
    add_user_to_group(user, group_name)
    return HttpResponse("creater's dashboard")
