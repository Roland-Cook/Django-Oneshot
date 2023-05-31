from django.shortcuts import render
from todos.models import TodoList

# Create your views here.

def todo_view(request):
    todo_total=TodoList.objects.all()
    context={
        "todo_list":todo_total
    }
    return render(request, "todos/todolist.html", context)
