from django.db import models

# Create your models here.
class Heart(models.Model):
    age=models.CharField(max_length=30)
    anaemia=models.CharField(max_length=30)
    creatinine_phosphokinase=models.CharField(max_length=30)