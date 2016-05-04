from django.shortcuts import render ,redirect , get_object_or_404
from django.http import HttpResponseRedirect
from .models import *
from .forms import *

# Create your views hereh
def  home(request):
    return render(request,'base.html' , {})
def saved(request):
    return render(request,'ok.html',{})

def create(request):
    form = AttendanceFrom(request.POST or None)
    title = "Student Information"
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect(retrive)
    context = {
    'title' : title,
    'form':form
    }
    return render(request,'create.html',context)

def attended(request):
    form = TotalDays(request.POST or None)
    title = "Number of Working Days"
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect(retrive)
    context = {
    'title' : title,
    'form':form
    }
    return render(request,'create.html',context)

def calculate(request, id=None):
    instance = get_object_or_404(Student,id=id)
    print (instance.name)
    qv = Day.objects.all()
    a = 0
    for obj in qv:
        a = obj.total_days
    p=0
    p = (instance.days_attended/a)*100
    p = ('%.2f'%p)
    name =instance.name
    context= {
    "p":p,
    'name' : name
    }
    return render(request,'calculate.html',context)

def retrive(request):
    qu = Student.objects.all().order_by('name')
    context = {
    'qu' : qu
    }
    return render(request,'retrive.html',context)
def updatedays(request,id=None):
    instance = get_object_or_404(Day,id=1)
    form  =TotalDays(request.POST or None , instance = instance)

    context ={
    'form' :form,
    'title' : "Update Number of classes"
    }
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect(retrive)

    return render (request , "create.html" , context)
def updatestudent(request,id=None):
    instance = get_object_or_404(Student,id=id)
    form  =AttendanceFrom(request.POST or None , instance = instance)
    context ={
    'form' :form,
    'title' : "Update Student Information"
    }
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect(retrive)

    return render (request , "create.html" , context)
def detail(request ,id=None):
    instance = get_object_or_404(Student,id=id)
    print (instance.name)
    qv = Day.objects.all()
    a = 0
    for obj in qv:
        a = obj.total_days
    p=0
    p = (instance.days_attended/a)*100
    p = ('%.2f'%p)
    d = instance.days_attended
    r =  a - d
    context = {
    'instance' : instance,
    'title': 'Detail',
    'p':p,
    'r': r,
    'a':a
    }
    return render(request , 'detail.html' , context)
