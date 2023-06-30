from django.db import models

# Create your models here.
class regist(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    contact=models.IntegerField()
    mail=models.CharField(max_length=30)
