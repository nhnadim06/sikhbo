from django.shortcuts import render, redirect
from .models import *
import datetime  # Fixed: Moved import to the top
from .forms import courseForm


def views_home(request):
    # Fetch data from the models
    categories = Category.objects.all()
    categories = Category.objects.exclude(name__iexact="Foundation").exclude(name__iexact="Career Track")
    
    statistics = Statistic.objects.first()  # Safely fetch the first statistics record
    instructors = Instructor.objects.all()

    # Fetch categories safely
    career_courses = Course.objects.filter(category__name='Career Track')  # Filter Career Track courses
    foundation_courses = Course.objects.filter(category__name='Foundation')  # Filter Foundation courses
    free_courses = Course.objects.filter(price=0)  # Filter Free courses (assuming price = 0 means free)

    # Get the current year
    current_year = datetime.datetime.now().year

    context = {
        'categories': categories,
        'career_courses': career_courses,
        'foundation_courses': foundation_courses,
        'free_courses': free_courses,
        'statistics': statistics,
        'current_year': current_year,  # Updated key to match template
    }

    return render(request, 'home.html', context=context)


def views_signup(request):
    return render (request,"signup.html")

def views_login(request):
    return render (request,"login.html")  

def courses(request):
    courses = Course.objects.all()
    return render (request,'courses.html',{'courses': courses})  

def course_details(request, id):
    course = Course.objects.get(pk=id)
    
    # Fetch related courses based on the category (example)
    related_courses = Course.objects.filter(category=course.category).exclude(id=course.id)

    context = {
        'course': course,
        'related_courses': related_courses,
    }

    return render(request, 'course_details.html', context)


def upload_course(request):
   form = courseForm()
   if request.method == 'POST':
       form = courseForm(request.POST, request.FILES)
       if form.is_valid():
           form.save()
           return redirect('home')
   context = {'form':form}
   return render(request, template_name = 'course_form.html', context= context)


def update_course(request,id):
   course = Course.objects.get(pk = id)
   form = courseForm(instance = course)
   if request.method == 'POST':
       form = courseForm(request.POST, request.FILES,instance = course)
       if form.is_valid():
           form.save()
           return redirect('home')
   context = {'form':form}
   return render(request, template_name = 'course_form.html', context= context)

def delete_course(request,id):
   course = Course.objects.get(pk=id)
   if request.method == 'POST':
       course.delete()
       return redirect('home')
   return render(request, template_name = 'delete_course.html')




def career_track_courses(request):
    career_track_category = Category.objects.get(name='Career Track')
    career_courses = Course.objects.filter(category=career_track_category) 
    return render(request, 'career_track_courses.html', {'career_courses': career_courses})

def foundation_courses(request):
    foundation_category = Category.objects.get(name='Foundation')

    foundation_courses = Course.objects.filter(category=foundation_category) 
    return render(request, 'foundation_courses.html', {'foundation_courses': foundation_courses})

def free_courses(request):
    free_courses = Course.objects.filter(price=0)  
    return render(request, 'free_courses.html', {'free_courses': free_courses})







