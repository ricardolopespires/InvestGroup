from django.urls import path
from . import views


app_name = 'dashboad'


urlpatterns =[

    path('dashboard/Investimentos', views.DashboadTemplateView.as_view(), name = 'manager'),


]