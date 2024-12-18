from django.urls import path
from .views import SubscribeView, UnsubscribeView, SendNewsletterView

urlpatterns = [
    path('subscribe/', SubscribeView.as_view(), name='subscribe'),
    path('unsubscribe/', UnsubscribeView.as_view(), name='unsubscribe'),
    path('send-newsletter/', SendNewsletterView.as_view(), name='send_newsletter'),
]
