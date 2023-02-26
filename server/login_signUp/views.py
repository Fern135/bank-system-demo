from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('<h1>Html works</h1>')

def login(request):
    return HttpResponse('login hello login')


def signUp(request):
    return HttpResponse('hello signing up ')


def forgot(request):
    return HttpResponse('hello forgot')
