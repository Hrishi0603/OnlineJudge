from django.db import models
from home.models import problem

# Create your models here.
class question(models.Model):
    problem_q = models.ForeignKey(problem, on_delete=models.CASCADE, related_name='questions')
    statement = models.TextField()


class CodeSubmission(models.Model):
    language = models.CharField(max_length=100)
    code = models.TextField()
    input_data = models.TextField(null=True,blank=True)
    output_data = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
