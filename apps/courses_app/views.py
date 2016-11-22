from django.shortcuts import render, redirect
from . import models

# Create your views here.
def index(request):
    courses = models.Courses.objects.all().order_by('-added_at')
    context = {
        'courses' : courses
    }
    return render(request, 'courses_app\index.html', context)

def add(request):
    models.Courses.objects.create(name = request.POST['name'], description = request.POST['descript'])
    return redirect('/')

def destroy(request,id):
    course = models.Courses.objects.get(id=id)
    context = {
        'course' : course
    }
    return render(request, 'courses_app\destroy.html', context)

def process(request, id):
    models.Courses.objects.filter(id=id).delete()
    return redirect('/')

def home(request):
    return redirect('/')
