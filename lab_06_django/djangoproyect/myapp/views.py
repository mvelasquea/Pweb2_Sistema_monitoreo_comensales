from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def ejemplo(request):
    return HttpResponse("<h1>Este es el ejemplo de las vistas con metodos</h1>")

