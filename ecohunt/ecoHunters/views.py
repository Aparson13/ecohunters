from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from operator import attrgetter

person = ""

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        new_name=request.POST['name']
        new_user=request.POST['newUsername']
        new_pass=request.POST['newPassword']

        if new_name == '':
            context = {
                'valid' : 'Please type in a name'
            }
            return render(request, 'signup.html', context)

        elif new_user == '':
            context = {
                'valid' : 'Please type in a username'
            }
            return render(request, 'signup.html', context)

        elif new_pass == '':
            context = {
                'valid' : 'Please type in a password'
            }
            return render(request, 'signup.html', context)
        else:
            if User.objects.filter(username=new_user).exists():
                context = {
                    'valid' : '**Username Already Taken**'
                }
                return render(request, 'signup.html', context)
            else:
                newUser = User(name=new_name, username=new_user, password=new_pass)
                newUser.save()
                global person
                person = new_user
                return render(request, 'home.html')         
    return render(request, 'signup.html')


def login(request):
    context ={
        'correct':""
    }
    if 'username' in request.POST:
        #gets username and password from text box
        usernameTxt = request.POST['username']
        passwordTxt = request.POST['password']
        #query username and password
        if User.objects.filter(username=usernameTxt).exists():
            usernamePerson = User.objects.get(username=usernameTxt)
            if usernamePerson.password == passwordTxt:
                global person
                person = usernameTxt
                return home(request)
            else:
                context = {
                    'correct':'Password incorrect'
                }
                return render(request, 'login.html', context)
        else:
            context = {
                    'correct':'User does not exist'
                }
    return render(request, 'login.html', context)

def LeaderBoard(request):
    users = User.objects.all()
    sorted_users = sorted(users, key=attrgetter('score'), reverse=True)
    top_users = sorted_users[:20]
    context = {'users': top_users}
    return render(request, 'leaderboard.html', context)
    