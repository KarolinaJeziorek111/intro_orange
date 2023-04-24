from django.shortcuts import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello(request):
    return HttpResponse("Hello, world")

def name(request):
    return HttpResponse("<h2>Witaj, <span style='color:red;'>Karolina</span><h2>")

def hi(request):
    return HttpResponse(
        """"
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset='UTF-8'>
    </head>
    <title>Witaj</title>
    <body>
    Hi world
    </body>
    </html>
    """
    )

def hi2(request):
    return render(request, 'hi_html.html')