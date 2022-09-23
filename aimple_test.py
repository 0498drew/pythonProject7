import unittest
from mycode import*

class MYFirstTest(unittest.TestCase):

def test_hello(self):
        self.assertEqual(hello_world(), 'hell world')
    def test_custon_num_list(self):
        self.assertEqual(len(create_num_list(10)), 10)
