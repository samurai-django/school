from django.urls import path
from . views import TodoListView, TodoCreateView
urlpatterns = [

    path('', TodoListView.as_view(), name='todo'),
    path('create/', TodoCreateView.as_view(), name='create'),

]
