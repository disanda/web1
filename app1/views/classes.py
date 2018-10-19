from django.shortcuts import render
from django.shortcuts import redirect
from app1 import models
def get_classes(request):
    cls_list = models.Classes.objects.all()
    return render(request,'classes/get_classes.html', {'cls_list': cls_list})

def add_classes(request):
    if request.method == "GET":
        cls_list = models.Classes.objects.all()
        return render(request,'classes/add_classes.html',{'cls_list':cls_list})
    elif request.method == 'POST':
        title = request.POST.get('titile')
        id = request.POST.get('id')
        models.Classes.objects.create(id=id,titile=title)
        return redirect('./get_students.html')

def del_classes(request):
    nid = request.GET.get('nid')
    models.Classes.objects.filter(id=nid).delete()
    return redirect('./get_students.html')

def edit_classes(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        obj = models.Classes.objects.filter(id=nid).first()
        return render(request,'classes/edit_classes.html', {'obj': obj})
    elif request.method == 'POST':
        nid = request.GET.get('nid')
        id = request.POST.get('id')
        title = request.POST.get('title')
        models.Classes.objects.filter(id=nid).update(id=id,titile=title)
        return redirect('./get_students.html')