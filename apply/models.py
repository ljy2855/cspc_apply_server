from django.db import models

class TermType(models.TextChoices):
    SPRING = 'spring'
    FALL = 'fall'

class Question(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=300)

class Recruitment(models.Model):
    year = models.PositiveSmallIntegerField()
    term = models.CharField(max_length=10, choices=TermType)
    is_open = models.BooleanField(default=True)

class Resume(models.Model):
    name = models.CharField(max_length=10)
    secret = models.CharField(max_length=20)
    


# Create your models here.
