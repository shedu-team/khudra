from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "sells/index.html")


def mohammad(request, nick):
    return HttpResponse(f"Hi, your nick name is:  {nick.capitalize()}!")


def greet(request, name):
    return render(request, "sells/greet.html", {
        "name": name.capitalize()
    })
