from django.urls import path
from .views import SideBar


urlpatterns = [

    path('', SideBar.as_view(), name='sidebar'),


]

