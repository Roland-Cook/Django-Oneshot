from django.urls import path
from todos.views import todo_view, show_todo_list, create_todo_list

urlpatterns = [
    path("", todo_view, name="todo_list_list"),
    path("<int:id>", show_todo_list, name="todo_list_detail"),
    path("create/", create_todo_list, name="create_todo_list")
]
