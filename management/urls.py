from django.urls import path
from . import views



app_name = 'management'



urlpatterns = [ 

	path('settings/',views.Settings_View.as_view(), name = 'settings'),


	path('settings/api/',views.Settings_Api_View.as_view(), name = 'api'),
	path('settings/api/<api_id>/detail/',views.Api_Detail_View.as_view(), name = 'detail_api'),
	path('settings/api/created/',views.Created_Api_View.as_view(), name = 'created_api'),


]
