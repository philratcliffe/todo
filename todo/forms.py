from django.forms import ModelForm

from . import models

class AddForm(ModelForm):
    class Meta:
        model = models.ToDo
        fields = ['task_text']


