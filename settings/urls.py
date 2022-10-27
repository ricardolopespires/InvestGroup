from django.urls import path
from . import views


app_name = 'settings'


urlpatterns = [

	path('profile/',views.Profile_View.as_view(), name = 'profile'),


]