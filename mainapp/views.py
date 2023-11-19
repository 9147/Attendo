from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Subject,Class,Student,Attendance,StudentList
from django.contrib.auth.models import User
from django.http import JsonResponse
from datetime import date

@login_required(login_url="/login/")
def demo(request):
    return render(request,'mainapp/demo.html')
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
                data=Student.objects.filter(Class=sub.Class)
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
                data=Student.objects.filter(Class=sub.Class)
            context={'data':data,"sid":sid}
            for a in data:
                print(a.rollno)
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
                    # change this to get data from studentlist
                    data = sub.students.all()
                else:
                    print(Student.objects.filter(Class=sub.Class))
                    data = Student.objects.filter(Class=sub.Class)
                    print("data:",data)
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
    elif option=='list':
        attr=[f.attname for f in StudentList._meta.fields]
        data=StudentList.objects.all()
    return render(request,'mainapp/edit.html',{'option':option,'attr':attr,'data':data})

@login_required(login_url="/login/")
def editmain(request,option,id):
    data = None
    if option=='stud':
        attr=[f.attname for f in Student._meta.fields]
        print(attr)
        type=['text','number','text']
        if id!='00':
            data=Student.objects.get(rollno=id)
    elif option=='class':
        attr=[f.attname for f in Class._meta.fields]
        type=['text']
        if id!='00':
            data=Class.objects.get(cid=id)
    elif option=='sub':
        attr=[f.attname for f in Subject._meta.fields]
        type = ['text', 'text', 'text', 'number', 'checkbox']
        if id!='00':
            data=Subject.objects.get(sid=id)
            print(data)
    elif option=='prof':
        attr=['id', 'username', 'first_name', 'last_name', 'email','password']
        type=['number','text','text','text','email','password']
        if id!='00':
            data=User.objects.get(id=id)
    attr=zip(attr,type)
    return render(request,'mainapp/editmain.html',{'id':id,'option':option,'attr':attr,'data':data,'class':Class.objects.all(),'prof':User.objects.all()})

@login_required(login_url="/login/")
def update(request,option,id):
    if option=='stud':
        if id=='00':
            val=Student(rollno=request.POST.get('rollno'),name=request.POST.get('name'),Class=Class.objects.get(cid=request.POST.get('Class_id')))
            val.save()
        else:
            val=Student.objects.get(rollno=id)
            val.rollno=request.POST.get('rollno')
            val.name=request.POST.get('name')
            val.Class=Class.objects.get(cid=request.POST.get('Class_id'))
            val.save()
    elif option=='class':
        print(request.POST.get('cid'))
        if id=='00':
            val=Class(cid=request.POST.get('cid'))
            val.save()
        else:
            val=Class.objects.get(cid=id)
            val.save()
    elif option=='sub':
        if id=='00':
            print(request.POST.get('name'))
            print(Class.objects.get(cid=request.POST.get('Class_id')))
            print(User.objects.get(id=request.POST.get('prof_id')))
            print(False if request.POST.get('partial') == None else True)
            val=Subject(sid=request.POST.get('sid'),name=request.POST.get('name'),Class=Class.objects.get(cid=request.POST.get('Class_id')),prof=User.objects.get(id=request.POST.get('prof_id')),partial=False if request.POST.get('partial') == None else True)
            val.save()
            # if val.partial:
            #     for a in val.cid.students.all():
            #         val.students.add(a)
            #     val.save()
        else:
            val=Subject.objects.get(sid=id)
            val.sname=request.POST.get('name')
            val.cid=Class.objects.get(cid=request.POST.get('Class_id'))
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
            # print("password:",request.POST.get('password'))
            val=User(username=request.POST.get('username'),first_name=request.POST.get('first_name'),last_name=request.POST.get('last_name'),email=request.POST.get('email'))
            val.set_password(request.POST.get('password'))
            val.save()
        else:
            # print("password:",request.POST.get('password'))
            val=User.objects.get(id=id)
            val.username=request.POST.get('username')
            val.first_name=request.POST.get('first_name')
            val.last_name=request.POST.get('last_name')
            val.email=request.POST.get('email')
            val.set_password(request.POST.get('password'))
            val.save()
    print('/edit/'+option+'/'+id)
    return HttpResponseRedirect('/edit/'+option)

@login_required(login_url="/login/")
def sheet(request,id):
    print(id)
    if id!=0:
        data=StudentList.objects.get(lid=id).student.all()
        list=StudentList.objects.get(lid=id)
    else:
        data=None
        list=None
    return render(request,'mainapp/sheet.html',{'id':id,'data':data,'StudentList':list,'class':Class.objects.all(),'subject':Subject.objects.filter(partial=True)})

@login_required(login_url="/login/")
def getData(request):
    if request.method == 'POST':
        if request.POST.get('data')=='class&subject&student':
            data1=Class.objects.all()
            data1=[{'cid':a.cid} for a in data1]
            data2=Subject.objects.all()
            data2=[{'sid':a.sid,'name':a.name,'partial':a.partial} for a in data2]
            data3=Student.objects.all()
            data3=[{'rollno':a.rollno,'name':a.name,'cid':a.Class.cid} for a in data3]
            data = {'class': data1, 'subject': data2, 'student': data3}
            return JsonResponse(data)
        elif request.POST.get('data')=='ListType&listsubjects':
            # print('obj:',StudentList.objects.get(lid=request.POST.get('id')).subjects.all())
            # val=StudentList.objects.get(lid=request.POST.get('id'))
            data=StudentList.objects.get(lid=request.POST.get('id')).subjects.all()
            data=[{'sid':a.sid,'name':a.name} for a in data]
            return JsonResponse({'type':StudentList.objects.get(lid=request.POST.get('id')).is_classList,'data':data})
    return HttpResponse(status=404)

@login_required(login_url="/login/")
def uploadData(request):
    if request.method== 'POST':
        data=request.POST.get('data')
        data=eval(data)
        print(data)
        for a in data['student']:
            if Student.objects.filter(rollno=a).exists():
                ele=Student.objects.get(rollno=a)
                ele.name=data['student'][a]['name']
                ele.Class=Class.objects.get(cid=data['student'][a]['class'])
                ele.save()
                # print(ele)
            else:
                val=Student(rollno=a,name=data['student'][a]['name'],Class=Class.objects.get(cid=data['student'][a]['class']))
                val.save()
                # print(val)
        if(data['id']!=''):
            list=StudentList.objects.get(lid=data['id'])
            list.name=data['listName']
            list.student.clear()
            list.subjects.clear()
        else:
            list=StudentList(name=data['listName'])
        list.is_classList = 0 == data['choice']
        if 0 == data['choice']:
            list.Class = Class.objects.get(cid=data['class'])
        else:
            for a in data['student']:
                std=Student.objects.get(rollno=a)
                list.student.add(std)
            for a in data['subject']:
                sub=Subject.objects.get(sid=a)
                list.subjects.add(sub)
        list.save()
        return JsonResponse({'data':'success'})
    return HttpResponse(status=404)