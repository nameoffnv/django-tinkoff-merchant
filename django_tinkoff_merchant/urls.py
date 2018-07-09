from django.urls import path

from .views import Notification

urlpatterns = [
    path('notification/', Notification.as_view(), name='notification'),
]
