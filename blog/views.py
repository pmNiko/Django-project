from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Project, Task
from .forms import CreateNewtask, CreateNewProject

# Create your views here.
def index(request):
    return render(request, 'index.html')

def hello(request, username):
    # print(type(id))
    # print(username)
    return HttpResponse(f'<h2>Hello world! {username}</h2>')
    # return HttpResponse(f'<h2>Hello world! {id}</h2>')
    


def about(request):
    phrase = 'This page refers about us and our values'
    return render(request, 'about.html', {'phrase': phrase})


def projects(request):
    projects = list(Project.objects.values())
    return render(request, 'projects/list.html', {
        'projects': projects
    })


def tasks(request):
    # task = Task.objects.get(id=id)
    # task = get_object_or_404(Task,id=id)
    tasks = Task.objects.all()
    return render(request, 'tasks/list.html', {
        'tasks': list(tasks)
    })

def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {
            'form': CreateNewtask
        })
    else:
        Task.objects.create(
            title       =   request.POST['title'],
            description =   request.POST['description'],
            project_id  =   1
        )
        return redirect('tasks')


def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
            "form": CreateNewProject
        })

    else:
        Project.objects.create(
            name = request.POST["name"]
        )
        return redirect("projects")