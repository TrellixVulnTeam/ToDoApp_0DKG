from django.forms import ModelForm

from . models import TodoList

class TodoListForm(ModelForm):
    class Meta:
        model = TodoList
        fields = ['title', 'description']