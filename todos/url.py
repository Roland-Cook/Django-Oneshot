from django.urls import path
from todos.views import todo_view, show_todo_list, create_todo_list, edit_todo_list, delete_todo_list, create_Todo_Item, update_todo_list

urlpatterns = [
    path("", todo_view, name="todo_list_list"),
    path("<int:id>", show_todo_list, name="todo_list_detail"),
    path("create/", create_todo_list, name="create_todo_list"),
    path("<int:id>/edit/", edit_todo_list, name="edit_todo_list"),
    path("<int:id>/delete", delete_todo_list, name="delete_todo_list"),
    path("items/create/", create_Todo_Item, name="create_todo_item"),
    path("items/<int:id>/edit/", update_todo_list, name="update_todo_list")
]
