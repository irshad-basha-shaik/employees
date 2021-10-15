from django.db import models

# Create your models here.

class Employee(models.Model):
    email=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    contact=models.CharField(max_length=50)
    depid=models.CharField(max_length=100, default='1')

    class Meta:
        db_table='employee'

class Department(models.Model):
    dname=models.CharField(max_length=100)

    class Meta:
        db_table='department'
