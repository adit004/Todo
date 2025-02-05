from django.shortcuts import render

from new_app.forms import TodoForms


# Create your views here.
def index(request):
    return render(request,"index.html")


def dashboard(request):
    return render(request, "dashboard.html")


def createTodo(request):
    data = TodoForms()
    return render(request,'create.html',{'form':data})