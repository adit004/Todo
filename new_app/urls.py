from django.urls import path


from new_app import views
# from new_app.views import createTodo

urlpatterns = [
    path('',views.index,name="index"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('view_todo',views.view_todo,name="view_todo"),
    path('delete_todo/<int:id>',views.delete_todo,name="delete_todo"),
    path('edit_todo/<int:id>', views.edit_todo, name="edit_todo"),
]