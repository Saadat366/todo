from django.db import models

class ToDoList(models.Model):
    url = models.IntegerField(unique=True)
    code = models.CharField(
        max_length=50,
        null=True,
        blank=True
        )
    def __str__(self):
        return str(self.url)


class ToDo(models.Model):
    text = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    todo_list = models.ForeignKey(
        to=ToDoList,
        null=True, blank=True,
        on_delete=models.SET_NULL
        )