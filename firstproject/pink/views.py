from django.shortcuts import render
from django.http import HttpResponse

def pink_page(request):
    return render(request, "pink.html")
