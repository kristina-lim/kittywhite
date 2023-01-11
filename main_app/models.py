from django.db import models
from django.urls import reverse

# Create your models here.
class Character(models.Model):
  name = models.CharField(max_length=100)
  gender = models.CharField(max_length=100)
  birthday = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=350)
  
  def __str__(self):
    return f'{self.name} ({self.id})'

  def get_absolute_url(self):
    return reverse('detail', kwargs={'character_id': self.id})