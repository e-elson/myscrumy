from django.urls import path
from .views import get_grading_parameters

urlpatterns = [
    path('', get_grading_parameters),
]
