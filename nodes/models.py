from django.db import models

# Create your models here.
class Nodes(models.Model):
    # node
    id=models.CharField(max_length=30,primary_key=True)
    name=models.CharField(max_length=30)
    value=models.CharField(max_length=30)
    x=models.IntegerField()
    y=models.IntegerField()
    symbol=models.CharField(max_length=30)
    symbol_size=models.IntegerField()
    itemStyle=models.JSONField()
    class Meta:
        managed=False
        db_table='nodes'

class Links(models.Model):
    id=models.CharField(max_length=30,primary_key=True)
    source = models.CharField(max_length=30)
    target = models.CharField(max_length=30)
    value = models.CharField(max_length=30)
    symbol=models.CharField(max_length=30)
    # link
    class Meta:
        managed=False
        db_table='links'

class Family(models.Model):
    id=models.CharField(max_length=30,primary_key=True)
    name=models.CharField(max_length=30)
    value=models.CharField(max_length=30)
    x=models.IntegerField()
    y=models.IntegerField()
    symbol=models.CharField(max_length=30)
    symbol_size=models.IntegerField()
    itemStyle=models.JSONField()
    class Meta:
        managed=False
        db_table='family'