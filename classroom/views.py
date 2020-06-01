from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView, TemplateView, View
from .forms import ClassCreateForm, StudentClassRegisterForm, ClassDetailForm
from .models import Class, Register, Relationship, Relationship2, ClassDetail
from django.urls import reverse_lazy
from account.decorators import student_required, teacher_required
from django.utils.decorators import method_decorator
from django.db.models import Q
from django.contrib.auth import get_user_model
import logging
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.shortcuts import redirect




User =get_user_model()


class ClassListView(ListView):
    model = Class
    context_object_name = 'classes'
    paginate_by = 5


    def get_queryset(self):
        current_user = self.request.user
        if current_user.is_superuser:
            return Class.objects.all()
        else:
            return Class.objects.filter(teacher=current_user.id)


        # s_word = self.request.GET.get('query')
        #
        # if s_word:
        #     object_list = Class.objects.filter(
        #         Q(semester__icontains=s_word)
        #         # | Q(subject__icontains=s_word)
        #     )
        # else:
        #     object_list = Class.objects.all()
        #
        # return object_list
        #



class RegisterListView(ListView):
    model = Relationship
    context_object_name = 'registers'
    template_name = 'classroom/register_list.html'
    paginate_by = 10


@method_decorator(teacher_required, name='dispatch')
class ClassCreateView(CreateView):
    model = Class
    form_class = ClassCreateForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.teacher = self.request.user
        return super().form_valid(form)


class ClassDetailView(DetailView):
    model = Class
    template_name = 'classroom/class_detail.html'



class StudentClassDetail(DetailView):
    queryset = Register.objects.all()
    # models = Register
    template_name = 'classroom/register_detail.html'


class StudentRegisterClass(CreateView):
    model = Relationship2
    form_class = StudentClassRegisterForm
    template_name = 'classroom/relationship_form.html'

    success_url = reverse_lazy('classroom:student_class')

    def form_valid(self, form):
        form.instance.students_id = self.request.user.id
        return super(StudentRegisterClass, self).form_valid(form)


    # def form_valid(self, form):
    #     form.instance.student = self.request.user
    #     return super().form_valid(form)

class StudentClassListView(ListView):
    model = Relationship2
    context_object_name = 'registers'
    template_name = 'classroom/relationship2_list.html'
    paginate_by = 10

    def get_queryset(self):
        current_user = self.request.user
        if current_user.is_superuser:  # スーパーユーザの場合、リストにすべてを表示する。
            return Relationship2.objects.all()
        else:  # 一般ユーザは自分のレコードのみ表示する。
            return Relationship2.objects.filter(students=current_user.id)








class StudentDetail(DetailView):
    model = Relationship2
    template_name = "classroom/relationship2_detail.html"


    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        context = super().get_context_data(**kwargs)
        context['students'] = Relationship2.objects.filter(students=pk)
        return context
    #
    # def get_context_data(self, **kwargs):
    #     pk = self.kwargs['pk']
    #
    #     context = super(StudentDetail, self).get_context_data(**kwargs)
    #
    #     context['students'] = Relationship2.objects.filter(students=pk)
    #
    #     return context
class SampleTemplateView(TemplateView):
    template_name = 'dashboard.html'

class ClassDetailCreateView(CreateView):
    model = ClassDetail
    form_class = ClassDetailForm
    template_name = 'classroom/classdetail_form.html'
    success_url = reverse_lazy('classroom:student_class')

    def form_valid(self, form):
        form.instance.teachers_id = self.request.user.id
        return super(ClassDetailCreateView, self).form_valid(form)
