from django.http import HttpResponse, JsonResponse
from .models import Task, Project
from django.shortcuts import render, redirect
from .forms import CreateNewTask, CreateNewTaskForm


def index(request):

    title = "Django Course!!"

    return render(request, 'index.html', {"title": title})


def about(request):

    nombre = "Facundo Scrollini"
    return render(request, "about.html", {'nombre': nombre})


def projects(request):

    projects = Project.objects.all();


    return render(request, "projects/projects.html", {'projects': projects})


def tasks(request):

    tasks = Task.objects.all()
    return render(request, "tasks/tasks.html" , {"tasks" : tasks})



def create_task(request):
    
    if request.method == 'GET':

        return render(request, 'tasks/create_task.html',{
            "form": CreateNewTask
        })
    
    title = request.POST["title"]
    description = request.POST["description"]
    
    Task.objects.create(title=title, description=description, project_id=1)

    return redirect('tasks')



def create_project(request):
    
    if request.method == "GET":
        return render(request,'projects/create_project.html',{
            'form': CreateNewTaskForm
        })
    
    name = request.POST["name"]
    Project.objects.create(name=name)
    return redirect('projects')


