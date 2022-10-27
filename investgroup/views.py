from django.views.generic import View
from django.shortcuts import render










class Index_View(View):

    def get(self, request):
        return render(request,'initial/index.html')

