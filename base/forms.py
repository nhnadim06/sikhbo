from django.forms import ModelForm
from .models import *


class courseForm(ModelForm):
   class Meta:
       model = Course
       fields = '__all__'