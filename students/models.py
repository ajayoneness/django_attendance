from django.db import models
import datetime

class students(models.Model):
    name = models.TextField(max_length=200)
    enrollment_no = models.TextField(max_length=100,primary_key=True)
    sem = models.TextField(max_length=20)
    branch = models.TextField(max_length=200)

class teachers(models.Model):
    t_name = models.TextField(max_length=200)
    subject = models.TextField(max_length=200)
    sem = models.TextField(max_length=100)

class presentabsent(models.Model):
    id = models.TextField(primary_key=True , max_length=250)
    date = models.DateTimeField(default=datetime.datetime.now())
    enrollment = models.TextField(max_length=200)
    sub = models.TextField(max_length=100)
    sem = models.TextField(max_length=100)
    teacher = models.TextField(max_length=200)
    name =  models.TextField(max_length=200)

