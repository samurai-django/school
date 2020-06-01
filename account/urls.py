from django.urls import path
from . import views
from .views import (
    StudentSignUp,
    TeacherSignUp,
    AccountUpdateView,
    ProfileTemplateView,
    # ProfileUpdateFormsetView,
    AccountCreateDoneView,
    AccountCreateCompleteView,
    # PasswordChangeView,
    AccountInformationView,
    AccountDetailView,
    LoginView,
    MessageToStudentView,
)

from django.contrib.auth import views as auth_views

urlpatterns = [

    path('register/', views.registration_view, name='registration'),
    path('login/', views.login_view, name='login_def'),
    path('class_login/', LoginView.as_view(), name='login'),

    path('def_login_student/', views.login_student, name='login_student'),
    # path('def_login_teacher/', views.login_teacher, name='login_teacher'),
    path('student_account_create/', StudentSignUp.as_view(), name='student_signup'),
    path('techer_account_create/', TeacherSignUp.as_view(), name='teacher_signup'),

    path('account_create/done/', AccountCreateDoneView.as_view(), name='account_create_done'),
    path('account_create/complete/<str:token>/', AccountCreateCompleteView.as_view(), name='account_create_complete'),
    # path('password_change/', PasswordChangeView.as_view(), name='password_change'),

    # path('password_change/', ),



    path('update/<int:pk>/', AccountUpdateView.as_view(), name='update'),
    path('profile/', ProfileTemplateView.as_view(), name='profile'),
    # path('profile-update/<int:pk>/', ProfileUpdateFormsetView.as_view(), name='update2'),

    path('account_inf/', AccountInformationView.as_view(), name='account_info'),
    path('account_detail/<int:pk>/', AccountDetailView.as_view(), name='detail'),

    path('messagetostudent/', MessageToStudentView.as_view(), name='message'),



]

