from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("neworder", views.neworder, name="neworder"),
    path("<str:name>", views.greet, name="greet"),
    path("nick/<str:nick>", views.mohammad, name="moh"),

]

