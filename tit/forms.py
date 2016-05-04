from django import forms
from .models import *

class AttendanceFrom(forms.ModelForm):
     class Meta:
         model = Student
         fields = [
         'name',
         'roll_no',
         'branch',
         'days_attended'
         ]

class TotalDays(forms.ModelForm):
    class Meta:
        model = Day
        fields = [
        "total_days"
        ]
