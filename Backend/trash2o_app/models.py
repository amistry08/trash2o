from django.db import models
from django.contrib.auth.models import User

class Refill_Point(models.Model):
  'Water Refill locations'
  description = models.CharField(max_length=200)
  location = models.CharField(max_length=200)

  class Meta:
    ordering = ['description']

  def __str__(self):
    return f'{description}'


class Container(models.Model):
  'Refill containers'
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  brand = models.CharField(max_length=100)
  category = models.CharField(max_length=50)
  quantity = models.IntegerField()
  date_added = models.DateField(auto_now_add=True)

  class Meta:
    ordering = ["-date_added"]

  def __str__(self):
    return f'{quantity} added on {date_added}'


