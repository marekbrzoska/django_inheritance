from django.utils import unittest
from models import DeadOrAliveParrot, DeadOrAliveLivingObject


class ParrotsUnitTest(unittest.TestCase):
    def test_dead_or_alive_parrot(self):
        self.assertEqual(str(type(DeadOrAliveParrot.born)), "<class 'django.db.models.fields.BooleanField'>", 
            "Type of DeadOrAliveParrot's born field is not BooleanField")
        
    def test_dead_or_alive_living_object(self):
        print str(type(DeadOrAliveLivingObject.born))
        self.assertEqual(str(type(DeadOrAliveLivingObject.born)), "<class 'django.db.models.fields.BooleanField'>", 
            "Type of DeadOrAliveLivingObject's born field is not BooleanField")
