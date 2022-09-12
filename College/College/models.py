from django.db import models

class EventRegister(models.Model):
    Rollno = models.IntegerField(blank=False)
    Name = models.CharField(max_length=100, blank=False)
    Class = models.CharField(max_length=20, blank=False)
    Age = models.IntegerField(blank=False)

    def __str__(self):
        return self.Name