from dataclasses import Field
from distutils.command.upload import upload
from django.db import models

def user_directory_path(filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return f'speakers/2019/{filename}'

class Speakers(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    affiliation = models.CharField(max_length=75)
    country = models.CharField(max_length=30)
    type = models.CharField(max_length=10)
    profile = models.TextField()
    photoFilename = models.ImageField(upload_to=user_directory_path)
    storagePath = models.CharField(max_length=100)
    speechTitle = models.CharField(max_length=100, null=True)
    speechAbstract = models.TextField()
    time = models.DateTimeField()
    room = models.CharField(max_length=20)
    symposium = models.CharField(max_length=100)