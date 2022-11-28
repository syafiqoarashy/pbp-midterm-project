from django.db import models

class Track(models.Model):
    id = models.CharField(max_length=5, primary_key=True)
    symposium = models.CharField(max_length=5)
    title = models.CharField(max_length=100)

class Submission(models.Model):
    id = models.CharField(max_length=4, primary_key=True)
    trackId = models.ForeignKey(Track, on_delete=models.RESTRICT)
    track = models.CharField(max_length=5)
    title = models.TextField()
    authors_name = models.TextField()
    submitted = models.DateTimeField()
    lastUpdated = models.DateTimeField()
    keywords = models.TextField()
    decision = models.TextField()
    notified = models.BooleanField(null=True)
    reviewsSent = models.BooleanField(null=True)
    abstract = models.TextField()
    location = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TextField()
    chair = models.TextField()