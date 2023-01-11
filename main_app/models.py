from django.db import models

# Create your models here.
class Character(models.Model):
  name = models.CharField(max_length=100)
  gender = models.CharField(max_length=100)
  birthday = models.CharField(max_length=100)
  species = models.CharField(max_length=100)
  description = models.TextField(max_length=350)
  
  def __str__(self):
    return f'{self.name} ({self.id})'