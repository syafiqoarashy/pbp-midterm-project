from django.db import models

# Create your models here.
"""
class Speakers(models.Model):
    id = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=50)
    affiliation = models.CharField(max_length=150)
    country = models.CharField(max_length=30)
    speakerType = models.CharField(max_length=20)
    profile = models.TextField()
    photoFilename = models.TextField()
    storagePath = models.TextField()
    speechTitle = models.TextField()
    speechAbstract = models.TextField()
    time = models.CharField(max_length=15)
    room = models.CharField(max_length=50)
    symposium = models.CharField(max_length=15)
    """

class EventsGeneral(models.Model):
    id = models.CharField(max_length=3, primary_key=True)
    date = models.DateField()
    startTime = models.CharField(max_length=15)
    endTime = models.CharField(max_length=15)
    program = models.TextField()
    speaker = models.ForeignKey('speakers.Speakers', blank=True, null=True, on_delete=models.RESTRICT)
    place = models.CharField(max_length=50)
    isParallel = models.BooleanField()


class EventsParallel(models.Model):
    eventId = models.ForeignKey(EventsGeneral, on_delete=models.RESTRICT, blank=True, null=True, default=0)
    date = models.DateField()
    startTime = models.CharField(max_length=15)
    endTime = models.CharField(max_length=15)
    program = models.ForeignKey('submission.Track', on_delete=models.RESTRICT)
    speaker = models.ForeignKey('speakers.Speakers', blank=True, null=True, on_delete=models.RESTRICT)
    place = models.CharField(max_length=50)

