from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def users(request):
    return render(request, "users/users.html")

def profile(request, username):
    context = {
        "username": username,
        }
    return render(request, "users/profile.html", context)
