from django.shortcuts import render
from django.http import HttpRequest
from . models import Employee,Department
# Create your views here.

def getAllEmployees():
    return Employee.objects.all()
def fetchAllDepartments():
    return Department.objects.all()
def index(request):
    return HttpRequest("This is a Index Page:")
def home(request):
    res = fetchAllDepartments()
    return render(request,"home.html",{"form_list":res})
def saveform(request):
    res = Employee.objects.all()
    if request.method=="POST":
        form = Employee(email=request.POST['email'], name=request.POST['name'], contact=request.POST['contact'], depid=request.POST['depid'])
        form.save()

    return render(request, "lob.html", {"form_list": res,"depts":fetchAllDepartments()})


def edit(request):
    id = request.GET['id']
    d = Employee.objects.get(id=id)
    d1 = Department.objects.all()
    return render(request,"edit.html",{"form":d,"depts":d1})

def editform(request):
    res = getAllEmployees()
    d = Employee.objects.filter(id=request.POST['id']).update(email=request.POST['email'],name=request.POST['name'], contact=request.POST['contact'],depid=request.POST['departments'])
    return render(request,"lob.html",{"form_list": res})
def delete(request):
    res = getAllEmployees()
    d = Employee.objects.filter(id=request.GET['id']).delete()
    return render(request, "lob.html",{"form_list":res})

def dentry(request):
    if request.method == 'POST':
        d=Department(dname=request.POST['dname'])
        d.save()
        return dmenu(request)
    return render(request,"dentry.html",{})

def dmenu(request):
    res=fetchAllDepartments()
    return render(request,"dmenu.html",{"form_list":res})
