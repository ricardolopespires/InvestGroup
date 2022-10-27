from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.db.models import Avg, Count, Sum ,F, Q
from django.views.generic import View
from datetime import date
from uuid import uuid4








class Profile_View(LoginRequiredMixin, View):


	def get(self, request):

		return render(request, 'settings/profile/index.html')