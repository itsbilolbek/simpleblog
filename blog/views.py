from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'blog/index.html', {'title': 'Home'})


def about(request):
    return HttpResponse('You are viewing about page')
