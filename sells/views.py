from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "sells/index.html")


def mohammad(request):
    return HttpResponse("Hello, Mohammad!")


def greet(request, name):
    return render(request, "sells/greet.html", {
        "name": name.capitalize()
    })
