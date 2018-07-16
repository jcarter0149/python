import unittest
from lootbag import Lootbag

class TestBagOLoot(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.bag = Lootbag()

    def test_can_list_toys_from_bag_for_child(self):
        toy = 'ball'
        jake_toys = self.bag.list_toys_for_child('Jake')

        self.assertIn(toy, jake_toys)

    def test_add_toy_to_bag(self):
        bag = Lootbag()
        toy = 'ball'
        self.assertEqual(bag.add_toy_to_bag(toy, 'Jake'), 'Toy added to bag')

        # toy = 'truck'
        # toy_list = self.bag.list_toys_for_child('Jake')
        # self.assertNotIn(toy, toy_list)
        # bag.add_toy_to_bag('truck', 'Jake')
        # toy_list = bag.list_toys_for_child('Jake')
        # self.assertIn(toy, toy_list)

if __name__ == '__main__':
    unittest.main()
