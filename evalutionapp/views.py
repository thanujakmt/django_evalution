
from django.shortcuts import render

# Create your views here.

def testview(request):
    return render(request,'homepage/homepage.html')