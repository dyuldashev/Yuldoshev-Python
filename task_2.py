"""
Answer the questions
Given bracket sequence: [((())()(())]]
Can this sequence be considered correct?
If the answer to the previous question is “no”, then what needs to be changed in it to make it correct?

Answer:
==> Can this sequence be considered correct? - No
==> To make the sequence correct, we need to fix the mismatched brackets.
We need to change the last square bracket "]"  to a closing
parenthesis ")" to match the opening parenthesis at the beginning of the
sequence.
[((())()(()))]

Algorithm for checking bracket sequence
"""


# Solve with stack
def check_brackets(brackets):
    try:
        result = []  # Stack to store opening brackets
        for ele in brackets:
            if len(result) == 0:
                result.append(ele)
            elif (result[-1] == "(" and ele == ')') or (result[-1] == "[" and ele == "]"):
                result.pop()
            else:
                result.append(ele)

        if len(result) == 0:
            print("Brackets are correct")
        else:
            print("Mistakes list: ", result)
    except Exception as e:
        print("Error:", e)

def main():
    while True:
        try:
            brackets = input("Enter your brackets sequence: ")
            if not brackets:
                brackets = input("Please enter brackets sequence: ")
            try:
                check_brackets(brackets)
            except Exception as e:
                print("Unexpected Error:", e)
            choice = input("Do you want to enter more data? (yes/no): ")
            if choice.lower() != "yes":
                break  # If the user doesn't want to enter more data, exit the loop
        except Exception as e:
            print("Something went wrong:", e)
def test_function():
    test_cases = [
        ("[((())()(())]]", "Mistakes list: ['[', '(', ']', ']']"),
        ("[()][()()]()", "Brackets are correct"),
        ("[(])", "Mistakes list: ['[', '(', ']', ')']"),
        ("", "Brackets are correct"),
        ("(", "Mistakes list: ['(']"),
        ("]", "Mistakes list: [']']"),
    ]

    for brackets, expected_output in test_cases:
        print("\nTesting bracket sequence:", brackets)
        print("Expected Output:", expected_output)
        try:
            check_brackets(brackets)
        except Exception as e:
            print("Unexpected Error:", e)




if __name__ == "__main__":
    test_function()
    print("Test your sample!")
    main()
