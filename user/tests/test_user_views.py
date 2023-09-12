"""
testing for user api views

"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status


CREATE_USER_URLS= reverse('user:create')
TOKEN_URL = reverse('user:token')
def create(**params):
   # create and return new user 
   return get_user_model().objects.create_user(**params)

pyload = {
   'email': 'user@example.com',
   'name': 'user',
   'password':'user1234'
}


class PublicUserAPITest(TestCase):
   # testing the public features of user api 
   def setUP(self):
      self.client = APIClient()
      
   def test_user_create(self):
      # testing creating a user successful 
      
      res = self.client.post(CREATE_USER_URLS, pyload)
      print("=================================res+++++++++++++", res.data)
      
      self.assertEqual(res.status_code, status.HTTP_201_CREATED)
      user = get_user_model().objects.get(email=pyload['email'])
      print("=================================res+++++++++++++",user.password)
      self.assertTrue(user.password, pyload['password'])
      self.assertNotIn('password', res.data)
      
   def test_user_with_email_exist_error(self):
      # testing user with email exist or not 
      create(**pyload)
      res = self.client.post(CREATE_USER_URLS,pyload)
      
      self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
      
   def test_password_to_short_error(self):
      
      pyload={
            'email': 'user@example.com',
            'name': 'user',
            'password':'uo'
      }
      res = self.client.post(CREATE_USER_URLS,pyload)
      
      self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
      user_exist = get_user_model().objects.filter(email=pyload['email']).exists()
      self.assertFalse(user_exist)
      
   def test_create_token_for_user(self):
      """ generet token for valid user """
      
      user_details={
         "name":"user",
         "email":"user@example.com",
         "password":"user12345",
      }
      
      create(**user_details)
      
      payload ={
         "email": user_details['email'],
         "password" : user_details['password']
      }
      
      res = self.client.post(TOKEN_URL,payload)
      
      self.assertIn('token', res.data)
      self.assertEqual(res.status_code, status.HTTP_200_OK)