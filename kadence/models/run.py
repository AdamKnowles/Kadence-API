from django.db import models




class Run(models.Model):
    time = models.TimeField(auto_now_add=False)
    date = models.DateField()
    distance = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.TimeField(auto_now_add=False)



    class Meta:
        verbose_name = ("run")
        verbose_name_plural = ("runs")