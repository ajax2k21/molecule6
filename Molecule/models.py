
from django.db import models

class Molecule(models.Model):
    LSN = models.BigIntegerField()
    sdf = models.TextField(max_length=100000)
