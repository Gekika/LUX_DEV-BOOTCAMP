
# TASK ONE
# Write a Python program to check whether a string is a palindrome or not using a stack.

# I declare  a stack to help me check for palindrome
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

def is_palindrome(string):
    stack = Stack()

    # Push characters onto the stack
    for char in string:
        stack.push(char)

    # Pop characters and compare with original string
    reversed_string = ""
    while not stack.is_empty():
        reversed_string += stack.pop()

    return reversed_string == string


#  I test if my function is doing
string = input("Enter a string: ")
if is_palindrome(string):
    print(f"{string} is a palindrome.")
else:
    print(f"{string} is not a palindrome.")




# TASK TWO 
# Explain the concept of list comprehension in Python with at least three examples.
