from django.contrib import admin
from django.urls import path
from apply.views import *

urlpatterns = [
    path('recruit',get_recuit_session),
    path('resume',api_resume),
]
