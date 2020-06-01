from django.shortcuts import render

from django.views.generic import ListView, CreateView, UpdateView, TemplateView, DetailView

class SideBar(TemplateView):
    template_name = 'users/sidebar.html'

