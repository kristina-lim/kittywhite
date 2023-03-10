from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

MEALS = (
  ('B', 'Breakfast'),
  ('L', 'Lunch'),
  ('D', 'Dinner')
)

class Hobby(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)
  img = models.CharField(max_length=100, default='')

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('hobbies_detail', kwargs={'pk': self.id})

class Character(models.Model):
  name = models.CharField(max_length=100)
  img = models.CharField(max_length=100, default='')
  gender = models.CharField(max_length=100)
  birthday = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=350)
  hobbies = models.ManyToManyField(Hobby)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  
  def __str__(self):
    return f'{self.name} ({self.id})'

  def get_absolute_url(self):
    return reverse('detail', kwargs={'character_id': self.id})
  
  def fed_for_today(self):
    return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)

class Feeding(models.Model):
  date = models.DateField('feeding date')
  meal = models.CharField(
    max_length=1,
    choices=MEALS,
    default=MEALS[0][0]
  )
  character = models.ForeignKey(Character, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_meal_display()} on {self.date}"

  class Meta:
    ordering = ['-date']

class Photo(models.Model):
  url = models.CharField(max_length=200)
  character = models.ForeignKey(Character, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for character_id: {self.character_id} @{self.url}"