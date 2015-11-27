from django.db import models

class ToDo(models.Model):
    todo_text = models.fields.CharField(max_length=200)
    created_date = models.DateTimeField('date created', auto_now_add=True)
    done = models.BooleanField(default=False)

    def __unicode__(self):
        return self.todo_text


