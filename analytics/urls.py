from django.urls import path
from . import views


app_name = 'analsytics'



from . import views

urlpatterns = [


    path('marning/call/',views.Marning_Call_View.as_view(), name = 'marning_call'),



]