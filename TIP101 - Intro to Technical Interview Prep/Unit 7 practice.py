"""
# Unit 7: Divide & Conquer & Recursion
# Session 1: Recursion
"""
"""Problem Set Version 1
Problem 1: Hello Hello
A recursive function is a function that calls itself within the body of the function.
Step 1: Copy the recursive function repeat_hello() into Replit and run it.
Step 2: Then create another function repeat_hello_iterative() that produces the same output without using recursion.

Compare your iterative (non-recursive) solution to the recursive solution provided. What is similar? What is different?"""
def repeat_hello(n):
  if n > 0:
    print("Hello")
    repeat_hello(n - 1)

repeat_hello(5)
print()

def repeat_hello_iterative(n):
  i = 0 
  while i < n:
    print("Hello")
    i += 1

repeat_hello_iterative(5)
print()

"""Problem 2: Factorial Cases
Given the base case and recursive case, write a function factorial() that returns the factorial of a non-negative integer n. The factorial of a number is the product of all numbers between 1 and n.
Base Case: The smallest number we can find a factorial of is 0. By definition, the factorial of 0 is 1.
Recursive Case: We can restate the problem to say that the factorial of n is n * the factorial of n-1."""
def factorial(n):
  if n == 1 or n == 0:
    return 1
  else: 
    return n * factorial(n - 1)

n = 5
print(f"The factorial of {n} is:", factorial(n))
print()

"""Problem 3: Recursive Sum
Without using the built-in sum() function, write a function sum_list() that calculates the sum of all values in a list recursively.

What is the time complexity of this function? What is the space complexity?"""
def sum_list(lst):
  if not lst:
    return 0
  return lst[0] + sum_list(lst[1:])

lst = [1, 2, 3, 4, 5, 6]
print(sum_list(lst))
print()

"""Problem 4: Recursive Power of 2
Given an integer n, return True if n is a power of two. Otherwise, return `False``. An integer n is a power of two if there exists an integer x such that n == 2ˣ.

Solve the problem recursively. What is the time complexity of this function? What is the space complexity?"""
def is_power_of_two(n):
  if n == 1:
    return True
  if n <= 0 or n % 2 != 0:
    return False
  return is_power_of_two(n / 2)

print(is_power_of_two(8))
print()

"""Problem 5: Binary Search I
Binary search is a searching algorithm that allows us to efficiently find the index of a given value within a sorted list. Given the pseudo code for binary search below, implement an iterative (non-recursive) implementation of binary search. There is also a recursive alternative that we’ll cover in the session 2 problem set!

Evaluate the time and space complexity of your implementation."""
def binary_search(lst, target):
  # Initialize a left pointer to the 0th index in the list
  left = 0
  # Initialize a right pointer to the last index in the list
  right = len(lst) - 1

  # While left pointer is less than right pointer:
  while left <= right:
    # Find the middle index of the array
    middle =  (left + right) // 2 
    #print("middle:", middle)

    # If the value at the middle index is the target value:
    if lst[middle] == target:
      # Return the middle index
      return middle
    # Else if the value at the middle index is less than our target value:
    elif lst[middle] < target:
      # Update pointer(s) to only search right half of the list in next loop iteration
      left = middle + 1
    # Else
    else:
      # Update pointer(s) to only search left half of the list in next loop iteration
      right = middle - 1
  # If we search whole list and haven't found target value, return -1
  if left > right:
    return -1

lst = [1, 3, 5, 7, 9, 11, 13, 15]
target = 11
print(binary_search(lst, target))
print()

"""Binary Search II with Recursion"""
def binary_search(arr, target, left, right):
  # target not in list
  if left > right:
    return -1

  middle = left + (right - left) // 2

  # target found at index middle
  if arr[middle] == target:
    print("middle found", middle)
    return middle

  elif arr[middle] > target:
    print("mid greater than target", middle)
    return binary_search(arr, target, left, middle - 1)

  else:
    print("mid less than target", middle)
    return binary_search(arr, target, middle + 1, right)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
result = binary_search(arr, target, 0, len(arr) - 1)
print(result)
print()

"""  Problem 6: Backwards Binary Search
Generally binary search returns the index of the first occurrence of the target in the list. Write an updated version of binary search find_last() that, given a list that may contain duplicates, returns the index of the last occurrence of target.

Evaluate the time and space complexity of your function."""

def find_last(lst, target):
  # base case - return -1 if list is empty
  if not lst:
    return -1

  # initialize left and right pointer 
  left = 0
  right = len(lst) - 1

  # while left pointer is less than right pointer:
  while left <= right:
    # find the middle index of the array
    middle =  (left + right) // 2 

    # if the value at the middle index is the target value:
    if lst[middle] == target:
      # if this is the last occurence of middle
      if lst[middle] == len(lst) - 1 or lst[middle + 1] > target:
        # Return the middle index
        return middle
      else:
        left = middle + 1
    # Else if the value at the middle index is less than our target value:
    elif lst[middle] < target:
      # Update pointer(s) to only search right half of the list in next loop iteration
      left = middle + 1
    # Else
    else:
      # Update pointer(s) to only search left half of the list in next loop iteration
      right = middle - 1
  # If we search whole list and haven't found target value, return -1
  return -1

lst = [1, 3, 5, 7, 9, 11, 11, 11, 13, 15]
target = 11
print("Backwards Binary Search:", find_last(lst, target))
print()

"""Problem 7: Find Floor
Given a sorted list of integers and a value x, return the index of the floor of x. The floor of x is the largest element in the array smaller than or equal to x. If there is no floor of x, return -1.
Evaluate the time and space complexity of your function."""

def find_floor(lst, x):
  if  not lst:
    return -1

  left = 0
  right = len(lst) - 1
  floor_index = -1

  while left <= right:
    mid = (left + right) // 2
    
    if lst[mid] == x:
      return mid

    elif lst[mid] < x:
      floor_index = mid
      left = mid + 1

    else:
      right = mid - 1
  return floor_index
      
lst = [1, 2, 8, 10, 11, 12, 19]
x = 5
print(find_floor(lst, x))
# Expected Output: 1
# 2 is the largest element in the list that is less than or equal to 5. 2 has index 1 in the list.
print()

"""Problem Set Version 2
Problem 1: Counting Down
A recursive function is a function that calls itself within the body of the function.
Step 1: Copy this code into Replit and run it.
Step 2: Then create another function countdown_iterative() that produces the same output without using recursion.
Compare your iterative (non-recursive) solution to the recursive solution provided. What is similar? What is different?"""

def countdown(n):
  if n > 0:
    print(n)
    countdown(n - 1)

countdown(5)
print()

def countdown_iterative(n):
  while n > 0:
    print(n)
    n -= 1
    
countdown_iterative(5)
print()

"""Problem 2: Fibonacci Cases
Given the base case and recursive case, write a function fibonacci() that returns the nth number in the fibonacci sequence. The Fibonacci sequence is a mathematical sequence of numbers where each number is the sum of the two preceding numbers.

Base Cases: Because Fibonacci numbers are defined by adding the two previous numbers in the sequence, the first two Fibonacci numbers are pre-defined. By definition, the 0th Fibonacci number is 0, and the 1st Fibonacci number is 1.

Recursive Case: The nth Fibonacci number is the n-1th Fibonacci number + the n-2th Fibonacci number."""

def fibonacci(n):
  if n < 0:
    return "Incorrect output"

  elif n == 0:
    return 0
  elif n == 1 or n == 2:
    return 1
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6)) # Expected Output: 8
# Explanation: The 6th Fibonacci number is 8. The 5th Fibonacci number is 5 and the 4th Fibonacci
# number is 3. 5 + 3 = 8.
print()

"""Problem 3: Recursive Product
Write a function list_product() that calculates the product of all values in a list recursively.
What is the time complexity of this function? What is the space complexity?"""

def list_product(lst):
  if not lst:
    return 1
  return lst[0] * list_product(lst[1:])

lst =  [1, 2, 3, 4, 5]
print(list_product(lst)) # Expected Output: 120
# Explanation: 1 * 2 * 3 * 4 * 5 = 120
print()

"""Problem 4: Recursive Power of 4
Given an integer n, return True if n is a power of four. Otherwise, return False.
An integer n is a power of four if there exists an integer x such that n == 4ˣ.
Solve the problem recursively. What is the time complexity of this function? What is the space complexity?"""

def is_power_of_four(n):
  if n == 1:
    return True

  if n <= 0 or n % 4 != 0:
    return False
  return is_power_of_four(n / 4)

n = 100
print(is_power_of_four(n))
print()

"""Problem 5: Binary Search II
Binary search is a searching algorithm that allows us to efficiently find the index of a given value within a sorted list. Given the recursive solution for binary search below, implement an iterative (non-recursive) implementation of binary search.

Evaluate the time and space complexity of your implementation."""
def binary_search_recursive(arr, target, left, right):
  if left > right:
      return -1  # Base case: target not found within bounds

  # find middle index of list
  mid = (left + right) // 2

  # If the middle element is the target, return its index
  if arr[mid] == target:
      return mid
  # If the target is less than the middle element, search the left half
  elif arr[mid] > target:
      return binary_search_recursive(arr, target, left, mid - 1)
  # If the target is greater than the middle element, search the right half
  else:
      return binary_search_recursive(arr, target, mid + 1, right)

arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 11
left = 0
right = len(arr) - 1
print("Recursive binary search")
print(binary_search_recursive(arr, target, left, right))
print()

def binary_search_iterative(arr, target):
  if target not in arr:
    return -1
    
  left = 0
  right = len(arr) - 1
  while left < right:
    mid = (left + right) // 2

    if arr[mid] == target:
      return mid

    elif arr[mid] < target:
      left = mid + 1
    else:
      right = mid - 1

print("Iterative binary search")
print(binary_search_iterative(arr, target))
print()

"""Problem 6: Find Ceiling
Given a sorted list of integers and a value x, return the index of the ceiling of x. The ceiling of x is the smallest element in the array larger than or equal to x. If there is no ceiling of x, return -1.
Evaluate the time and space complexity of your function."""

def find_ceiling(lst, x):
  if not lst:
    return -1

  left = 0
  right = len(lst) - 1
  ceiling_index = -1
  while left <= right:
    mid = (left + right) // 2
    if lst[mid] == x:
      return mid
      
    elif lst[mid] < x:
      left = mid + 1
    else:
      ceiling_index = mid
      right = mid - 1
  return ceiling_index

lst = [1, 2, 8, 10, 11, 12, 19]
x = 5
print(find_ceiling(lst, x)) # Expected Output: 2
# 8 is the largest element in the list that is greater than or equal to 5. 
# 8 has index 2 in the list.
print()

"""Problem 7: Ternary Search
Ternary search is a search algorithm that, similar to binary search, works on a sorted array. However, instead of dividing the search interval into two halves (as in binary search), ternary search divides it into three parts, using two midpoints. This reduces the problem size to approximately one-third in each step, rather than one-half.

Given the pseudocode for ternary_search() below, implement the function. Evaluate the time and space complexity of your solution"""

def ternary_search(lst, target):
  # Divide the array into three parts using two mid points (mid1 and mid2).
  left = 0
  right = len(lst) - 1

  # While the lower bound is less than or equal to the upper bound:
  while left <= right:
    mid1 = left + (right - left) // 3
    mid2 = right - (right - left) // 3
    # Compare the target value with the values at mid1 and mid2:
        # If the target value matches mid1 or mid2
          # the search is successful.
    if lst[mid1] == target:
      return mid1

    if lst[mid2] == target:
      return mid2
      
    # If the target is less than the value at mid1
      # search between the lower bound and mid1 - 1.
    if target < lst[mid1]:
      right = mid1 - 1
    elif target > lst[mid2]:
      left = mid2 + 1
    # If the target is between mid1 and mid2
      # search between mid1 + 1 and mid2 - 1.
    else:
      left = mid1 + 1
      right = mid2 - 1
    # If the target is greater than the value at mid2
      # search between mid2 + 1 and the upper bound.
  # Return -1, indicating the target is not in the array.
  return -1

lst = [1, 3, 5, 7, 9, 11, 13, 15]
target = 11
print("Ternary search")
print(ternary_search(lst, target)) # Expected Output: 5
# Explanation: 11 has index 5 in the list
print()

"""Problem Set Version 3
Problem 1: In The Stars
A recursive function is a function that calls itself within the body of the function.

Step 1: Copy the recursive function insert_stars() into Replit and run it.

Step 2: Then create another function insert_stars_iterative() that produces the same output without using recursion or the built-in join() method.

Compare your iterative (non-recursive) solution to the recursive solution provided. What is similar? What is different?"""

def insert_stars(s):
    # If the string is empty or has only one character, return it as is
    if len(s) <= 1:
        return s
    # Otherwise, insert '*' between the first character and the rest, then recurse
    else:
        return s[0] + '*' + insert_stars(s[1:])

print(insert_stars('abc'))

def insert_stars_iterative(s):
  new_s = ''
  for i in s:
    new_s += i + '*'
  return new_s[:-1]
print(insert_stars_iterative('abc'))
print()

"""Problem 2: String Length Cases
Given the base case and recursive case, write a recursive function string_length() that returns the length of a string s without using the built-in len() function.

Base Case: An empty string should have size 0.

Recursive Case: We can restate the problem to say that the string length is 1 + the length of s[1:]."""

def string_length(s):
  if not s:
    return 0
  return 1 + string_length(s[1:])
    
s = 'abc'
print(string_length(s))
# Input: 'abc' # Expected Output: 3
print()

"""Problem 3: Recursive Digits Sum
Given a non-negative integer n, write a function sum_digits() that calculates and returns the sum of its digits recursively.

Evaluate the time and space complexity of your solution."""

def sum_digits(n):
  if n == 0:
    return 0
  return (n % 10) + sum_digits(n // 10)

n = 523
print(sum_digits(n))
print()
# Input: 523 # Expected Output: 10
# Time and Space complexity is O(log_10 n)

"""Problem 4: Recursive Count 7s
Given a non-negative integer n, write a recursive function count_sevens() that returns the count of the occurrences of 7 as a digit.

Evaluate the time and space complexity of your solution."""

def count_sevens(n):
  if n == 0:
    return 0

  if n % 10 == 7:
    return 1 + count_sevens(n // 10)
  return count_sevens(n // 10)

print(count_sevens(727))
print()
# Example Input: 727 # Expected Output: 2
# Explanation: 2 digits with value 7 in the number 727

"""Problem 5: Binary Search III
Binary search is a searching algorithm that allows us to efficiently find the index of a given value within a sorted list. Given the pseudo code for binary search below, implement an iterative (non-recursive) implementation of binary search that returns True if the given target is in the list and False otherwise. There is also a recursive alternative that we’ll cover in the session 2 problem set!

Evaluate the time and space complexity of your implementation."""

def binary_search(lst, target):
  # Initialize a left pointer to the 0th index in the list
  # Initialize a right pointer to the last index in the list
  left = 0
  right = len(lst) - 1

  # While left pointer is less than right pointer:
    # Find the middle index of the array
  while left <= right:
    mid = (left + right) // 2

    # If the middle value is the target value, return True
    if lst[mid] == target:
      return True
    # If the middle value is smaller than the target value, search the right half of the list
    elif lst[mid] < target:
      left = mid + 1
    # If the middle value is greater than the target value, search the left half of the list
    else:
      right = mid - 1

  # Return False if the target element has not been found
  return False

target = 11
lst = [1, 3, 5, 7, 9, 11, 13, 15]
print(binary_search(lst, target)) # Expected Output: True
print()

"""Problem 6: Find Missing
Given a sorted list of integers nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the list.

Your solution must have O(log n) time complexity."""

def find_missing(nums):
  left = 0
  right = len(nums)

  while left < right:
    mid = left + (right - left) // 2

    if nums[mid] > mid:
      right = mid
    else:
      left = mid + 1

  return left

nums = [0,1,3]
print(find_missing(nums))
# Example Input: nums = [0,1,3] # Expected Output: 2
print()

"""Problem 7: Square Root
Given a positive number, return the square root of it. If the number is not a perfect square, return the floor of its square root."""
def sqrt_helper(n, low, high):
  # Base case: if low exceeds high, we've found our answer
  if low > high:
      return high

  # Calculate mid point
  mid = (low + high) // 2

  # If mid * mid is exactly x, we've found the square root
  if mid * mid == n:
      return mid
  # If mid * mid is less than x, search in the upper half
  elif mid * mid < n:
      # Check if (mid + 1) * (mid + 1) exceeds x
      if (mid + 1) * (mid + 1) > n:
          return mid  # mid is the floor of the square root
      return sqrt_helper(n, mid + 1, high)
  # If mid * mid is greater than x, search in the lower half
  else:
      return sqrt_helper(n, low, mid - 1)
    
def sqrt(n):
  # Handle base cases
  if n == 0 or n == 1:
      return n
  # Start the recursive search
  return sqrt_helper(n, 1, n)

print(sqrt(8))
# Input: 8 # Expected Output: 2
print()


print("Search Algorithms")
"""
Unit 7 - Session 2: Search Algorithms
"""
"""Problem Set Version 1
Problem 1: Neatly Nested
Given a string, return True if it is a nesting of zero or more pairs of parentheses. Return False otherwise. A valid pair of parentheses is defined as (). The input string will only contain the characters ( or ). Your solution must be recursive.

Evaluate the time and space complexity of your solution."""
def is_nested(s):
  # Base cases
  if len(s) == 0:
      return True
  if len(s) == 1:
      return False

  # Check if the first and last characters form a pair
  if s[0] == '(' and s[-1] == ')':
      # Recursive case: check the substring without the outer parentheses
      return is_nested(s[1:-1])
  else:
      return False

paren_s = "()(!"
print(is_nested(paren_s))
print()

"""Problem 2: How Many 1s
Given a sorted list of integers containing only 0s and 1s, count the total number of 1’s in the array in O(log n) time."""
def count_ones_recursive(lst):
  if not lst:
    return 0
  return (( 1 if lst[0]==1 else 0) + count_ones_recursive(lst[1:]))

def count_ones(lst):
  low, high = 0, len(lst) - 1
  first_one_index = -1
  
  while low <= high:
    mid = low + (high - low) // 2

    if lst[mid] == 1:
      first_one_index = mid
      high = mid - 1
    else:
      low = mid + 1

  if first_one_index == -1:
    return 0

  return len(lst) - first_one_index
      
print(count_ones([0, 0, 0, 1, 1, 1, 1]))  # Expected Output: 4
print(count_ones([0, 0, 0, 0, 0, 0, 1]))  # Expected Output: 1
print(count_ones([0, 0, 0, 0, 0, 0, 0]))  # Expected Output: 0
print(count_ones([1, 1, 1, 1, 1, 1, 1]))  # Expected Output: 7
print(count_ones([]))                     # Expected Output: 0
print()

"""Problem 3: Binary Search IV
Thus far, we’ve mostly been using an iterative implementation of the binary search algorithm. Recursive implementations of binary search are also very common. Implement binary_search() recursively."""
def binary_search(nums, target):
  return binary_search_helper(nums, target, 0, len(nums) - 1)

def binary_search_helper(nums, target, low, high):
  while low <= high:
    mid = low + ((high - low)) // 2
    if nums[mid] == target:
      return mid
    elif nums[mid] > target:
      return binary_search_helper(nums, target, low, mid - 1)
    elif nums[mid] < target:
      return binary_search_helper(nums, target, mid + 1, high)
  return -1

nums = [1, 3, 5, 7, 9, 11, 13, 15]
target = 11
nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target2 = 5
print(binary_search(nums, target))   # Output: 5
print(binary_search(nums2, target2)) # Output: 4
print()

"""Problem 4: Count Rotations
You are given a circularly sorted list of integers. A circularly sorted list of integers is a sorted list whose elements have then been rotated some number of times such that the last element of the array becomes the first element of the array. Write a function count_rotations() that returns the total number of times the array is rotated. Assume there are no duplicates in the array."""

def count_rotations(nums):
  if not nums:
    return 0

  left = 0
  right = len(nums) - 1

  # if the array is not rotated at all
  if nums[left] <= nums[right]:
    return 0

  while left <= right:
    # if there are only two elements left, the right one is smallest
    if left + 1 == right:
      return right

    mid = (left + right) // 2

    # If mid element is smaller than its previous element,
    # mid is the smallest element and mid is the rotation count
    if nums[mid] < nums[mid - 1]:
      return mid
      
    # If mid element is smaller than last element, then the minimum 
    # element lies in left half
    if nums[mid] < nums[right]:
      right = mid - 1

    # else, the minimum element lies in the right 
    else:
      left = mid + 1
  return 0
    
nums = [8, 9, 10, 2, 5, 6]
print(count_rotations(nums))
print()
# Example Input: [8, 9, 10, 2, 5, 6]
# Expected Output: 3
# Explanation: Array is rotated 3 times:
  # Sorted Array: [2, 5, 6, 8, 9, 10]
  # First Rotation: [10, 2, 5, 6, 8, 9]
  # Second Rotation: [9, 10, 2, 5, 6, 8]
  # Third Rotation: [8, 9, 10, 2, 5, 6]

"""Problem 5: Merge Sort I
Merge sort is a sorting algorithm that takes in an unsorted list and returns a sorted list in O(n log n) time which is faster than many other sorting algorithms that have O(n²) time complexity. It uses a divide and conquer approach.

Merge sort works by using a divide and conquer approach: it divides the array into two halves until each sublist contains only a single element, then it recursively sorts each sublist, and merges the sorted sublists into a sorted array.

Given the pseudo-code and helper function merge() below, implement the merge_sort() function."""

# Helper function: Merges two sorted lists into one sorted list
def merge(left, right):
  result = [] # List to store the merged result
  i = j = 0 # Pointers to iterate over left and right input arrays

  # Compare elements from left and right halves of the list and add them to the
  # result list in the correct order
  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
        result.append(left[i])
        i += 1
    else:
        result.append(right[j])
        j += 1
  # Add any remaining elements from the left half to the result list
  while i < len(left):
      result.append(left[i])
      i += 1

  # Add any remaining elements from the right half to the result list
  while j < len(right):
      result.append(right[j])
      j += 1

  return result

def merge_sort(lst):
  if len(lst) <= 1:
    return lst

  mid = len(lst) // 2
  left_half = lst[:mid]
  right_half = lst[mid:]

  sorted_left = merge_sort(left_half)
  sorted_right = merge_sort(right_half)

  return merge(sorted_left, sorted_right)

lst = [5,3,4,2,1]
sorted_lst = merge_sort(lst)
print("Sorted array using merge sort:", sorted_lst)
print()
# Example Input: [5,3,4,2,1]
# Expected Output: [1,2,3,4,5]

"""Problem 6: Circle Search
Given a circularly sorted list of integers, return the index of a given target. Assume there are no duplicates in the list."""

def search_circular_list(nums, target):
  if not nums:
    return -1

  left = 0
  right = len(nums) - 1

  while left <= right:
    mid = left + ((right - left)) // 2
    
    if nums[mid] == target:
      return mid

    # check if the left half is sorted
    if nums[left] <= nums[mid]:
      # if target is in the left half
      if nums[left] <= target < nums[mid]:
        right = mid - 1
      else:
        left = mid + 1
    # right half must be sorted
    else:
      # if target is in the right half
      if nums[mid] < target <= nums[right]:
        left = mid + 1
      else:
        right = mid - 1
  # if target is not found, return -1
  return -1

nums = [8, 9, 10, 2, 5, 6]
target = 10
print(search_circular_list(nums, target))
print()
# Example Input: nums = [8, 9, 10, 2, 5, 6], target = 10
# Expected Output: 2
# Explanation: 10 is at index 2 in the list

"""Problem Set Version 2
Problem 1: Substring Search
Given two strings s and sub, write a function count_substring() that returns the number of times the substring sub occurs in s. Occurrences should not overlap. A substring is a sequence of adjacent characters within a larger string.

Your solution must be recursive.

Evaluate the time complexity of your solution."""
def count_substring(s, sub):
  # Base case: if s is shorter than sub, no occurrences are possible
  if len(s) < len(sub) or not sub:
    return 0

  # Check if s starts with sub
  if s.startswith(sub):
      # If yes, count this occurrence and recursively check the rest of s
      return 1 + count_substring(s[len(sub):], sub)
  else:
      # If no, recursively check the rest of s
      return count_substring(s[1:], sub)

# Test the function
def test_count_substring():
  test_cases = [
      ("banana", "ana"),
      ("hello world", "l"),
      ("aaaaa", "aa"),
      ("abcabcabc", "abc"),
      ("mississippi", "issi"),
      ("", "abc"),
      ("abc", ""),
      ("abcabcabcabc", "abcabc")
  ]

  for s, sub in test_cases:
      result = count_substring(s, sub)
      print(f"String: '{s}', Substring: '{sub}', Occurrences: {result}")

# Run the tests
test_count_substring()
print()

"""Problem 2: How Many 0s (Iterative)
Given a sorted list of integers containing only 0s and 1s, count the total number of 0’s in the array in O(log n) time."""

def count_zeroes_iter(lst):
  # base case: if list is empty, return 0
  if not lst:
    return 0
    
  # two pointer pointing to the start and end of list
  low, high = 0, len(lst) - 1

  # if the last element is 0, all elements are 0
  if lst[high] == 0:
    return len(lst)

  # using binary search loop through list
  while low <= high:
    mid = low + ((high - low)) // 2

    if lst[mid] == 1:
      high = mid - 1
    elif lst[mid] == 0:
      if mid == len(lst) - 1 or lst[mid + 1] == 1:
        return mid + 1
      else:
        low = mid + 1

  return 0

# Test cases
print("How Many 0s (Iterative)")
print(count_zeroes_iter([0, 0, 0, 0, 1, 1, 1]))  # Expected Output: 4
print(count_zeroes_iter([0, 0, 0, 1, 1]))        # Expected Output: 3
print(count_zeroes_iter([0, 0, 0, 0, 0, 0, 1]))  # Expected Output: 6
print(count_zeroes_iter([0, 0, 0, 0, 0, 0, 0]))  # Expected Output: 7
print(count_zeroes_iter([1, 1, 1, 1, 1]))        # Expected Output: 0
print(count_zeroes_iter([]))                     # Expected Output: 0
print()

"""Problem 3: How Many 0s (Recursive)
Implement count_zeroes() recursively."""

def count_zeroes_search(lst, low, high):
  # base case
  if low > high:
    return 0

  if lst[high] == 0:
    return high - low + 1

  if lst[low] == 1:
    return 0

  # calculate mid point
  mid = low + ((high - low)) // 2

  # recursive case
  if lst[mid] == 0:
    if mid == high or lst[mid + 1] == 1:
      return mid + 1
    else:
      return count_zeroes_search(lst, mid + 1, high)
  else: # lst[mid] == 1
    return count_zeroes_search(lst, low, mid - 1)

# wrapper function to initialize recursion
def count_zeroes_recur(lst):
  if not lst:
    return 0
  return count_zeroes_search(lst, 0, len(lst) - 1)

# Test cases
print("How Many 0s (Recursive)")
print(count_zeroes_recur([0, 0, 0, 0, 1, 1, 1]))  # Expected Output: 4
print(count_zeroes_recur([0, 0, 0, 1, 1]))        # Expected Output: 3
print(count_zeroes_recur([0, 0, 0, 0, 0, 0, 1]))  # Expected Output: 6
print(count_zeroes_recur([0, 0, 0, 1, 1, 1, 1]))  # Expected Output: 3
print(count_zeroes_recur([0, 0, 0, 0, 0, 0, 0]))  # Expected Output: 7
print(count_zeroes_recur([1, 1, 1, 1, 1]))        # Expected Output: 0
print(count_zeroes_recur([]))                     # Expected Output: 0
print()

"""Problem 4: Special Numbers
You are given a sorted list of non-negative integers nums. nums is considered special if there exists a number x such that there are exactly x numbers in nums that are greater than or equal to x.

Notice that x does not have to be an element in nums.

Return x if the array is special, otherwise, return -1. It can be proven that if nums is special, the value for x is unique."""

def is_special(nums):
  pass

# Example Input: nums = [3,5] # Expected Output: 2
# Explanation: There are 2 values (3 and 5) that are greater than or equal to 2.

# """
# Assignment Questions
# 1. Mystery Time Complexity
# What is the time complexity of the following function? lst is a sorted list of integers. target is an integer. Assume n represents the length of lst."""

# def mystery_function(lst, target):
#   left, right = 0, len(lst) - 1
#   while left <= right:
#     mid = (left + right) // 2
#     mid_value = lst[mid]

#     if mid_value == target:
#       return mid
#     elif mid_value < target:
#       left = mid + 1
#     else:
#       right = mid - 1
#   return -1
# # answer: O(log n)

# """2. Recursive Prediction
# Given the following code, what is the value of output?"""
# def mystery_function(n):
#   if n == 0:
#     return 0

#   if n % 2==1:
#     return 2 + mystery_function(n-1)
#   else:
#     return 3 + mystery_function(n-1)

# output = mystery_function(2) # 5

# """3. Base Case Scenario
# Which of the following best describes the base case of the following recursive algorithm:"""
# def sequence(n):
#   if n == 1 or n == 2:
#     return 1
#   else:
#     return sequence(sequence(n - 1)) + sequence(n - sequence(n-1))
# # answer: n == 1 or n == 2

# """4. Predict the Recursive Call
# Given the following code, what is the value of output?"""
# def recursive_function(a, b):
#   if b < 0:
#     return -1 * recursive_function(a, -b)
#   if b == 0:
#     return 0
#   return a + recursive_function(a, b-1)

# output = recursive_function(3, 2) # 6

# """5. String Search
# Given an alphabetically sorted list of strings names and a string val, return the index of the first occurence of val in O(log n) time. If val is not a name in names, return -1. names = {'Amal', 'Beric', 'Florin', 'Julie', 'Qin'], val = 'Julie'. Output: 3."""
# def find_val(names, val):
#     left = 0
#     right = len(names) - 1

#     while left <= right:
#         mid = (left + right) // 2

#         if names[mid] == val:
#             return mid
#         elif names[mid] < val:
#             left = mid + 1
#         else:
#             right = mid - 1

#     return -1

# # Test the function
# names = ['Amal', 'Beric', 'Florin', 'Julie', 'Qin']
# val = 'Julie'
# result = find_val(names, val)
# print(result)  # Expected output: 3

# # Test with a value not in the list
# val = 'Tabrez'
# result = find_val(names, val)
# print(result)  # Expected output: -1

# # Test with a value at the beginning of the list
# val = 'Amal'
# result = find_val(names, val)
# print(result)  # Expected output: 0

# # Test with a value at the end of the list
# val = 'Qin'
# result = find_val(names, val)
# print(result)  # Expected output: 4

# """6. Power Function
# Given two integers, x and n, where n >= 0, write a function power() that recursively computes and returns x^n"""
# def power(x, n):
#     # Base cases
#     if n == 0:
#         return 1
#     if n == 1:
#         return x

#     # Recursive case
#     # If n is even
#     if n % 2 == 0:
#         half_power = power(x, n // 2)
#         return half_power * half_power
#     # If n is odd
#     else:
#         return x * power(x, n - 1)

# print(power(2, 3))  # Expected output: 8
# print(power(3, 4))  # Expected output: 81
# print(power(5, 0))  # Expected output: 1
# print(power(7, 1))  # Expected output: 7

# """7. Find the Domain
# Given a list of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value. Return the result as a list in the form [start_position, end_position]. If target is not found in the list, return [-1, 1]. Your solution must have 0(log n) time complexity. Inputs: nums = [5,7,7,8,8,10], target = 8. Output: [3, 4]."""

# def search(nums, target):
#     def binary_search_left(nums, target):
#         left, right = 0, len(nums) - 1
#         while left <= right:
#             mid = (left + right) // 2
#             if nums[mid] == target:
#                 if mid == 0 or nums[mid-1] < target:
#                     return mid
#                 right = mid - 1
#             elif nums[mid] < target:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#         return -1

#     def binary_search_right(nums, target):
#         left, right = 0, len(nums) - 1
#         while left <= right:
#             mid = (left + right) // 2
#             if nums[mid] == target:
#                 if mid == len(nums) - 1 or nums[mid+1] > target:
#                     return mid
#                 left = mid + 1
#             elif nums[mid] < target:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#         return -1

#     left = binary_search_left(nums, target)
#     if left == -1:
#         return [-1, -1]
#     right = binary_search_right(nums, target)
#     return [left, right]


# nums = [5,7,7,8,8,10]
# target = 8
# print(search(nums, target))  # Expected output: [3, 4]

# target = 6
# print(search(nums, target))  # Expected output: [-1, -1]
