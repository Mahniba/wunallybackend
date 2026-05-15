from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
    print("hellooooooooooooooooooooooooooooooooooooooooo")
    return HttpResponse("Hello, world. You're at the login page.")