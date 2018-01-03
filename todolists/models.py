from django.contrib.auth.models import User
from django.db import models


class TodoList(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    user = models.ForeignKey(User)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class TodoListItem(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField()
    todolist = models.ForeignKey('TodoList')
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.title