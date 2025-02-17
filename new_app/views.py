from django.shortcuts import render, redirect

from new_app.forms import TodoForms
from new_app.models import Todo


# Create your views here.
def index(request):
    return render(request,"index.html")


def dashboard(request):
    data = TodoForms()
    if request.method == 'POST':
        data = TodoForms(request.POST)
        if data.is_valid():
            data.save()
            return redirect('view_todo')
    return render(request, "dashboard.html",{'form':data})


# def createTodo(request):
#     data = TodoForms()
#     if request.method == 'POST':
#         data = TodoForms(request.POST)
#         if data.is_valid():
#             data.save()
#             return redirect('dashboard')
#     return render(request,'create.html',{'form':data})


def view_todo(request):
    data = Todo.objects.all()
    return render(request,'views.html',{'view':data})

# delete
def delete_todo(request,id):
    data = Todo.objects.get(id=id)
    data.delete()
    return redirect('view_todo')

#update
def edit_todo(request,id):
    data = Todo.objects.get(id=id)
    form = TodoForms(instance=data)
    if request.method == 'POST':
        form1 = TodoForms(request.POST,instance=data)
        if form1.is_valid():
            form1.save()
            return redirect('view_todo')
    return render(request,'update.html',{'form':form})
