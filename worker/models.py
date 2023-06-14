from django.db import models

# Create your models here.

class EmployeeTimout(models.Model):

    employee_uid =  models.CharField(max_length=25, primary_key=True)
    hash = models.CharField(max_length=250)
    datetime = models.DateTimeField()

