from django.shortcuts import render,redirect , get_object_or_404
from todos.models import TodoList, TodoItem
from todos.forms import TodoForm,EditTodoForm

# Create your views here.

def todo_view(request):
    todo_list = TodoList.objects.all()
    context = {
        "todo_list": todo_list,
    }
    return render(request, "todos/todo_list.html", context)


def show_todo_list(request, id):
    todo_list_object = TodoList.objects.get(id=id)
    context = {
    "todo_list_object": todo_list_object
   }
    return render(request, "todos/todo_details.html", context)


def create_todo_list(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todo_list_list")
    else:
        form = TodoForm()
    context = {
        "form": form
            }
    return render(request, "todos/todo_create.html", context)

def edit_todo_list(request,id):
    post = get_object_or_404(TodoList.objects, id=id)
    if request.method == "POST":
        form = EditTodoForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("todo_list_detail", id=id)
    else:
        form = EditTodoForm(instance=post)

    context={
        "post_object":post,
        "post_form":form,
    }
    return render(request, "todos/todo_edit.html", context)
