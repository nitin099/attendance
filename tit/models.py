from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20,null=False , blank=False)
    roll_no = models.IntegerField()
    branch = models.CharField(max_length=20)
    days_attended = models.IntegerField()
    timestamp=models.DateTimeField(auto_now=True, auto_now_add=False)
    update=models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name

class Day(models.Model):
    total_days = models.IntegerField()
