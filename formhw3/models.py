from __future__ import unicode_literals

from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    office_details = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField()

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    classroom = models.CharField(max_length=100)
    times = models.CharField(max_length=100)
    #students = models.ManyToManyField(Student)
    #teacher = models.ForeignKey(Teacher)
