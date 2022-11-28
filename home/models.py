from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Testimonial(models.Model):
    username = models.CharField(max_length=255, default="Guest")
    content = models.TextField()
    institute = models.CharField(max_length=255)