from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("You are at the Home Page")
    return render(request,"index.html")

def about (request):
    return HttpResponse("You are at the About Page")

def contact (request):
    return HttpResponse("You are at the Contact Page")