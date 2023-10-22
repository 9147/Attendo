from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Subject

@login_required(login_url="/login/")
def home(request):
    data=Subject.objects.all().filter()
    context={'data':data}
    return render(request,'mainapp/home.html',context=context)

@login_required(login_url="/login/")
def about(request):
    return render(request,'mainapp/about.html')

@login_required(login_url="/login/")
def docs(request):
    return render(request,'mainapp/docs.html')