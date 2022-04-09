from django.urls import path
from . import views


app_name = 'financeiro'


urlpatterns = [

    path('manager/capitais/',views.Manager_Capital_View.as_view(), name = 'manager'),
]

