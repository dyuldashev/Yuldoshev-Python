"""
Make up an algorithm
If the entered number is greater than 7, then print “Hello”
If the entered name matches “John”, then output “Hello, John”, if not, then output "There is no such name"
There is a numeric array at the input, it is necessary to output array elements that are multiples of 3

"""


def is_numeric(value):
    """
    Check if the input value is numeric.
    """
    try:
        float(value)
        return True
    except ValueError:
        return False


def process_numeric_array(array):
    """
    Check if the input data is a numeric array and return array elements divisible by 3.
    If the input data is not a numeric array, return an empty list.
    """
    try:
        result = []
        for num in array:
            if is_numeric(num):
                num = float(num)
                if num % 3 == 0:
                    result.append(num)
            else:
                return None  # Indicate that input is not a numeric array
        return result
    except Exception as e:
        raise RuntimeError("Error processing numeric array") from e


def handle_input(input_data):
    """
    Handle different types of input data.
    """
    if input_data.isdigit():
        if int(input_data) > 7:
            print("Hello")
    elif input_data.isalnum():
        if input_data == "John":
            print("Hello, John")
        else:
            print("There is no such name")
    else:
        nums = [num.strip() for num in input_data.split(',')]
        result = process_numeric_array(nums)
        if result is None:
            print("Given input is not a numeric array")
        elif result:
            print(result)
        else:
            print("Given array does not contain numeric elements divisible by 3")


def main():
    print("Your data can be just a number, string or array.\n If it is an array please separate it with a comma")
    while True:
        try:
            input_data = input("Enter data: ")
            if not input_data:
                break  # If the user enters an empty string, exit the loop
            handle_input(input_data)
            choice = input("Do you want to enter more data? (yes/no): ")
            if choice.lower() != "yes":
                break  # If the user doesn't want to enter more data, exit the loop
        except Exception as e:
            print("Something went wrong:", e)


if __name__ == "__main__":
    main()
