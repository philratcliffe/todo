from django.shortcuts import render
from django.http import HttpResponseRedirect
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

class DetailView(generic.DetailView):
    model = models.ToDo
    template_name = 'todo/detail.html'

class DeleteView(generic.DeleteView):
    model = models.ToDo
    success_url = reverse_lazy('index')

def add(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/todo/')

    else:
        form = AddForm()

    return render(request, 'todo/add.html', {'form': form})







