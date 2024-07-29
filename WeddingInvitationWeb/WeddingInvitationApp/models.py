from django.db import models

class GuestsPlusOne(models.Model):
    plus_one_name = models.CharField(max_length=50)
    plus_one_surname = models.CharField(max_length=25)
    plus_one_relation = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.name} {self.surname} - {self.relation}'

class GuestAttendence(models.Model):
    cell = models.CharField(max_length=15, primary_key=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    church_attendence = models.BooleanField()
    home_attendence = models.BooleanField()
    song_request = models.CharField(max_length=200, blank=True, null=True)
    plus_one = models.ForeignKey(GuestsPlusOne, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'{self.name} {self.surname}'
