from django.urls import path

from .views import *

urlpatterns = [
    path('checkout/', checkout),
    path('orders/', OrdersList.as_view()),
]