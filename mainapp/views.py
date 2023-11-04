from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Subject,Class,Student,Attendance
from django.contrib.auth.models import User
from django.http import JsonResponse
from datetime import date

@login_required(login_url="/login/")
def home(request):
    data=Subject.objects.filter(prof=request.user)
    # print(Subject.objects.filter(prof=request.user))
    context={'data':data}
    return render(request,'mainapp/home.html',context=context)

@login_required(login_url="/login/")
def about(request):
    return render(request,'mainapp/about.html')

@login_required(login_url="/login/")
def docs(request):
    return render(request,'mainapp/docs.html')

@login_required(login_url="/login/")
def swapy(request, sid):
    try:
        if request.user==Subject.objects.get(sid=sid).prof:
            sub=Subject.objects.get(sid=sid)
            if sub.partial:
                data=sub.students.all()
            else:
                data=sub.cid.students.all()
            context={'data':data}
            return render(request,'mainapp/swapy.html',context=context)
        else:
            return HttpResponse(status=404)
    except Exception:
        return HttpResponse(status=404)

@login_required(login_url="/login/")
def optionSelect(request,sid):
    try:
        if request.user==Subject.objects.get(sid=sid).prof:
            sub=Subject.objects.get(sid=sid)
            if sub.partial:
                data=sub.students.all()
            else:
                data=sub.cid.students.all()
            context={'data':data,'sub':sub,'sid':sid}
            return render(request,'mainapp/optionSelect.html',context=context)
        else:
            return HttpResponse(status=404)
    except Exception:
        return HttpResponse(status=404)

@login_required(login_url="/login/")
def mark(request, sid):
    try:
        if request.user==Subject.objects.get(sid=sid).prof:
            sub=Subject.objects.get(sid=sid)
            if sub.partial:
                data=sub.students.all()
            else:
                data=sub.cid.students.all()
            context={'data':data,"sid":sid}
            # for a in data:
                # print(a.rollno)
            return render(request,'mainapp/mark.html',context=context)
        else:
            return HttpResponse(status=404)
    except Exception:
        return HttpResponse(status=404)

@login_required(login_url="/login/")
def attendance(request,sid):
    if request.method == 'POST':
        try:
            if request.user == Subject.objects.get(sid=sid).prof:
                sub = Subject.objects.get(sid=sid)
                if sub.partial:
                    data = sub.students.all()
                else:
                    data = sub.cid.students.all()
                for a in data:
                    value = request.POST.get(str(a.rollno))
                    val=Attendance(sid=Subject.objects.get(sid=sid),rollno=a,date=date.today(),status=value)
                    val.save()
                # print(request.POST)
                return JsonResponse({'data': 'success'})
            else:
                return HttpResponse(status=404)
        except Exception as e:
            # print(e)
            return HttpResponse(status=404)
    return HttpResponse(status=404)

@login_required(login_url="/login/")
def edit(request,option):
    if option=='stud':
        attr=[f.attname for f in Student._meta.fields]
        data=Student.objects.all()
    elif option=='class':
        attr=[f.attname for f in Class._meta.fields]
        data=Class.objects.all()
    elif option=='sub':
        attr=[f.attname for f in Subject._meta.fields]
        data=Subject.objects.all()
    elif option=='prof':
        attr=['id', 'username', 'first_name', 'last_name', 'email']
        data=User.objects.all()
    return render(request,'mainapp/edit.html',{'option':option,'attr':attr,'data':data})

@login_required(login_url="/login/")
def editmain(request,option,id):
    data = None
    if option=='stud':
        attr=[f.attname for f in Student._meta.fields]
        type=['text','number','text']
        if id!='00':
            data=Student.objects.get(rollno=id)
    elif option=='class':
        attr=[f.attname for f in Class._meta.fields]
        type=['text','text']
        if id!='00':
            data=Class.objects.get(cid=id)
    elif option=='sub':
        attr=[f.attname for f in Subject._meta.fields]
        type = ['text', 'text', 'text', 'number', 'checkbox']
        if id!='00':
            data=Subject.objects.get(sid=id)
            print(data)
    elif option=='prof':
        attr=['id', 'username', 'first_name', 'last_name', 'email']
        type=['number','text','text','text','email']
        if id!='00':
            data=User.objects.get(id=id)
    attr=zip(attr,type)

    return render(request,'mainapp/editmain.html',{'id':id,'option':option,'attr':attr,'data':data})

@login_required(login_url="/login/")
def update(request,option,id):
    if option=='stud':
        if id=='00':
            print(request.POST.get('rollno'),request.POST.get('name'),request.POST.get('cid_id'),Class.objects.get(cid=request.POST.get('cid_id')))
            val=Student(rollno=request.POST.get('rollno'),name=request.POST.get('name'),cid=Class.objects.get(cid=request.POST.get('cid_id')))
            val.save()
        else:
            print(request.POST.get('rollno'), request.POST.get('name'), request.POST.get('cid_id'),
                  Class.objects.get(cid=request.POST.get('cid_id')))
            val=Student.objects.get(rollno=id)
            val.rollno=request.POST.get('rollno')
            val.name=request.POST.get('name')
            val.cid=Class.objects.get(cid=request.POST.get('cid_id'))
            val.save()
    elif option=='class':
        if id=='00':
            val=Class(name=request.POST.get('name'),cid=request.POST.get('cid'))
            val.save()
        else:
            val=Class.objects.get(cid=id)
            val.name=request.POST.get('name')
            val.save()
    elif option=='sub':
        if id=='00':
            print(request.POST.get('name'))
            print(Class.objects.get(cid=request.POST.get('cid_id')))
            print(User.objects.get(id=request.POST.get('prof_id')))
            print(False if request.POST.get('partial') == None else True)
            val=Subject(sid=request.POST.get('sid'),name=request.POST.get('name'),cid=Class.objects.get(cid=request.POST.get('cid_id')),prof=User.objects.get(id=request.POST.get('prof_id')),partial=False if request.POST.get('partial') == None else True)
            val.save()
            # if val.partial:
            #     for a in val.cid.students.all():
            #         val.students.add(a)
            #     val.save()
        else:
            val=Subject.objects.get(sid=id)
            val.sname=request.POST.get('name')
            val.cid=Class.objects.get(cid=request.POST.get('cid_id'))
            val.prof=User.objects.get(id=request.POST.get('prof_id'))
            val.partial=False if request.POST.get('partial') == None else True
            print("partial:",False if request.POST.get('partial') == None else True)
            val.save()
            # if val.partial:
            #     for a in val.cid.students.all():
            #         val.students.add(a)
            #     val.save()
    elif option=='prof':
        if id=='00':
            val=User(username=request.POST.get('username'),first_name=request.POST.get('first_name'),last_name=request.POST.get('last_name'),email=request.POST.get('email'))
            val.save()
        else:
            val=User.objects.get(id=id)
            val.username=request.POST.get('username')
            val.first_name=request.POST.get('first_name')
            val.last_name=request.POST.get('last_name')
            val.email=request.POST.get('email')
            val.save()
    print('/edit/'+option+'/'+id)
    return HttpResponseRedirect('/edit/'+option)
