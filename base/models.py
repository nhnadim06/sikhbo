from django.db import models
from django.contrib.auth.models import User 

# Extend User model to include role
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('User', 'User'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='User')

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(blank=True, null=True)
    icon = models.ImageField(upload_to='category_icons/', blank=True, null=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    thumbnail = models.ImageField(upload_to='course_thumbnails/', null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    students_enrolled = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='', blank=True, null=True)

    def __str__(self):
        return self.title

class Statistic(models.Model):
    total_enrollment = models.PositiveIntegerField(default=0)
    total_students = models.PositiveIntegerField(default=0)
    total_videos = models.PositiveIntegerField(default=0)
    total_courses = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "Platform Statistics"

class Instructor(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='instructor_profiles/')
    social_links = models.JSONField(default=dict, blank=True)  # Example: {"linkedin": "url", "twitter": "url"}

    def __str__(self):
        return self.name
