from django.db import models
import math


class Run(models.Model):
    time = models.TimeField(auto_now_add=False)
    date = models.DateField()
    distance = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.TimeField(auto_now_add=False)

    class Meta:
        verbose_name = ("run")
        verbose_name_plural = ("runs")
        
    @property
    def pace(self):

        # get Run object
        run = Run.objects.get(pk=self.pk)

        # get duration value
        duration = str(run.duration)

        # split string into list
        duration_list = duration.split(":")

        # add hours, minutes, and seconds by their index to sum the total number of seconds in all three
        duration_in_seconds = (
            (int(duration_list[0]) * 60 * 60) + (int(duration_list[1]) * 60) + int(duration_list[2]))

        # divide total seconds and run distance to get pace
        pace = (duration_in_seconds / run.distance) / 60

        # split that resulting pace into tuple
        minutes_and_seconds = math.modf(pace)

        # get the places after decimal and turn it into seconds
        whole_seconds = round(minutes_and_seconds[0] * 60)

        # get final pace in the 00:00 format
        new_pace = (f'{round(minutes_and_seconds[1])}:{whole_seconds:02}')

        return new_pace

    @property
    def new_duration(self):
        run = Run.objects.get(pk=self.pk)

        # get duration value
        duration = str(run.duration)

        # split string into list
        duration_list = duration.split(":")

        final_duration = (f'{duration_list[0]} hours {duration_list[1]} min {duration_list[2]} sec')
        

        return final_duration

