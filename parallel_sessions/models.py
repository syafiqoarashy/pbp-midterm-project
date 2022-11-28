from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class Tracks(models.Model):
    symposium = models.CharField(max_length = 20)
    title = models.TextField()

