from django.db import models

# Create your models here.
class Nodes(models.Model):
    # node
    id=models.CharField(max_length=30,primary_key=True)
    name=models.CharField(max_length=30)
    val=models.IntegerField()
    color=models.CharField(max_length=30)
    class Meta:
        managed=False
        db_table='nodes_nodes'

class Links(models.Model):
    source=models.CharField(max_length=30)
    target=models.CharField(max_length=30)
    color=models.CharField(max_length=30)
    # link
    class Meta:
        managed=False
        db_table='links_links'