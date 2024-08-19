
from django.shortcuts import render
from . import models

# Create your views here.

def testview(request):
    categories = models.Category.objects.all()
    subcategories = models.SubCategory.objects.all()
    return render(request,'homepage/homepage.html',{"categories":categories,"subcategories":subcategories})

def user_face_view(request):
    return render(request,'components/user_face.html')

def app_view(request):
    return render(request,'components/app.html')

def login_view(request):
    return render(request,'components/login.html')

def register_view(request):
    return render(request,'components/register.html')