# sendsms/urls.py

from django.urls import path
from .views import send_sms_view


urlpatterns = [
    path('send-sms/', send_sms_view, name='send_sms_view'),
]
