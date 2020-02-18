from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Course
from django.template import loader
from .forms import adtaaCourseForm

def index(request):
    courseList = Course.objects.all()
    context = {
        'courseList':courseList,
    }
    return render(request, 'ADTAA/index.html', context)


def addCourse(request):
    if request.method == 'POST':
        form = adtaaCourseForm(request.POST)
        if form.is_valid():
            new_course = form.save()
            return HttpResponseRedirect('/adtaa/')

    else:
        form = adtaaCourseForm()

    return render(request, 'ADTAA/addCourse.html', {'form':form})