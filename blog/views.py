from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import Project, Task

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
    return render(request, 'projects.html', {
        'projects': projects
    })


def tasks(request):
    # task = Task.objects.get(id=id)
    # task = get_object_or_404(Task,id=id)
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {
        'tasks': list(tasks)
    })