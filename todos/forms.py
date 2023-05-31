from todos.models import TodoList
from django.forms import ModelForm

class TodoForm(ModelForm):
    class Meta:
        model=TodoList
        fields=[
            "name"
        ]
