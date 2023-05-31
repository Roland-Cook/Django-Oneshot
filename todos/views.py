from django.shortcuts import render,redirect
from todos.models import TodoList, TodoItem
from todos.forms import TodoForm

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


def create_todo_list(request):
    if request.method=="POST":
        form =TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todo_list_list")
    else:
        form =TodoForm()
    context = {
        "form":form
            }
    return render(request,"todos/todo_create.html", context)
