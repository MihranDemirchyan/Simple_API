from django.db import models


class Moto(models.Model):
    name = models.CharField(max_length=30)
    model = models.CharField(max_length=50)
    created_year = models.IntegerField()
    HP = models.IntegerField()
