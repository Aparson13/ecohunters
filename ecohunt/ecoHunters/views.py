from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from operator import attrgetter

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def home(request):
    return render(request, 'home.html')

def signup(request):
    return render(request, 'signup.html')

def LeaderBoard(request):
    users = User.objects.all()
    sorted_users = sorted(users, key=attrgetter('score'), reverse=True)
    top_users = sorted_users[:20]
    context = {'users': top_users}
    return render(request, 'leaderboard.html', context)
    