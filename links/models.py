from django.db import models

# Create your models here.
class Links(models.Model):
    # node
    source=models.CharField(max_length=30)
    target=models.CharField(max_length=30)
    color=models.CharField(max_length=30)