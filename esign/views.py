from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# request handler
# request -> response


def say_hello(request):
    return render(request,'hello.html',{'name':'Guiguiba'})
    #return HttpResponse('Hello World')

def main(request):
    return render(request,'esign/home.html')

def homepage(request):
    return render(request,'home.html')

def project(request):
    esign= changerequest.objects.all()
    return render(request,'project.html',{'esign':esign})

def dashboard(request):
    clients = client.objects.all()
    esign = changerequest.objects.all()

    context = {'client':client, 'esign':esign}
    return render(request,'dashboard.html')

def about(request):
    return HttpResponse('About us')

