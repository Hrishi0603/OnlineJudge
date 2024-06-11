from django.urls import path
from question.views import submit

urlpatterns = [
    path("", submit, name="submit"),
]
