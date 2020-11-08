from django.db import models
from django.contrib.auth.models import User
from django.core.validators import *

def validate_decimals(value):
    try:
        return round(float(value), 2)
    except:
        raise ValidationError(
            ('%(value)s is not an integer or a float  number'),
            params={'value': value},
        )


# Create your models here.
class Students(models.Model):
    section = (("",""),
               ("A","A"),
               ("B","B"),
               ("C","C"),
               ("D","D"))
    CHOICES = [(i, i) for i in range(11)]
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    student_email =models.EmailField(max_length=200,blank=True, null=True)
    class_number = models.IntegerField(max_length=10, choices=CHOICES)
    section = models.CharField(max_length=1, choices=section)
    roll_number = models.CharField(max_length=5)
    maths = models.FloatField(max_length=5,)
    english = models.FloatField(max_length=5,validators=[validate_decimals])
    social = models.FloatField(max_length=5,validators=[validate_decimals])
    evs = models.FloatField(max_length=5,validators=[validate_decimals])
    hindi = models.FloatField(max_length=5,validators=[validate_decimals])
    exam_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return "(0) – {1}".format(self.teacher,self.student_name,self.student_email,self.class_number, self.section, self.roll_number, self.maths,
                                  self.english, self.social, self.evs,self.hindi,self.exam_date)
