from django.db import models

class Market(models.Model):
    date = models.DateField()
    open = models.CharField(max_length=128)
    high = models.CharField(max_length=128)
    low = models.CharField(max_length=128)
    close = models.CharField(max_length=128)
    shares_traded = models.IntegerField()
    turnover = models.FloatField()
