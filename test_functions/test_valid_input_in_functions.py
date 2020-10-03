import unittest
from more_functions import validate_input_in_functions as val_input


class MyTestCase(unittest.TestCase):
    def test_score_input_test_name(self):
        self.assertEqual("Python1!: 0", val_input.score_input("Python1!"))

    def test_score_input_test_score_valid(self):
        self.assertEqual("Python2!: 95", val_input.score_input("Python2!", 95))

    def test_score_input_test_score_below_range(self):
        self.assertEqual("Invalid test score, try again!", val_input.score_input("Python3!", -5))

    def test_score_input_test_score_above_range(self):
        self.assertEqual("Invalid test score, try again!", val_input.score_input("Python4!", 125))

    def test_test_score_non_numeric(self):
        with self.assertRaises(TypeError):
            val_input.score_input("Python5!", "Ninty")

    def test_score_input_invalid_message(self):
        self.assertEqual("Not a valid score, try again", val_input.score_input("Python6!", 105, "Not a valid score, try again"))


if __name__ == '__main__':
    unittest.main()
