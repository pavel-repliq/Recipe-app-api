from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from .models import *
from .serializers import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.


class RecipeCreateAndListView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = RecipeModel.objects.filter()
    serializer_class = RecipeSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class RecipeDetailView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin):
    queryset = RecipeModel.objects.filter()
    serializer_class = RecipeDetailSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
