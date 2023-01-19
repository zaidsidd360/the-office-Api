from django.db import models


class Character(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    summary = models.TextField()

    def __str__(self):
        return self.firstname + ' ' + self.lastname
