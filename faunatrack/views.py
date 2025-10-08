from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def home(request: HttpRequest):
    print(request.user.profil.profil_picture)

    return HttpResponse("Bonjour")
    