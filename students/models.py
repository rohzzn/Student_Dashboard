from secrets import choice
from django.db import models

# Create your models here.
class Student(models.Model):

    gender_choice = (
        ('M', 'Male'),
        ('F', 'Female'),

    )

    roll_no = models.IntegerField()
    photo = models.ImageField(upload_to='photos/%y/%m/%d')
    full_name = models.CharField(max_length=50)
    course = models .CharField(max_length=50)
    grade = models.CharField(max_length=50)
    gender = models.CharField(choices=gender_choice, max_length=100)

    def __str__(self):
        return self.full_name