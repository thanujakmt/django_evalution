
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from . import models

def admin_only(user):
    return user.is_authenticated and (user.is_staff or user.is_superuser)



@user_passes_test(admin_only, login_url = '/login/', redirect_field_name= None)
@login_required(login_url='/login/')
def homepage(request):
    categories = models.Category.objects.all()
    subcategories = models.SubCategory.objects.all()
    return render(request,'homepage/homepage.html',{"categories":categories,"subcategories":subcategories})

@login_required(login_url='/login/')
def user_face_view(request):
    return render(request,'components/user_face.html')

@login_required(login_url='/login/')
def app_view(request):
    return render(request,'components/app.html')

def logout_view(request):
    
    if request.method == 'POST':
        logout(request)
        return redirect('login')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request,username = username, password = password)

        if user is not None:
            login(request,user)
            if not user.is_staff:
                return redirect('userface')
            else:
                return redirect('homepage')

    return render(request,'components/login.html')

def register_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            return redirect('register')
        
        user = User.objects.create(username = username, email= email)
        user.set_password(password)
        user.save()
        print(user)
        return redirect('login')

    return render(request,'components/register.html')

def upload_screenshort(request):
    if request.method == 'POST':
        file = request.Files[0]
        
    return render(request,'components/register.html') 
