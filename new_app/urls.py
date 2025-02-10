from django.urls import path
from setuptools.extern import names

from new_app import views
# from new_app.views import createTodo

urlpatterns = [
    path('',views.index,name="index"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('viewtodo',views.view_todo,name="view_todo")
    # path('Todo',views.createTodo,name="createTodo")
]