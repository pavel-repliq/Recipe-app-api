# simple tests

from django.test import SimpleTestCase

from . import calc

class CalcTest(SimpleTestCase):
   # test the calc module 
   
   def test_add_numbers(self):
      # test for adding numbers together 
      re = calc.add(5,6)
      
      self.assertEqual(re,11)
      
   def test_subtract_numbers(self):
      # test for subtracting numbers 
      
      re= calc.subtract(10,15)
      
      self.assertEqual(re,5)