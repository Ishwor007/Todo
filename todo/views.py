from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Todo

# Create your views here.

def todo(request):
    if request.method == 'POST':
        text2 = request.POST['text']
        todo = Todo()
        todo.text = text2
        todo.save()
        text = Todo.objects.all()
        context = {'text':text}
        return render(request,'todo/index.html',context)

    else:
        text = Todo.objects.all()
        context = {'text':text}
        return render(request,'todo/index.html',context)   


def addComplete(request,t_id):
    print("hello ",t_id)
    todo = Todo.objects.get(pk=t_id)
    todo.complete = True
    todo.save()
    return redirect('todo')


def delComplete(request):
    complete_todo = Todo.objects.filter(complete = True)
    complete_todo.delete()
    return redirect('todo')


def delAll(request):
    deleteToDo = Todo.objects.all()
    deleteToDo.delete()
    return redirect("todo")
    
