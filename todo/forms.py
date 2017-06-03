from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from . import models

class AddForm(ModelForm):
    class Meta:
        model = models.ToDo
        fields = ['task_text']
        labels = {
            "task_text": _("Task"),
        }


