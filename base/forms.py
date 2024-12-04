from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['role']  # Include any other fields you want to allow the user to update



# SignUpForm
class SignUpForm(UserCreationForm):
    role = forms.ChoiceField(choices=UserProfile.ROLE_CHOICES, required=True)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user_profile = UserProfile.objects.create(user=user, role=self.cleaned_data['role'])
        if commit:
            user.save()
            user_profile.save()
        return user

# LoginForm
class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']



class courseForm(ModelForm):
   class Meta:
       model = Course
       fields = '__all__'