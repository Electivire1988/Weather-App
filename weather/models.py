from django.db import models

class City(models.Model):
    name = models.CharField(max_length=35)

    def __srt__(self):
        return self.name
