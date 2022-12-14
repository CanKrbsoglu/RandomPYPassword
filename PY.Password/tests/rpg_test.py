import unittest

from source import rpg

class rpg_test(unittest.TestCase):
    def test_random_password_generator(self):
        result_password = len(rpg.random_password_generator())

        self.assertGreaterEqual(result_password, 5)
        self.assertLessEqual(result_password, 20)
