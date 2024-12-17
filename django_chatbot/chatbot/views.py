from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def start(request):
    return render(request, "start.html")

# render chatbot.html page
def chatbot(request):
    return render(request, "chatbot.html")
