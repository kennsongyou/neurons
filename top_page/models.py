from django.db import models


# Create your models here.
class TopPage(models.Model):
    name = models.CharField(max_length=20)
    gender = models.IntegerField(max_length=11)
