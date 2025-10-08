from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.
def home(request: HttpRequest):
    user = request.user 
    return render(request, "home.html", context={
        "title": "Faunatrack October 2025",
        "username": user.username if user.is_authenticated else "Inconnu"
    })
    