from django.db import models

class BacterialStrain(models.Model):
    maturation_period = models.PositiveIntegerField()
    life_expectancy = models.PositiveIntegerField()
    reproduction_rate = models.PositiveIntegerField()
