from django.urls import path
from .views import (
    ClassListView,
    ClassCreateView,
    ClassDetailView,
    StudentClassDetail,
    RegisterListView,
    StudentRegisterClass,
    StudentClassListView,
    StudentDetail,
    SampleTemplateView,
    ClassDetailCreateView



)

app_name = 'classroom'



urlpatterns = [
    path('', ClassListView.as_view(), name='classroom'),
    path('create_class/', ClassCreateView.as_view(), name='create_class'),
    path('detail_class/<slug>/', ClassDetailView.as_view(), name='detail_class'),
    path('detail_register/<int:pk>/', StudentClassDetail.as_view(), name='detail_register'),
    path('register/', RegisterListView.as_view(), name='register'),
    path('register_student/', StudentRegisterClass.as_view(), name='student_register'),
    path('register_class/', StudentClassListView.as_view(), name='student_class'),
    path('student_detail/<slug>/', StudentDetail.as_view(), name='student_detail'),
    path('sample/', SampleTemplateView.as_view(), name='sample'),
    path('class_detail/', ClassDetailCreateView.as_view(), name='class_detail'),


]


