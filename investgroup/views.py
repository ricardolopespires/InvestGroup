from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView,DetailView






class IndexTemplateView(TemplateView):
    template_name = 'initial/index.html'

class AboutTemplateView(TemplateView):
    template_name = 'initial/about.html'

class ServiceTemplateView(TemplateView):
    template_name = 'initial/service.html'


    