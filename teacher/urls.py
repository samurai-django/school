from django.urls import path
from .views import TeacherFunctionView, TeacherFunctionListView
urlpatterns = [
    path('', TeacherFunctionView.as_view(), name='teacher'),
    path('list/', TeacherFunctionListView.as_view(), name='teacher_list'),
    # path('class/', ClassListView.as_view(), name='class'),


]
