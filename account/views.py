from .models import Account, MessageToStudent
from django.views.generic import ListView, CreateView, UpdateView, TemplateView, DetailView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate, logout
from account.forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm, StudentForm, ImageUpdateForm, MessageToStudentForm
from extra_views import InlineFormSet, UpdateWithInlinesView
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import get_user_model
from django.core.signing import BadSignature, SignatureExpired, loads, dumps
from django.http import Http404, HttpResponseBadRequest
from django.template.loader import render_to_string
from django.conf import settings
from django.template.loader import get_template
from django.core.mail import BadHeaderError, send_mail
from .decorators import student_required, teacher_required
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from teacher.models import TeacherFunction
from teacher.forms import TeacherFunctionForms
# from classroom.models import Class, Register, Course



User = get_user_model()


class MessageToStudentView(CreateView):
    model = MessageToStudent
    form_class = MessageToStudentForm
    success_url = reverse_lazy('index')
    # template_name = 'account/messagetostudent_form.html'

# class HomeView(ListView):
#
#     model = Course
#     paginate_by = 10
#     template_name = 'course/course_list.html'
#
#
#     def get_queryset(self):
#         current_user = self.request.user
#         if current_user.is_superuser:
#             return Course.objects.all()
#         else:
#             return Course.objects.filter(name=current_user.id)


#
# class HomeView(ListView):
#
#     model = Class
#     paginate_by = 10
#     template_name = 'account/account_list.html'
#
#     def get_queryset(self):
#         current_user = self.request.user
#         if current_user.is_superuser:
#             return Class.objects.all()
#         else:
#             return Class.objects.filter(teacher=current_user.id)
#


    # def get_context_data(self, **kwargs):
    #
    #     context = super(HomeView, self).get_context_data(**kwargs)
    #
    #     page_obj1 = Paginator(Account.objects.select_related().all(), self.paginate_by)
    #     context['accounts'] = page_obj1.page(context['page_obj'].number)
    #     context['teachers'] = TeacherFunction.objects.all()
    #     # page_obj2 = Paginator(TeacherFunction.objects.select_related().all(), self.paginate_by)
    #     # context['teachers'] = page_obj2.page(context['page_obj'].number)
    #     context['classes'] = Class.objects.all()
    #     context['teachers'] = TeacherFunction.objects.all()
    #     context['registers'] = Register.objects.all()
    #
    #     return context




        # return render(request, 'Blog/home.html', context)





    def get_is_student_count(self):
        return Account.objects.filter(is_student=True).count()




def teacher_view(request):
    accounts = Account.objects.all()
    page = request.GET.get('page1')
    paginator = Paginator(accounts, 1)

    try:
        accounts = paginator.page(page)
    except PageNotAnInteger:
        accounts = paginator.page(1)
    except EmptyPage:
        accounts = paginator.page(paginator.num_pages)

    teachers = TeacherFunction.objects.all()
    paginator = Paginator(teachers, 1)
    page = request.GET.get('page2')
    try:
        teachers = paginator.page(page)
    except PageNotAnInteger:
        teachers = paginator.page(1)
    except EmptyPage:
        teachers = paginator.page(paginator.num_pages)

    context = {'accounts': accounts, 'teachers': teachers}
    return render(request, 'account/account_list.html', context)



# Class View Account_Create_View

class StudentSignUp(CreateView):
    template_name = 'account/account_create.html'
    form_class = RegistrationForm
    # model = User
    success_url = reverse_lazy('account_create_done')
# {% Email-confirmation %}


    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'is_student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):

        user = form.save(commit=False)
        user.is_active = False
        user.is_student = True


        user.save()

        current_site = get_current_site(self.request)
        domain = current_site.domain
        context = {
            'protocol': self.request.scheme,
            'domain': domain,
            'token': dumps(user.pk),
            'user': user,
        }


        subject = render_to_string('account/mail_template/create/subject.txt', context)
        """本文"""
        message = render_to_string('account/mail_template/create/message.txt', context)
        """送信元メールアドレス"""

        user.email_user(subject, message)


        return redirect('account_create_done')


class TeacherSignUp(CreateView):
    template_name = 'account/account_create.html'
    form_class = RegistrationForm
    # model = User
    success_url = reverse_lazy('account_create_done')
# {% Email-confirmation %}

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'is_teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):

        user = form.save()
        user.is_active = False
        user.is_teacher = True


        user.save()

        current_site = get_current_site(self.request)
        domain = current_site.domain
        context = {
            'protocol': self.request.scheme,
            'domain': domain,
            'token': dumps(user.pk),
            'user': user,
        }


        subject = render_to_string('account/mail_template/create/subject.txt', context)
        """本文"""
        message = render_to_string('account/mail_template/create/message.txt', context)
        """送信元メールアドレス"""


        user.email_user(subject, message)


        return redirect('account_create_done')


class AccountCreateDoneView(TemplateView):

    template_name = 'account/account_create_done.html'

class AccountCreateCompleteView(TemplateView):

    template_name = 'account/account_create_complete.html'
    timeout_seconds = getattr(settings, 'ACTIVATION_TIMEOUT_SECONDS', 60*60*24)

    def get(self, request, **kwargs):
        token = kwargs.get('token')
        try:
            user_pk = loads(token, max_age=self.timeout_seconds)
        except SignatureExpired:
            return HttpResponseBadRequest()
        except BadSignature:
            return HttpResponseBadRequest()

        else:
            try:
                user = User.objects.get(pk=user_pk)
            except User.DoesNotExist:
                return HttpResponseBadRequest()
            else:
                if not user.is_active:

                    user.is_active = True
                    user.save()
                    return super().get(request, **kwargs)
        return HttpResponseBadRequest()



class LogoutConfirmView(TemplateView):
    template_name = 'registration/logout_confirm.html'

class PasswordChangeView(TemplateView):
    template_name = 'registration/password_change_form.html'


# {{login 関数　}}


def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect('index')
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

        if user:
            login(request, user)
            return redirect('index')
    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form

    return render(request, 'account/login.html', context)

class Login(LoginView):
    form_class = AccountAuthenticationForm
    template_name = 'account/login.html'

# {{login_student 関数　}}

# @student_required
def login_student(request):

    context = {}
    # user = request.user
    # if user.is_authenticated:
    # return redirect('index')

    if request.POST:
        form = StudentForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            # is_student = request.POST['is_student']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('index')
    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form
    # form.add_error(None, 'you dont have student ID')
    return render(request, 'account/login.html', context)


class AccountUpdateView(UpdateView):
    model = Account
    form_class = AccountUpdateForm
    template_name = "account/account_update.html"
    success_url = reverse_lazy('index')

class ProfileTemplateView(TemplateView):
    template_name = 'account/profile.html'

class AccountInlineFormSet(InlineFormSet):
    model = Account
    fields = ('email', 'username', )
    can_delete = True


class AccountInformationView(TemplateView):
    template_name = 'account/account_info.html'

class AccountDetailView(DetailView):
    model = Account







# ------------------------------------------------------------------------------- #

# {{関数ベースview}}
def registration_view(request):

    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('index')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'account/register.html', context)

def account_view(request):
    if not request.user.is_authenticated:
        return redirect('login')

    context = {}

    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = AccountUpdateForm(
            initial={
                'email': request.user.email,
                'username': request.user.username,
            }
        )
        context['account_form'] = form
        return render(request, 'account/account.html', context)