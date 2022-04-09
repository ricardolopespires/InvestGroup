"""investgroup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [

    #-------------------- Index ------------------------------------------------------

    path('admin/', admin.site.urls),
    path('', views.IndexTemplateView.as_view(), name = 'index'),
    path('about/', views.AboutTemplateView.as_view(), name = 'about'),
    path('service/', views.ServiceTemplateView.as_view(), name = 'service'),
    path('', include('accounts.urls')),


    #---------------------- Dashboad ------------------------------------------------

    path('', include('dashboard.urls', namespace = 'dashboard')),
    path('analytics', include('analytics.urls', namespace = 'analytics')),
    path('acoes', include('acoes.urls', namespace = 'ações')),
    path('crypto/', include('crypto.urls', namespace = 'crypto')),
    path('capital/', include('financeiro.urls', namespace = 'financeiro')),

    #---------------------- Management administration---------------------------------

    path('management/',include('management.urls', namespace = 'management')),

]


if settings.DEBUG:
    urlpatterns  += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 