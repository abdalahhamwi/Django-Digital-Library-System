from django.shortcuts import render

# Create your views here.

def digital_library (request): 
    return render (request,'index.html')