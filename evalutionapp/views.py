
from django.shortcuts import render
from . import models

# Create your views here.

def testview(request):
    categories = models.Category.objects.all()
    subcategories = models.SubCategory.objects.all()
    return render(request,'homepage/homepage.html',{"categories":categories,"subcategories":subcategories})