"""
URL configuration for eLearning project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from .import settings
from django.conf.urls.static import static



from base import views as base_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base_views.views_home,name="home"),
    path('course_details/<str:id>',base_views.course_details, name = 'course_details'),
    path('upload_course/',base_views.upload_course,name='upload_course'),
    path('update_course/<str:id>',base_views.update_course,name = 'update_course'),
    path('delete_course/<str:id>',base_views.delete_course,name = 'delete_course'),
    path('signup/', base_views.views_signup,name="signup"),
    path('login/', base_views.views_login,name="login"),
    path('logout/', base_views.views_logout, name='logout'),
    path('courses/', base_views.courses,name="courses"),
    path('enroll_course/<str:id>/', base_views.enroll_course, name='enroll_course'),
    path('career-track-courses/', base_views.career_track_courses, name='career_track_courses'),
    path('foundation-courses/', base_views.foundation_courses, name='foundation_courses'),
    path('free-courses/', base_views.free_courses, name='free_courses'),
    path('profile/', base_views.user_profile, name='user_profile'),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])