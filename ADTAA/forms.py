from django import forms
from django.forms import ModelForm
from .models import Course


class adtaaCourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['courseNumber', 'courseTitle', 'courseDays', 'courseTime',
                  'discipline1', 'discipline2']

