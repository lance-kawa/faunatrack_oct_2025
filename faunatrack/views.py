from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.
def home(request: HttpRequest):
    return render(request, "home.html", context={
        "title": "Faunatrack October 2025"
    })
    