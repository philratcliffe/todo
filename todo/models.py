from django.db import models


class ToDo(models.Model):
    task_text = models.fields.CharField(max_length=200)
    created_date = models.DateTimeField('date created', auto_now_add=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.task_text
