from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
    print("hhh")
    return HttpResponse("first docker images and ")
