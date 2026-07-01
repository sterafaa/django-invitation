from django.db import models

class Meeting(models.Model):
    date = models.DateTimeField()

    def __str__(self):
        return str(self.date)
