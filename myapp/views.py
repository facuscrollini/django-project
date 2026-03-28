from django.http import HttpResponse, JsonResponse
from .models import Task, Project
from django.shortcuts import render

def index(request):

    title = "Django Course!!"

    return render(request, 'index.html', {"title": title})


def about(request):

    nombre = "Facundo Scrollini"
    return render(request, "about.html", {'nombre': nombre})


def projects(request):

    projects = Project.objects.all();


    return render(request, "projects.html", {'projects': projects})


def tasks(request):

    # task = Task.objects.get(title=title)
    return render(request, "tasks.html")