#  serializers for user API view 

from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from django.utils.translation import gettext as _

class UserSerializers(serializers.ModelSerializer):
   
   class Meta:
      model = get_user_model()
      fields = ['email', 'name', 'password']
      extra_kwargs = {'password':{'write_only': True, 'min_length': 5}}
      
      
      def create(self, **validated_data):
         "create and return user with validated data (encrypted pass)"
         return get_user_model().objects.create_user(**validated_data)


class AuthTokenSerializer(serializers.Serializer):
   """ serializer for user auth token"""
   email = serializers.EmailField()
   password = serializers.CharField(
      trim_whitespace = True,
   )
   
   def validate (self, attrs):
      """ validate and authenticad the user"""
      email = attrs.get("email")
      password = attrs.get("password")
      
      user = authenticate(
         request= self.context.get('request'),
         username = email,
         password = password,
      )
      
      if not user : 
         msg = "enabale to authenticate user "
         raise serializers.ValidationError(msg)
      
      attrs['user'] = user
      return attrs