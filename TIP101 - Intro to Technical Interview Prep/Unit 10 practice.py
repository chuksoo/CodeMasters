"""
Session 1: Review I
*******************
Problem Set Version 1
Problem 1: Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', return True if the input string is valid and False otherwise.

An input string is valid if:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type."""
# def is_valid(s):
#   # Dictionary to hold matching pairs of brackets
#   bracket_map = {')': '(', '}': '{', ']': '['}
#   # Stack to keep track of opening brackets
#   stack = []

#   # Iterate through each character in the string
#   for char in s:
#       # If the character is a closing bracket
#       if char in bracket_map:
#           # Pop the top element from the stack if it's not empty, otherwise assign a dummy value
#           top_element = stack.pop() if stack else '#'
#           # Check if the popped element matches the corresponding opening bracket
#           if bracket_map[char] != top_element:
#               return False
#       else:
#           # If it's an opening bracket, push it onto the stack
#           stack.append(char)

#   # If the stack is empty, all brackets were matched correctly
#   return not stack


# # Case 1
# s = "()"
# print(is_valid(s)) # Expected Output: True

# # Case 2
# s = "()[]{}"
# print(is_valid(s)) # Expected Output: True

# # Case 3
# s = "(())"
# print(is_valid(s)) # Expected Output: True

# # Case 4
# s = "(]"
# print(is_valid(s)) # Expected Output: False

# # Case 5
# s = "([)]"
# print(is_valid(s)) # Expected Output: False
# print()

# class TreeNode:
#   def __init__(self, val=0, left=None, right=None):
#       self.val = val
#       self.left = left
#       self.right = right

# def mystery_function(root, val):
#   if not root:
#       return TreeNode(val)
#   if val < root.val:
#       root.left = mystery_function(root.left, val)
#   else:
#       root.right = mystery_function(root.right, val)
#   #print(root.val)
#   return root

# def print_tree(root):
#   if not root:
#       return
#   print(root.val, end=" ")
#   print_tree(root.left)
#   print_tree(root.right)

# root = TreeNode(4)
# root.left = TreeNode(2)
# root.right = TreeNode(7)
# root = mystery_function(root, 1)
# root = mystery_function(root, 3)
# print_tree(root)

import numpy as np


def conv2d(input, weight, stride=1, padding=0):
    # Get the dimensions of the input and weight matrices
    input_h, input_w = input.shape
    weight_h, weight_w = weight.shape

    # Calculate the output dimensions
    output_h = (input_h - weight_h + 2 * padding) // stride + 1
    output_w = (input_w - weight_w + 2 * padding) // stride + 1

    # Initialize the output matrix
    output = np.zeros((output_h, output_w))

    # Apply padding to the input matrix
    if padding > 0:
        input_padded = np.pad(input, pad_width=padding, mode='constant', constant_values=0)
    else:
        input_padded = input

    # Perform the convolution operation
    for i in range(0, output_h):
        for j in range(0, output_w):
            # Extract the region of the input corresponding to the current output element
            region = input_padded[i * stride:i * stride + weight_h, j * stride:j * stride + weight_w]
            # Perform element-wise multiplication and sum the results
            output[i, j] = np.sum(region * weight)

    return output


# Example usage
input = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
weight = np.array([[1, 0], [0, -1]])
print(conv2d(input, weight, stride=1, padding=0))