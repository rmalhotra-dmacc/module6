"""
Author: Rajiv Malhotra
Program: inner_functions_assignment.py
Date: 10/04/20

Program accepts a list of measurements for a rectangle and returns a string with perimeter and area.
"""


def measurements(rect_measure):
    """
    Function accepts a list of measurements for a rectangle and returns a string with perimeter and area
    :param rect_measure: list of measurements
    :type rect_measure:list
    :return: Formatted string with perimeter and area
    :rtype: String
    """

    def area(a_measure):
        if len(a_measure) == 1:
            return a_measure[0] * a_measure[0]
        elif len(a_measure) == 2:
            return a_measure[0] * a_measure[1]
        else:
            raise IndexError

    def perimeter(p_measure):
        if len(p_measure) == 1:
            return p_measure[0] * 4
        elif len(p_measure) == 2:
            return p_measure[0] * 2 + p_measure[1] * 2
        else:
            raise IndexError

    try:
        a_value = area(rect_measure)
        p_value = perimeter(rect_measure)
    except IndexError:
        raise IndexError
    else:
        return "Perimeter = {} Area = {}".format(p_value, a_value)


if __name__ == '__main__':
    try:
        print(measurements([2, 3]))
    except IndexError:
        print("Please enter either 1 or 2 measurements only")
