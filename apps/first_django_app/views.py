from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect("/")

def show(request, blog_num):
    return HttpResponse("placeholder to display blog number: "+blog_num)

def edit(request, blog_num):
    return HttpResponse("placeholder to edit blog "+blog_num)

def destroy(request, blog_num):
    return redirect("/")

# Create your views here.
