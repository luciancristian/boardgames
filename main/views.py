from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "main/home.html", {'message': 'Hi, there!'})
# Create your views here.
