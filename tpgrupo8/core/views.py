from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "core/home.html")

def lacteos(request):
    return render(request, "core/lacteos.html")

def contact(request):
    return render(request, "core/contact.html")
