""" 
   views for user API 
"""

from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from .serializers import * 
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics 
from rest_framework.authtoken.views import ObtainAuthToken
# Create your views here.


# class UserCreateView(APIView):
#    "view for create user in sytem"
   
#    def get(self,request):
#       user = get_user_model().objects.all()
#       serializer = UserSerializers(user,many=True)
#       return Response(serializer.data, status = status.HTTP_200_OK)
#    def post(self, request):
#       serializer = UserSerializers(data=request.data)
#       if serializer.is_valid():
#          serializer.save()
#          return Response(serializer.data, status=status.HTTP_201_CREATED)
#       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserCreateView(generics.CreateAPIView):
   serializer_class = UserSerializers
   
class UserAuthTokenView(ObtainAuthToken):
   serializer_class = AuthTokenSerializer