from django.urls import path
from todos.views import todo_view

urlpatterns = [
    path("", todo_view, name="todo_list_list"),
]
