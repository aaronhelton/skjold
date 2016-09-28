from django.db import models
from semantic.models import Context, Klass

# Create your models here.
class Aspect(models.Model):
  name = models.CharField(max_length=25)
  contexts = models.ManyToManyField(Context)
  classes = models.ManyToManyField(Klass)

  def __str__(self):
    return self.name
  
class Section(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self):
    return self.name
