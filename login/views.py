from django.shortcuts import render,HttpResponse
from django.contrib.auth import authenticate, login,logout
from django.http import JsonResponse
from mainapp.views import home
from django.contrib import messages

def loginPage(request):
    return render(request,'login/login.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        type=request.POST['type']
        print("type:",type)
        print(username,password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if type=='admin':
                if user.is_superuser:
                    login(request,user)
                    return JsonResponse({'data':'success'})
                else:
                    return HttpResponse(status=401)
            login(request,user)
            print("success")
            return JsonResponse({'data':'success'})
        else:
            return HttpResponse(status=401)
    return HttpResponse(status=404)

def logoutPage(request):
    logout(request)
    return home(request)