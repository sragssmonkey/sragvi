from django.shortcuts import render

def home(request):
    return render(request,'resume/home.html')
# Create your views here.
from django.shortcuts import render
from .models import Project

def home(request):
    projects = Project.objects.all()  # no ordering by created_at
    return render(request, 'resume/home.html', {'projects': projects})
