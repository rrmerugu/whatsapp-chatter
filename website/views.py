from django.shortcuts import render

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


def landing(request):
    #chat_data = ChatMessages.objects.all()

    return render(request, 'landing.html', {'title': "Lucy | AI Mate"})


def signin(request):
    return render(request, 'signin.html', {'title': 'Signin'})


def chatdata(request):
    return render(request, 'chatdata.html', {'title': 'All Chat Data'})
