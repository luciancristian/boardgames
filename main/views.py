from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "main/home.html")
# Create your views here.
