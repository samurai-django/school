from .forms import TeacherFunctionForms
from django.views.generic import CreateView, ListView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import TeacherFunction
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from account.decorators import student_required, teacher_required
from django.utils.decorators import method_decorator


User = get_user_model()

@method_decorator(login_required, name='dispatch')
@method_decorator(teacher_required, name='dispatch')
class TeacherFunctionView(CreateView):
    model = TeacherFunction
    # form_class = TeacherFunctionForms
    fields = ['title', 'content', ]
    success_url = reverse_lazy('index')
    template_name = 'teacher/teacher_forms.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TeacherFunctionListView(ListView):
    model = TeacherFunction
    context_object_name = 'posts'
    paginate_by = 2
    #
    # def get_queryset(self):
    #     return super().get_queryset().order_by('-date')





    # template_name = 'account/account_list.html'

    # def paginate_queryset(self, queryset, count):
    #     paginator = Paginator(queryset, count)
    #     page = self.request.GET.get('page')
    #     try:
    #         page_obj = paginator.page(page)
    #     except PageNotAnInteger:
    #         page_obj = paginator.page(1)
    #     except EmptyPage:
    #         page_obj = paginator.page(paginator.num_pages)
    #     return page_obj




    # def get_queryset(self):
    #     user = get_object_or_404(User, username=self.kwargs.get('username'))
    #     return TeacherFunction.objects.filter(author=user).order_by('-date')

