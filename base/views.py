from django.shortcuts import render 

# Create your views here.
def home(request):
    return render(request,template_name='base\home.html')

def login(request):
    return render(request,template_name='base\login.html')

def signup(request):
    return render(request,template_name='base\signup.html')
