"""
Make up an algorithm
If the entered number is greater than 7, then print “Hello”
If the entered name matches “John”, then output “Hello, John”, if not, then output "There is no such name"
There is a numeric array at the input, it is necessary to output array elements that are multiples of 3

"""


def is_numeric_arr(input_array):
    """
    Check if the input data is a numeric array and return array elements multiples of 3.
    If the input  data is not a numeric array, return False.
    """
    try:
        # Split the input string into individual elements
        nums = input_data.split(',')
        # new variable for result
        result: list = []
        for num in nums:
            if num.isnumeric():
                result.append(float(num) * 3)
            else:
                # If any element is not numeric, return False
                return False
        return result
    except Exception as e:
        # If any error occurs during processing, return False
        return False


# Get input from console
input_data = input()
try:
    # Check if the input is a digit greater than 7
    if input_data.isdigit():
        if int(input_data) > 7:
            print("Hello")
    # Check if the input is an alphabetic string
    elif input_data.isalpha():
        if input_data == "John":
            print("Hello, John")
        else:
            print("There is no such name")
    # Checking. Is the given data numeric array
    else:
        result = is_numeric_arr(input_data)
        if result:
            print(result)
        else:
            print("Given array is not numeric")
except Exception as e:
    print("Something is wrong: ", e)
