from django.urls import path
from .views import (
    HomeView,
    AddCourse,
    AddCourseDetail,
    ApproveView,
    CourseDetailView,
    CourseDetailListView,
    CourseDetailUpdateView,


)
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('create/', views.course_create, name='ajax'),
    path('course/<int:pk>/course_detail/', CourseDetailListView.as_view(), name="course_detail_list"),
    path('course/<int:pk>/course_detail/course_update/', CourseDetailUpdateView.as_view(), name="course_detail_update"),

    path('add_course/', AddCourse.as_view(), name='add_course'),
    path('add_course_detail/', AddCourseDetail.as_view(), name='add_course_detail'),
    path('approve_course/<int:pk>/', ApproveView.as_view(), name='update'),
    path('course_detail/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    # path('course_detail_list/<int:pk>/', CourseDetailListView.as_view(), name='course_detail_list'),


]
