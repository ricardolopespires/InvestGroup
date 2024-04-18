from django.urls import path
from . import views 
 
urlpatterns = [ 
    path('bank/<pk>', views.bank_list), 
    path('bank/details/<pk>', views.bank_detail), 
] 
