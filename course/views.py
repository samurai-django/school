from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from .models import Course, CourseDetail
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator
from account.decorators import student_required, teacher_required, superuser_required
from .forms import AddCourseForm, AddCourseDetailForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.template.loader import render_to_string


class HomeView(LoginRequiredMixin, ListView):

    model = Course
    context_object_name = 'courses'
    paginate_by = 10
    template_name = 'course/course_list.html'

    def get_queryset(self):
        current_user = self.request.user
        if current_user.is_superuser:
            return Course.objects.filter(is_registered=False)
        elif current_user.is_student:
            return Course.objects.filter(is_registered=True)
        else:
            return Course.objects.filter(name=current_user.id)

class CourseDetailListView(ListView):
    model = CourseDetail
    context_object_name = 'courses'
    template_name = 'course/coursedetail_list.html'

    def get_context_data(self, **kwargs):
        context = super(CourseDetailListView, self).get_context_data(**kwargs)
        context['course'] = self.course


        return context

    def get_queryset(self):
        course = self.course = get_object_or_404(Course, pk=self.kwargs['pk'])
        queryset = super().get_queryset().filter(course=course)

        return queryset

class CourseDetailUpdateView(UpdateView):
    model = CourseDetail
    template_name = 'course/coursedetail_update.html'
    fields = ['number', 'pdf_file', ]
    success_url = reverse_lazy('index')







@method_decorator(teacher_required, name='dispatch')
class AddCourse(CreateView):
    model = Course
    form_class = AddCourseForm
    success_url = reverse_lazy('index')
    template_name = 'course/course_form.html'

    def form_valid(self, form):
        form.instance.name = self.request.user
        response = super(AddCourse, self).form_valid(form)
        if self.request.is_ajax():
            print(form.cleaned_data)
            data = {
                'message': "Successfully Created Course"
            }
            return JsonResponse(data)
        else:
            return response


@method_decorator(teacher_required, name='dispatch')
class AddCourseDetail(CreateView):
    model = CourseDetail
    form_class = AddCourseDetailForm
    success_url = reverse_lazy('index')
    template_name = 'course/course_detail_form.html'



    # def form_invalid(self, form):
    # def form_valid(self, form):
    #     form.instance.name = self.request.user
    #     return super(AddCourseDetail, self).form_valid(form)

@method_decorator(superuser_required, name='dispatch')
class ApproveView(UpdateView):
    model = Course
    template_name = 'course/course_update.html'
    fields = ['abstract', 'is_registered', ]
    success_url = reverse_lazy('index')


class CourseDetailView(DetailView):
    model = CourseDetail
    # queryset = CourseDetail.objects.all()
    context_object_name = 'courses'
    template_name = 'course/course_detail.html'


def course_create(request):
    form = AddCourseForm()
    context = {'form': form}
    html_form = render_to_string('course/course_ajax.html',
                                 context,
                                 request=request,
                                 )
    return JsonResponse({'html_form': html_form})

