from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
   # Models test 
   
   def test_create_user_with_email(self):
      # test for creating user with email 
      
      email = 'user@example.com'
      password = 'user1234'
      
      user = get_user_model().objects.create_user(
         email=email,
         password=password
      )
      
      self.assertEqual(user.email, email)
      self.assertTrue(user.check_password(password))
      self.assertTrue(user.is_active)
      self.assertFalse(user.is_staff)
      self.assertFalse(user.is_superuser)
      
   def test_super_user_create_with_email(self):
      
      email = 'user@example.com'
      password = 'user1234'
      user = get_user_model().objects.create_superuser(
         email=email,
         password=password
      )
      self.assertTrue(user.is_active)
      self.assertTrue(user.is_staff, True)
      self.assertTrue(user.is_superuser)