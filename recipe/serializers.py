from rest_framework import serializers
from .models import *


class RecipeSerializer(serializers.ModelSerializer):
   # serializer for recipe 
   class Meta:
      model = RecipeModel
      fields =['id','title','description', 'time_minutes', 'price','user'] 
      read_only_fields= ['id']

   def validate_time_minutes(self, value):
      if value < 5 :
         raise serializers.ValidationError("too short time") 
      return value 

class RecipeDetailSerializer(RecipeSerializer):
   #  serializer for recipe detail view 
   
   class Meta(RecipeSerializer.Meta):
      fields = RecipeSerializer.Meta.fields + ['description'] 