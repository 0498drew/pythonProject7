import unittest

from games import Games

class  Test(unittest.TestCase):
    def setUp(self):
        self.games = Games()

    def test_games_mul_method_return_correct_result(self):
        result = self.games.mul(2, 2)
        self.assertEqual(4, result)
    def test_games_return_error_massege_if_both_agrs_are_not_num(self):
        self.assertRaises(ValueError, self.games.mul, 'two', 'three')
    def test_games_return_error_massege_if_x_agr_is_not_num(self):
        self.assertRaises(ValueError, self.games.mul, 'two', 2)
    def test_games_return_massege_if_y_agr_is_not_num(self):
        self.assertRaises(ValueError, self.games.mul, 3, 'three')
if __name__ == '__main__':
    unittest.main()