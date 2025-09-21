from django.shortcuts import render
from django.http import HttpResponse

def pink_page(request):
    return HttpResponse("<h1>This is the Pink Page!</h1>")
