from django.shortcuts import render
from .models import Category, Course, Statistic, Instructor
import datetime  # Fixed: Moved import to the top

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

def views_courses(request):
    return render (request,"courses.html")  
