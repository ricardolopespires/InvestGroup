"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

urlpatterns = [
    path('api/v1/auth/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('api/v1/quiz/', include('quiz.urls')),
    path('api/v1/quiz/', include('quiz.urls')),
    path('api/v1/history/', include('history.urls')),
    path('api/v1/trading/', include('trading.urls')),    
    path('api/v1/finances/', include('finances.urls')),
    path('api/v1/transactions/', include('transactions.urls')),
    path('api/v1/plataform/', include('plataform.urls')),
    path('api/v1/advisor/', include('advisors.urls')),
    path('api/v1/notifications/', include('notifications.urls')),
    path('api/v1/agents/', include('agents.urls')),
    path('api/v1/management/', include('management.urls')),
    path('api/v1/personal/', include('personal.urls')),
    
]

# Add this block to serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
