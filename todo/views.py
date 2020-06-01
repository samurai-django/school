from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from .models import Todo
from django.urls import reverse_lazy
from .forms import TodoForm
from django.views.generic.edit import ModelFormMixin


class TodoCreateView(CreateView):
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy('todo')

class TodoListView(ListView, ModelFormMixin):
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy('todo')
    template_name = 'todo/todo.html'
    paginate_by = 5

    def get_queryset(self):
        return Todo.objects.order_by('-date').first()




    def get(self, request, *args, **kwargs):
        self.object = None
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = None
        self.object_list = self.get_queryset()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)