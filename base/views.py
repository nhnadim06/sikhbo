from django.shortcuts import render

# Create your views here.
def home(request):
    return render (request,"home.html")

def signup(request):
    return render (request,"signup.html")

def login(request):
    return render (request,"login.html")  

def courses(request):
    return render (request,"courses.html")  
