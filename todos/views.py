from django.shortcuts import render
from todos.models import TodoList, TodoItem

# Create your views here.

def todo_view(request):
    todo_total = TodoList.objects.all()
    context = {
        "todo_list": todo_total
    }
    return render(request, "todos/todo_list.html", context)


def show_todo_list(request, id):
    todo_list_object = TodoList.objects.get(id=id)
    context = {
    "todo_list_object": todo_list_object
   }
    return render(request, "todos/todo_details.html", context)
