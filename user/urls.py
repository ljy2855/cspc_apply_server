from django.urls import path
from views import check_applicant
urlpatterns = [
    path('check-id',check_applicant),
]
