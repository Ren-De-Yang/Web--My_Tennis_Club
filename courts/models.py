from django.db import models

class Court(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    type = models.CharField(max_length=255)

    def __str__(self):
        return self.name
