from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Players(models.Model):
    profiles models.OneToOneField(profile)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
 
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('profile', kwargs={'player_id': self.id})