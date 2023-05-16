from django.views.generic import View, ListView, TemplateView, DetailView
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Avg, Count, Sum ,F, Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponseRedirect
from rest_framework.views import APIView
from django.utils.text import slugify
from django.contrib import messages
from datetime import date, datetime
from django.shortcuts import render
from rest_framework import generics
from accounts.models import User
from uuid import uuid4






class Marning_Call_View(LoginRequiredMixin, View):



	def get(self, request):
		return render(request, 'analytics/marning_call.html')