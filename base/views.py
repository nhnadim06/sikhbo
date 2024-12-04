from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import *
from .forms import courseForm
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib import messages



# Home View
def views_home(request):
    categories = Category.objects.exclude(name__iexact="Foundation").exclude(name__iexact="Career Track")
    statistics = Statistic.objects.first()
    instructors = Instructor.objects.all()
    career_courses = Course.objects.filter(category__name='Career Track')
    foundation_courses = Course.objects.filter(category__name='Foundation')
    free_courses = Course.objects.filter(price=0)
    current_time = datetime.now()

    context = {
        'categories': categories,
        'career_courses': career_courses,
        'foundation_courses': foundation_courses,
        'free_courses': free_courses,
        'statistics': statistics,
        'current_time': current_time,
    }
    return render(request, 'home.html', context=context)

# Signup View
def views_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST.get('role', 'User')  # Default to User

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            # Inform the user that the username is taken
            messages.error(request, "Username is already taken.")
            return render(request, "signup.html")

        # Create user
        user = User.objects.create_user(username=username, password=password)

        # Check if UserProfile already exists for the user
        if not hasattr(user, 'userprofile'):
            # Create UserProfile only if it does not exist
            UserProfile.objects.create(user=user, role=role)

        # Redirect to login page after successful signup
        return redirect('views_login')

    return render(request, "signup.html")

# Login View
def views_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, "login.html")

# Logout View
def views_logout(request):
    logout(request)
    return redirect('home')

# Course Views
@login_required
def courses(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})

def course_details(request, id):
    course = Course.objects.get(pk=id)
    related_courses = Course.objects.filter(category=course.category).exclude(id=course.id)
    context = {'course': course, 'related_courses': related_courses}
    return render(request, 'course_details.html', context)

# Admin-only Views
@login_required
def upload_course(request):
    if request.user.profile.role != 'Admin':
        return HttpResponseForbidden("You are not authorized to perform this action.")

    form = courseForm()
    if request.method == 'POST':
        form = courseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('views_home')

    context = {'form': form}
    return render(request, 'course_form.html', context)

@login_required
def update_course(request, id):
    if request.user.profile.role != 'Admin':
        return HttpResponseForbidden("You are not authorized to perform this action.")

    course = Course.objects.get(pk=id)
    form = courseForm(instance=course)
    if request.method == 'POST':
        form = courseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            return redirect('views_home')

    context = {'form': form}
    return render(request, 'course_form.html', context)

@login_required
def delete_course(request, id):
    if request.user.profile.role != 'Admin':
        return HttpResponseForbidden("You are not authorized to perform this action.")

    course = Course.objects.get(pk=id)
    if request.method == 'POST':
        course.delete()
        return redirect('views_home')

    return render(request, 'delete_course.html')

# Other Course Categories
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
