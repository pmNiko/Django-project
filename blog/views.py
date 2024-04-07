from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from .models import Project, Task

# Create your views here.
def index(request):
    return HttpResponse('Welcome to index page')

def hello(request, username):
    # print(type(id))
    # print(username)
    return HttpResponse(f'<h2>Hello world! {username}</h2>')
    # return HttpResponse(f'<h2>Hello world! {id}</h2>')


def about(request):
    return HttpResponse('About')


def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)


def tasks(request, id):
    # task = Task.objects.get(id=id)
    task = get_object_or_404(Task,id=id)
    return HttpResponse(f'task: {task.title}')