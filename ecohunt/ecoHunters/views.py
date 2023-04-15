from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def home(request):
    return render(request, 'home.html')

def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')
