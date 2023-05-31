from todos.models import TodoList,TodoItem
from django.forms import ModelForm

class TodoForm(ModelForm):
    class Meta:
        model=TodoList
        fields=[
            "name"
        ]


class EditTodoForm(ModelForm):
    class Meta:
        model = TodoList
        fields = [
            "name"
        ]



class CreateTodoForm(ModelForm):
    class Meta:
        model = TodoItem
        fields = [
            "task",
            "due_date",
            "is_completed",
            "list"
        ]
