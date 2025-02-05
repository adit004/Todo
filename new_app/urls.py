from django.urls import path

from new_app import views
from new_app.views import createTodo

urlpatterns = [
    path('',views.index,name="index"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('Todo',views.createTodo,name="createTodo")
]