"""InvestGroup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),


    path('',views.Index_View.as_view(), name = 'index'),
    path('',include('accounts.urls')),

    #------------------------ Dashboard ------------------------------------------

    path('dashboard/',include('dashboard.urls', namespace =  'dashboard')),
    path('settings/',include('settings.urls', namespace = 'settings')),
    path('',include('economia.urls', namespace = 'economia')),


    #---------------------------- Management Administration ---------------------------
    path('management/', include('management.urls', namespace = 'management')),
    path('quiz/',include('quiz.urls', namespace = 'quiz')),
    path('investor/',include('investor.urls', namespace = 'investor')),



    path('api/save_question_result/' , views.save_question_result),
    


    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


