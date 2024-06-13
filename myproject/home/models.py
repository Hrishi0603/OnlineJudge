from django.db import models

# Create your models here.

class topic(models.Model):
    name = models.CharField(max_length=255) #Is statement a variable? Can it be replaced by 'topic'?

class problem(models.Model):
    #statement = models.CharField(max_length=255) 
    #How do I add another field?
    topic_link = models.ForeignKey(topic, on_delete=models.CASCADE, related_name='problems')
    title = models.CharField(max_length=255)
    statement = models.TextField()
    #name = models.CharField(max_length=255, default='Default Problem Name')  # Add default value here