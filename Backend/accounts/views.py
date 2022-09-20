from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import CreateUserForm
from django.contrib import messages
# Create your views here.

# this view signs up a new writer to the database and sends a success message
def _sign_up(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                # This gets sent to the admin login page, debug later
                # messages.success(request, "Account was created successfully for " + username)
            
                return redirect('login')
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)


def _log_in(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, "Username or Password is incorrect")
    
    context ={}

    return render(request, 'accounts/login.html', context)


def _log_out(request):
    logout(request)
    return redirect('login')

