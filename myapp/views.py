from django.http import HttpResponse
from .models import Task, Project

def index(request):
    return HttpResponse("<h1>Index Page </h1>")


# Create your views here.
def hello(request, id ):

    # return HttpResponse(f"<h1>Hola {username} lola</h1>")
    return HttpResponse(f"<h1>Hola {id} lola</h1>" )



def about(request):
    return HttpResponse("<h3>About</h3>")



def projects(request):

    projects = Project.objects.all();

    html = "<h1>Projects</h1><ul>"

    for project in projects:
        html += f"<li>{project.name}</li>"
    
    html += "</ul>"

    return HttpResponse(html)


def tasks(request):
    return HttpResponse("<h1>Tasks</h1>")