from django.shortcuts import render
from django.shortcuts import redirect
from app1 import models

def get_students(request):
    cls_list = models.Student.objects.all()
    return render(request, 'students/get_students.html', {'stu_list': cls_list})

def add_students(request):
    if request.method == "GET":
        return render(request, 'students/add_students.html')
    elif request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        cs = request.POST.get('cs_id')
        tell = request.POST.get('tell')
        models.Student.objects.create(id=id,username=name,age=age,gender=gender,tel=tell,cs_id=cs)
        return redirect('./get_students.html')

def del_students(request):
    nid = request.GET.get('nid')
    models.Student.objects.filter(id=nid).delete()
    return redirect('./get_students.html')

def edit_students(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        obj = models.Student.objects.filter(id=nid).first()
        return render(request, 'students/edit_students.html', {'obj': obj})
    elif request.method == 'POST':
        nid = request.GET.get('nid')
        name = request.POST.get('name')
        models.Student.objects.filter(id=nid).update(username=name)
        age = request.POST.get('age')
        models.Student.objects.filter(id=nid).update(age=age)
        gender = request.POST.get('gender')
        models.Student.objects.filter(id=nid).update(gender=gender)
        cs = request.POST.get('cs')
        models.Student.objects.filter(id=nid).update(cs=cs)
        return redirect('./get_students.html')