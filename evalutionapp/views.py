
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from . import models
from .models import ImageUpload
from django.http import JsonResponse
from django.conf import settings

def admin_only(user):
    return user.is_authenticated and (user.is_staff or user.is_superuser)

@user_passes_test(admin_only, login_url = '/login/', redirect_field_name= None)
@login_required(login_url='/login/')
def homepage(request):
    categories = models.Category.objects.all()
    subcategories = models.SubCategory.objects.all()
    if request.method == 'POST':
        app_icon = request.FILES['app_icon']
        form = request.POST
        app_name = request.POST.get('app_name')
        app_link = request.POST.get('app_link')
        category = models.Category.objects.get(pk = request.POST.get('category'))
        print(category)
        subcategory = models.SubCategory.objects.get(pk=request.POST.get('subcategory'))
        app_points = request.POST.get('points')
       
        app = models.App.objects.create(
            app_name = app_name,
            app_link = app_link,
            app_icon = app_icon,
            app_points = app_points,
            category = category,
            subcategory = subcategory

        )
        app.save()
        return redirect('homepage')
    return render(request,'homepage/homepage.html',{"categories":categories,"subcategories":subcategories})

@login_required(login_url='/login/')
def user_face_view(request,id):
    app = models.App.objects.get(pk = id)
    return render(request,'components/user_face.html',{'app':app})

@login_required(login_url='/login/')
def app_view(request):
    allApps = models.App.objects.all()
    print(allApps)
    return render(request,'components/app.html',{'apps':allApps})

@login_required(login_url='/login/')
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
                return redirect('app')
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

def upload_screenshort(request,id):
    if request.method == 'POST':
        image_file = request.FILES['image']
        print(image_file)
        app = models.App.objects.get(pk = id)
        app.app_image = image_file
        app.save()
        image_url = f'{settings.MEDIA_URL}{app.app_image.name}'
        return JsonResponse({'image': image_url})
    return JsonResponse({'error': 'Invalid request'}, status=400)
