"""""
1.) Write a function is_prime() that takes in a positive integer n and returns True if it is a prime number and False otherwise. A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.

"""
def is_prime(n):
  if n < 2:
    return False
  else:
    for num in range(2, n):
      if n % num == 0:
        return False
    return True

print(is_prime(5))
print(is_prime(12))
print(is_prime(9))
print()

'''
2.)Write a function reverse_list() that takes in a list lst and returns elements of the list in reverse order. The list should be reversed in-place without using list slicing (e.g. lst[::-1]).

Instead, use the two-pointer approach, which is a common technique in which we initialize two variables (also called a pointer in this context) to track different indices or places in a list or string, then moves the pointers to point at new indices based on certain conditions. In the most common variation of the two-pointer approach, we initialize one variable to point at the beginning of a list and a second variable/pointer to point at the end of list. We then shift the pointers to move inwards through the list towards each other, until our problem is solved or the pointers reach the opposite ends of the list.
'''

def reverse_list(lst):
  start = 0
  end = len(lst) - 1
  while start < end:
    lst[start], lst[end] = lst[end], lst[start]
    start += 1
    end -= 1
  return lst

lst = [1, 2, 3, 4, 5]
print(reverse_list(lst))

def reverse_list2(lst):
  # Create a new reversed list
  reversed_lst = lst[::-1]
  # Copy the elements back into the original list
  for i in range(len(lst)):
      lst[i] = reversed_lst[i]
    
lst = [1, 2, 3, 4, 5]
print(reverse_list(lst))
print()

'''
4.)Write a function sort_list_by_parity() that takes in an integer list nums as a parameter and moves all the even integers at the beginning of the list followed by all the odd integers. The function returns any list that satisfies this condition.
'''
def sort_array_by_parity(nums):
  new_list = []
  for i in nums:
    if i % 2 == 0:
      new_list.append(i)

  for j in nums:
    if j not in new_list:
      new_list.append(j)
  return new_list

nums = [3,1,2,4]
nums2 = [0]
print("Brute force approach")
print(sort_array_by_parity(nums))
print(sort_array_by_parity(nums2))
print()

def sort_array_by_parity2(nums):
  left = 0
  right = len(nums) - 1
  while left < right:
    if nums[left] % 2 == 0:
      left += 1
    elif nums[right] % 2 != 0:
      right -= 1
    else:
      nums[left], nums[right] = nums[right], nums[left]
      left += 1
      right -= 1
  return nums

print("Two Pointer approach")
nums = [3,1,2,4,6,5]
print(sort_array_by_parity2(nums))
print()

# def sort_array_by_parity2(nums):
#   i = 0
#   j = len(nums) - 1
#   while i < j:
#       if nums[i] % 2 != 0:
#           nums[i], nums[j] = nums[j], nums[i]
#           j -= 1
#       else:
#           i += 1
#   return nums

# print("Two Pointer approach")
# nums = [3,1,2,4,6,5]
# print(sort_array_by_parity(nums))

"""
Problem 5: Palindrome
Write a function first_palindrome() that takes in a list of strings words as a parameter and returns the first palindromic string in the list. A string is palindromic if it reads the same forward and backward. If there is no such string, return an empty string
"""
def first_palindrome(words):
  for lst in words:
    left = 0
    right = len(lst) - 1
    if lst[left] != lst[right]:
        continue
    while left < right:
        if lst[left] == lst[right]:
            left += 1
            right -= 1
    if lst is None:
      return ""
    return lst


words = ["abc","car","ada","racecar","cool"]
palindrome1 = first_palindrome(words)
print(palindrome1)

words2 = ["abc","racecar","cool"]
palindrome2 = first_palindrome(words2)
print(palindrome2)

words3 = ["abc", "def", "ghi"]
palindrome3 = first_palindrome(words3)
print(palindrome3)

"""
Problem 6: Remove Duplicates with O(1)
Write a function remove_duplicates() that takes in a sorted list of integers nums as a parameter and removes the duplicates in-place such that each element appears only once. Do not allocate extra space for another array; you must do this by modifying the input list with O(1) extra memory. The function returns the new length of the list.
"""
def remove_duplicates(nums):
  if not nums:
    return 0

  unique_pos = 1
  for i in range(1, len(nums)):
    if nums[i] != nums[i-1]:
      nums[unique_pos] = nums[i]
      unique_pos += 1
  del nums[unique_pos:]
  return unique_pos

nums = [1,1,2,3,4,4,4,5]
print(nums)
print(remove_duplicates(nums))
print(nums) # sam
print()


def is_long_pressed(name, typed):
  num1_pointer = 0
  num2_pointer = 0
  while num1_pointer < len(name) and num2_pointer < len(typed):
    if name[num1_pointer] == typed[num2_pointer]:
      num1_pointer += 1
      num2_pointer += 1
    elif typed[num2_pointer] == typed[num2_pointer - 1]:
      num2_pointer += 1
    else:
      return False
  return num1_pointer == len(name)

name = "alex"
typed = "aaleex"
print(is_long_pressed(name, typed))

name2 = "saeed"
typed2 = "ssaaedd"
print(is_long_pressed(name2, typed2))

name3 = "courtney"
typed3 = "courtney"
print(is_long_pressed(name3, typed3))
print()

"""
Problem Set Version 2
Problem 1: Perfect Number
Write a function is_perfect_number() that takes in a positive integer n and returns True if it is a perfect number and False otherwise. A perfect number is a positive integer that is equal to the sum of its proper divisors, excluding itself.

For example, 6 is a perfect number because its divisors or 1, 2, and 3 and 1 + 2 + 3 = 6.
"""
def is_perfect_number(n):
  import math
  if n <= 1:
    return False
    
  sum_of_divisors = 1  # Start with 1 because 1 is a proper divisor of any positive integer.
  sqrt_n = int(math.sqrt(n))
  
  for i in range(2, sqrt_n + 1):
    if n % i == 0:
      sum_of_divisors += i
      if i != n // i:
        sum_of_divisors += n // i
  return sum_of_divisors == n

print(is_perfect_number(6))
print(is_perfect_number(28))
print(is_perfect_number(9))
print()

"""
Problem 2: 2-Pointer Palindrome
Write a function is_palindrome() that takes in a string s as a parameter and returns True if the string is a palindrome and False otherwise. You may assume the string contains only lowercase alphabetic characters.

The function must use the two-pointer approach, which is a common technique in which we initialize two variables (also called a pointer in this context) to track different indices or places in a list or string, then moves the pointers to point at new indices based on certain conditions. In the most common variation of the two-pointer approach, we initialize one variable to point at the beginning of a list and a second variable/pointer to point at the end of list. We then shift the pointers to move inwards through the list towards each other, until our problem is solved or the pointers reach the opposite ends of the list.
"""

def is_palindrome(s):
  left = 0
  right = len(s) - 1
  while left < right:
    if s[left] != s[right]:
      return False
    if s[left] == s[right]:
      left += 1
      right -= 1
  return True

s = "amanaplanacanalpanama"
s2 = "hello world"
print(is_palindrome(s))  # True
print(is_palindrome(s2)) # False
print("The time complexity is O(n) and space complexity is O(1)")
print()

"""
Problem 3: Evaluate Palindrome
The is_palindrome() problem can also be solved without using the two-pointer technique (as you may have seen it in previous units)! Evaluate the time and space complexity of your two-pointer solution.

Then, evaluate the time and space complexity of the following solution:
"""
def is_palindrome_2(s):
  reverse = s[::-1]
  return reverse == s

s = "amanaplanacanalpanama"
s2 = "hello world"
print(is_palindrome_2(s))  # True
print(is_palindrome_2(s2)) # False
print("The time complexity is O(n) and space complexity is O(n)")
print()

"""
Problem 4: Make Palindromes
You are given a string s consisting of lowercase English letters, and are allowed to perform operations on it. In one operation, you can replace a character in s with another lowercase English letter.

Write a function make_palindrome() that takes in a string s and turns it into a palindrome with the minimum number of operations as possible. If there are multiple palindromes that can be made using the minimum number of operations, make the lexicographically smallest one.

A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, string a has a letter that appears earlier in the alphabet than the corresponding letter in b.

The function returns the resulting palindrome string.
"""

def make_palindrome(s):
  s = list(s)
  left = 0
  right = len(s) - 1
  while left < right:
    if s[left] != s[right]:
      if s[left] < s[right]:
        s[right] = s[left]
      else:
        s[left] = s[right]
    left += 1
    right -= 1
  return "".join(s)
  
s = "egcfe"
s_pal = make_palindrome(s)
print(s_pal)
# s_pal == "efcfe"
# The min number of operations to make s a palindrome is 1 by changing `f` to `g`
# another palindrome possible is "egcge", but it is not lexicographically smaller

s = "abcd"
s_pal = make_palindrome(s)
print(s_pal)
# s_pal == "abba"
# The min number of operations to make s a palindrome is 2 by changing `c` to `b` and `d` to `a`
# a palindrome cannot be created in 1 operation

s = "seven"
s_pal = make_palindrome(s)
print(s_pal)
# s_pal == "neven"
# The min number of operations to make s a palindrome is 1 by changing `s` to `n`
# to get a palindrome that is lexographically smaller, it would take more operations
print()

"""
Problem 5: Reverse Vowels
Write a function reverse_vowel() that takes in a string s as a parameter and returns a string with all the vowels in the string reversed. The consonants should remain in the same position. For this question, we consider a, e, i, o, and u as vowels but not y. The vowels can appear in both lower and upper cases, more than once.
"""

def reverse_vowels(s):
  vowels = ['a', 'e', 'i', 'o', 'u']
  s_lst = [i for i in s]
  left = 0
  right = len(s_lst) - 1
  while left < right:
    if s_lst[left] in vowels and s[right] in vowels:
      s_lst[left], s_lst[right] = s_lst[right], s_lst[left]
      left += 1
      right -= 1
    elif s_lst[left] in vowels and s[right] not in vowels:
      right -= 1
    elif s_lst[left] not in vowels and s[right] in vowels:
      left += 1
    else:
      left += 1
      right -= 1
  return "".join(s_lst)
  

s1 = "hello"
rev_s1 = reverse_vowels(s1)
print(rev_s1) # holle

s2 = "leetcode"
rev_s2 = reverse_vowels(s2)
print(rev_s2) # leotcede
print()

"""
Problem 6: Two-Pointer Remove Element
The two-pointer approach can also be used with two pointers that iterate forward through a list or string at different rates. Use two pointers to solve the following problem:

Write a function removeElement() that takes in a list nums and a value val as parameters and removes all instances of that value in-place. The function returns the new length of nums.
"""
def removeElement(nums, val):
  results = nums[:]
  left = 0
  while left < len(results):
    if results[left] == val:
      results.pop(left)
    else:
      left += 1
  return results
    
nums = [5, 4, 4, 3, 4, 1]
nums_len = removeElement(nums, 4)
print(nums) # returns [5, 4, 4, 3, 4, 1] 
print(nums_len) # returns [5, 3, 1] 
print()

"""
Problem Set Version 3
Problem 1: Highest Exponent
Write a function find_highest_exponent() that takes in an integer base and an integer limit as parameters. The function returns the highest exponent for which a given base raised to that exponent is less than or equal to limit.
"""
def find_highest_exponent(base, limit):
  left = 0
  ans = 0
  while ans <= limit:
    left += 1
    ans = base**left
  return left - 1
    
exp = find_highest_exponent(2, 100)
print(exp)

exp2 = find_highest_exponent(3, 5)
print(exp2)
print()

"""Problem 2: Two-Pointer Target Sum
Write a function two_sum() that takes in a sorted list of integers nums and an integer target as parameters and returns the indices of the two numbers that add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the indices in any order.

The function must use the two-pointer approach, which is a common technique in which we initialize two variables (also called a pointer in this context) to track different indices or places in a list or string, then moves the pointers to point at new indices based on certain conditions. In the most common variation of the two-pointer approach, we initialize one variable to point at the beginning of a list and a second variable/pointer to point at the end of list. We then shift the pointers to move inwards through the list towards each other, until our problem is solved or the pointers reach the opposite ends of the list."""

def two_sum(nums, target):
  sorted_nums = sorted(list(set(nums)))
  start = 0
  end = len(sorted_nums) - 1
  while start < end:
    two_sums = nums[start] + nums[end]
    if two_sums == target:
      return [start, end]
    elif two_sums < target:
      start += 1
    else:
      end -= 1
  return []
      
nums = [2,7,11,15,7]
sol1 = two_sum(nums, 9)
print(sol1) # [0,1]

sol2 = two_sum(nums, 18)
print(sol2) # [1,2]
print("Time Complexity: O(n log n) and Space Complexity: O(n)")
print()

"""Problem 3: Evaluate Two Sum
The two_sum() problem can also be solved without using the two pointer technique (as you may have seen it in previous units)! Evaluate the time and space complexity of your two-pointer solution.

Then, evaluate the time and space complexity of the following solution:"""

def two_sum_1(nums, target):
  prev_map = {}  # Value to index mapping

  for i in range(len(nums)):
      diff = target - nums[i]
      if diff in prev_map:
          return [prev_map[diff], i]
      prev_map[nums[i]] = i

nums = [2,7,11,15,7]
sol1 = two_sum_1(nums, 9)
print(sol1) # [0,1]

sol2 = two_sum_1(nums, 18)
print(sol2) # [1,2]
print("Time Complexity: O(n) and Space Complexity: O(n)")
print()

"""Problem 4: Two-Pointer Reverse Letters
Using the two-pointer approach, write a function reverse_only_letters() that takes in a string s as a parameter. The function reverses the order of the letters in the string and returns the new string. Non-letter characters should remain in their original positions."""

def reverse_only_letters(s):
  s_str = list(s)
  left = 0
  right = len(s_str) - 1
  while left <= right: 
    if not s_str[left].isalpha():
      left += 1
    elif not s_str[right].isalpha():
      right -= 1
    else:
      s_str[left], s_str[right] = s_str[right], s_str[left]
      left += 1
      right -= 1
  return "".join(s_str)

s = "a-bC-dEf-ghIj"
reversed_s = reverse_only_letters(s)
print(reversed_s) # j-Ih-gfE-dCba
print()

"""Problem 5: Reverse Prefix
Write a function reverse_prefix() that takes in a 0-indexed string word and a character ch as parameters. The function reverses the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive) and keeps the rest of the string the same. If ch does not exist in word, do nothing. Return the resulting string."""

def reverse_prefix(word, ch):
  word_lst = list(word)
  if ch not in word:
    return word
  start = end = 0
  for i in range(0, len(word_lst)):
    if word[i] != ch:
      end += 1
    else: 
      break
  while start < end:
    word_lst[start], word_lst[end] = word_lst[end], word_lst[start]
    start += 1
    end -= 1
  return "".join(word_lst)


word = "abcdefd"
rev_word = reverse_prefix(word, "d")
print(rev_word) # dcbaefd

word2 = "helloworld"
rev_word2 = reverse_prefix(word2, "w")
print(rev_word2) # wollehorld

word3 = "xyzxyz"
rev_word3 = reverse_prefix(word3, "a")
print(rev_word3) # xyzxyz
print()

"""Problem 6: Squash Spaces
The two-pointer approach can also be used with two pointers that iterate forward through a list or string at different rates. Use two pointers to solve the following problem:

Write a function squash_spaces() that takes in a string s as a parameter and returns a new string with each substring with consecutive spaces reduced to a single space. Assume s can contain leading or trailing spaces, but in the result should be trimmed.
Do not use any of the built-in trim methods."""

def squash_spaces(s):
  n = len(s)
  result = []
  left = 0
  right = 0

  while right < n:
      # Skip leading spaces
      while left < n and s[left].isspace():
          left += 1
      right = left

      # Copy non-space characters
      while right < n and not s[right].isspace():
          result.append(s[right])
          right += 1

      # Add a single space if there are more non-space characters ahead
      if right < n:
          result.append(' ')

      # Move left pointer to the next non-space character
      left = right
      while left < n and s[left].isspace():
          left += 1
      right = left

  return ''.join(result)
  
print(squash_spaces("  hello    world  "))
print(squash_spaces("  what  about  this    ?"))
print(squash_spaces("this is my sentence"))
print()

"""Session 2: Two Pointer Technique II
Problem 2: Sharing Cookies
Imagine you're an awesome babysitter and want to give the kids you're looking after some cookies as a snack.
Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with.
Each cookie j has a cookie size s[j].
If s[j] >= g[i], we can assign the cookie j to the child i, and the child will be content.
If s[j] < g[i], the child will not be content.

Write a function find_content_children() that takes in the greed list g and the cookie size list s as parameters and maximizes the number of content children you are babysitting! The function returns"""

def find_content_children(s, g): 
  g.sort()
  s.sort()
  child = cookie = 0
  while child < len(g) and cookie < len(s):
      if s[cookie] >= g[child]:
          child += 1
      cookie += 1
  return child
      
# Test
g = [1,2,3]
s = [1,1,3]
# There are 3 children and 3 cookies
# child `0` has a greed factor of 1
# cookie `0` has a size of 1 --> content child

# child `1` has a greed factor of 2
# cookie `1` has a size of 1, this child will not be content

# child `2` has a greed factor of 3
# cookie `2` has a size of 3 --> content child

print(find_content_children(s, g)) # Output: 2 


g = [1,1]
s = [2,2,2]
# There are 2 children and 3 cookies
# child `0` has a greed factor of 1
# cookie `0` has a size of 2 --> content child

# child `1` has a greed factor of 1
# cookie `1` has a size of 1 --> content child
print(find_content_children(s, g)) # Output: 2 
print()

"""Problem 3: Valid Palindrome
Write a function valid_palindrome() that takes in a string s as a parameter and returns True if it can be a palindrome after deleting at most one character from it and False otherwise."""

def valid_palindrome(s):
  left = 0
  right = len(s) - 1
  while left < right:
    if s[left] != s[right]:
      return is_this_palindrome(s, left + 1 , right) or is_this_palindrome(s, left, right - 1)
    left += 1
    right -= 1
  return True

def is_this_palindrome(s, left, right):
  while left < right:
    if s[left] != s[right]:
      return False
    left += 1
    right -= 1
  return True
    

s = "aba"
s2 = "abca"
s3 = "abc"
print(valid_palindrome(s))
print(valid_palindrome(s2))
print(valid_palindrome(s3))
print()

"""Problem 4: Positive Negative Pairs
Write a function find_largest_k() that takes in a list of integers nums that does not contain any zeroes as a parameter. The function finds the largest positive integer k such that -k also exists in the array and returns k. If there is no such integer, return -1."""

def find_largest_k(nums):
  start = 0
  end = len(nums) - 1
  max_val = -99999
  while start < end:
    if nums[start] > max_val:
      max_val = nums[start]
    start += 1
  return max_val if -max_val in nums else -1

nums = [-1,2,-3,3,-1]
print(find_largest_k(nums))

nums2 = [-10,2,7,-3]
print(find_largest_k(nums2))