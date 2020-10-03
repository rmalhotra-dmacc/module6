"""""
Program: string_functions.py
Author: Rajiv Malhotra
Last Modified Date: 10/03/2020
 
The program will accept string message and a number n and returns the string with message printed n times
"""""


def multiply_string(message, n):
    """
    This function takes a message and number and returns the message printed n times
    :param message: string
    :param n: integer
    :return: string
    """
    try:
        #check if number is between 1 and 9
        if 1 <= n <= 9:
            return(message * n)
        else:
            print("Value of n must be between 1 and 9")
    except TypeError as err:
        print(err)


if __name__ == '__main__':
    print(multiply_string('Python!', 4))
