from django.db import models

# Create your models here.

class Link(models.Model):
    link = models.CharField(max_length=500)
    # filename = models.CharField(max_length=100)
    def __str__(self):
        return self.link