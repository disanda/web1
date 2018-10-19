from django.db import models

# Create your models here.
# Create your models here.
class Classes(models.Model):
    titile = models.CharField(max_length=32)
    m = models.ManyToManyField("Teachers")
class Teachers(models.Model):
    name = models.CharField (max_length=32)
class Student(models.Model):
    username = models.CharField(max_length=32)
    age = models.IntegerField()
    gender = models.BooleanField()
    tel = models.CharField(max_length=32)
    cs = models.ForeignKey(Classes,on_delete=models.CASCADE,)
