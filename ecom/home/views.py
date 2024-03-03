from django.shortcuts import render,redirect
from . models import *

# Create your views here.


def home(request):

    task=Task.objects.filter(is_completed=False)
    completed_task=Task.objects.filter(is_completed=True)

    context = {
        'task':task,
        'completed_task':completed_task
    }
    
    return render(request,'home.html',context)


def mark_as_done(request,id):

    task=Task.objects.get(id=id)
    task.is_completed=True
    task.save()
   
    return redirect('home')


def add_task(request):

    if request.method=='POST':
        taskk=request.POST.get('taskk')
        datee=request.POST.get('datee')
        todo=Task.objects.create(name=taskk,created_date=datee)
        todo.save()

    return redirect('home')


def delete_task(request,id):

    task=Task.objects.get(id=id)
    task.delete()


    return redirect('home')


def mark_as_undone(request,id):
    task=Task.objects.get(id=id)
    task.is_completed=False
    task.save()

    return redirect('home')


# def update_task(request,id):
#     get_task=get_object_or_404(Task,id=id)
#     if
#     return redirect('home')
