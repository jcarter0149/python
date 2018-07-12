import unittest
import sys
sys.path.append("../")
from animal import Animal
from animal import Dog


class TestAnimal(unittest.TestCase):

   @classmethod
   def setUpClass(self):
       self.bob = Dog("Bob")

   def test_animal_creation(self):

       bob = self.bob

       self.assertIsInstance(bob, Animal)
       self.assertIsInstance(bob, Animal)

   def test_animal_can_set_legs(self):
       self.bob.set_legs(6)
       self.assertEqual(self.bob.legs,6)

   def test_animal_can_set_species(self):
       self.bob.set_species('Dog')
       self.assertEqual(self.bob.species, 'Dog')

   def test_animal_can_get_species(self):
       self.bob.get_species()
       self.assertEqual(self.bob.species, 'Dog')

   def  test_animal_can_walk(self):
       self.bob.set_legs(4)
       self.bob.walk()
       self.assertEqual(self.bob.speed, .8)

   def test_animal_get_name(self):
       self.bob.name = 'Winston'
       self.assertEqual(self.bob.name, 'Winston')

if __name__=="__main__":
   unittest.main()