import unittest
from more_functions import string_functions


class MyTestCase(unittest.TestCase):
    def test_score_input_test_name(self):
        self.assertEqual("Python!Python!Python!Python!", string_functions.multiply_string("Python!", 4))


if __name__ == '__main__':
    unittest.main()
