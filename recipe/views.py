from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
)
from .models import *
from .serializers import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class RecipeCreateAndListView(GenericAPIView, CreateModelMixin, ListModelMixin):
   queryset = RecipeModel.objects.filter()
   serializer_class = RecipeSerializer
   authentication_classes = [TokenAuthentication]
   permission_classes =[IsAuthenticated]
   
   
   def get(self, request, *args, **kwargs):
      return self.list(request, *args, **kwargs)

   def post(self, request, *args, **kwargs):
      return self.create(request, *args, **kwargs)
