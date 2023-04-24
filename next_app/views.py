from django.shortcuts import render, HttpResponse
from django.utils.html import escape

# Create your views here.

def hello(request):
    return HttpResponse("Hello World!")

def eva(request):
    return HttpResponse("Hello <span style='color:red'>Eva</span>!")

def adam(request):
    return HttpResponse("Hello Adam!")

def name(request, data):

    # pamiętaj escape jest output
    print(data)
    escaped_data = escape(data)
    print(escaped_data)
    return HttpResponse(f"Hello, {escaped_data}!")

# Xss - podatność xss
#

