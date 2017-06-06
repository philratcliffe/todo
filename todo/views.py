from . import models
from .forms import AddForm
from django.views import generic
from django.core.urlresolvers import reverse_lazy


class IndexView(generic.ListView):
    template_name = 'todo/index.html'
    context_object_name = 'latest_todo_list'

    def get_queryset(self):
        """Return the last fifteen todos."""
        return models.ToDo.objects.all().order_by('created_date')[:15]


class UpdateView(generic.UpdateView):
    model = models.ToDo
    success_url = reverse_lazy('index')
    template_name_suffix = '_update_form'
    fields = ['task_text', 'done']


class DeleteView(generic.DeleteView):
    model = models.ToDo
    success_url = reverse_lazy('index')


class CreateView(generic.CreateView):
    model = models.ToDo
    success_url = reverse_lazy('index')
    form_class = AddForm
