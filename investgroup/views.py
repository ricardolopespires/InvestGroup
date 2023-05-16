from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.views.generic import View
from django.shortcuts import render
from datetime import date
from uuid import uuid4









class Index_View(View):

    def get(self, request):
        return render(request,'initial/index.html')




