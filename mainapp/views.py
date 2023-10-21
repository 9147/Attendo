from django.shortcuts import render,HttpResponse

def home(request):
    return render(request,'mainapp/home.html')

def about(request):
    return render(request,'mainapp/about.html')

def docs(request):
    return render(request,'mainapp/docs.html')