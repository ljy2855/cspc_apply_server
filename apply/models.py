from django.db import models

from user.models import Applicant

class TermType(models.TextChoices):
    SPRING = 'spring'
    FALL = 'fall'


class Recruitment(models.Model):
    year = models.PositiveSmallIntegerField()
    term = models.CharField(max_length=10, choices=TermType.choices)
    is_open = models.BooleanField()
    start_time = models.DateField()
    document_deadline = models.DateField()
    interview_start_time = models.DateField()
    interview_end_time = models.DateField()
    announce_time = models.DateField()
    
class InterViewTime(models.Model):
    time = models.DateTimeField()
    is_fixed = models.BooleanField(default=False)

class Resume(models.Model):
    applicant = models.OneToOneField(Applicant,on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    student_id = models.PositiveSmallIntegerField()
    semester = models.PositiveSmallIntegerField()
    #지원서 답변
    introduce = models.TextField(default='')
    motivate = models.TextField(default='')
    to_do = models.TextField(default='')
    etc = models.TextField(default='')

    interview_time_choice = models.ManyToManyField(InterViewTime,related_name="interview_time")
    interview_requirement = models.TextField(default='')




# Create your models here.
