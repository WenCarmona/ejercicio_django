from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("¡Hola Mundo! Este es mi primer proyecto de Django")
