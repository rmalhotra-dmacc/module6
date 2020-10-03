"""
Author: Rajiv Malhotra
Program: validate_input_in_functions.py
Date: 10/03/20

Program takes a test_name, test_score, and invalid_message that validates the test_score,
then prints valid input as 'Test name: ##'.
"""


def score_input(test_name, test_score=0, invalid_message='Invalid test score, try again!'):
    """
    Function that accepts params and returns a string
    :param test_name: The name of a test exam
    :param test_score: A value between 0 and 100 representing a test score
    :param invalid_message: Message displayed when an invalid score is provided
    :return: formatted string with test name and test score.
    """
    # return { test_name: test_score}
    return "{}: {}".format(test_name, test_score)


if __name__ == '__main__':
    print(score_input("test1", 85))
