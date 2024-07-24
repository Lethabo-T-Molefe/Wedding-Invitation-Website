from django.db import models

class GuestAttendence(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    cell = models.CharField(max_length=10, primary_key=True)
    church_attendence = models.BooleanField()
    home_attendence = models.BooleanField()
    song_request = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f'{self.name} {self.surname}'
