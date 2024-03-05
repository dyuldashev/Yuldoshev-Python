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
    result = []  # Stack to store opening brackets
    for ele in brackets:
        if len(result) == 0:
            result.append(ele)
        elif (result[-1] == "(" and ele == ')') or (result[-1] == "[" and ele == "]"):
            result.pop()
        else:
            result.append(ele)

    if len(result) == 0:
        print("Brackets are right")
    else:
        print("Mistakes list: ", result)


# The above function is not fully correct. We might be optimizing depending on a given task
brackets = input("Enter the sequence ( or ] brackets: ")
check_brackets(brackets)
