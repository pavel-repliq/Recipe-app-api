from django.db import models
from app import settings
# Create your models here.


class RecipeModel(models.Model):
   #  Recipe objects 
   user = models.ForeignKey(
      settings.AUTH_USER_MODEL,
      on_delete=models.CASCADE,
   )
   title = models.CharField(max_length=250)
   description = models.TextField(blank=True)
   time_minutes = models.IntegerField()
   price = models.IntegerField()
   
   
   def __str__(self) -> str:
      return self.title