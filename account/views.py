from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.utils.translation import gettext as _
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import CustomUser


# Create your views here.
def log_in(request):
    if request.method == 'POST' and "login" in request.POST:
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, _('Logged in successfully'))
            return redirect('home:home')
        else:
            messages.error(request, _('Invalid username or password'))
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    if request.method == 'POST' and "signup" in request.POST:
        username = request.POST['name']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        email = request.POST['email']
        phone=request.POST['phone']
        
        if password != confirm_password:
            messages.error(request, _('Passwords do not match'))
            return render(request, 'login.html', {'error': 'Passwords do not match'})
        
        # validate that all data is entered
        if not all([username, password, confirm_password, email, phone]):
            messages.error(request, _('Please fill in all fields'))
            return render(request, 'login.html', {'error': 'Please fill in all fields'})
        
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, _('Email already exists'))
            return render(request, 'login.html', {'error': 'Email already exists'})
        else:
            user = CustomUser.objects.create_user(username=username, password=password, email=email,phone=phone)
            user.save()
            messages.success(request, _('Account created successfully'))
            login(request, user)
            return redirect('home:home')
    
    return render(request, 'Login.html')




def log_out(request):
    logout(request)
    return redirect('home:home')



