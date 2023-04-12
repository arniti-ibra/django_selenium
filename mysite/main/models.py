from django.db import models

# Create your models here.
class Player(models.Model):
  name = models.CharField(max_length=100, unique=True)
  height = models.CharField(max_length=100)
  team = models.CharField(max_length=100)
  ppg = models.DecimalField(max_digits=5, decimal_places= 2)

  def __unicode__(self):
    return self.id()