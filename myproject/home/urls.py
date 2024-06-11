from django.urls import path
from home.views import topics, problems

urlpatterns = [
    path("topics/", topics, name="topics"),
    path("topics/<int:topic_id>/problems/", problems, name="problems"),
    #path("problems/", problems, name="problems")
]