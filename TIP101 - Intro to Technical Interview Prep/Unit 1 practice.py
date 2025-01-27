# Session 1 
# Problem Set Version 1
''' Problem 6: Classify Age '''
def classify_age(age):
  return "child" if age < 18 else "adult"

output = classify_age(18)
print(output)
output = classify_age(7)
print(output)
output = classify_age(50)
print(output)
print()

''' Problem 7: What time is it? '''
def what_time_is_it(hour):
  if hour == 2:
    return "taco time 🌮"
  elif hour == 12:
    return "peanut butter jelly time 🥪"
  else:
    return "nap time 😴"

time = what_time_is_it(2)
print(time)
time = what_time_is_it(7)
print(time)
time = what_time_is_it(12)
print(time)
print()

'''Problem 11: Counter
Write a function counter() that uses the range function to print numbers between 1 and a given stop value (inclusive).'''
def counter(stop):
  for i in range(1, stop + 1):
    print(i)
    
counter(7)
print()

'''Problem 12: Sum of 1 to 10
Write a function sum_ten() that returns the sum of numbers from 1 to 10.'''
def sum_ten():
  accum = 0
  for w in range(1, 11):
    accum += w
  return accum 

print("Sum of tens:", sum_ten())
print()

'''Problem 13: Total Sum
Write a function sum_positive_range() that returns the sum of numbers from 1 to a given stop value (inclusive).'''
def sum_positive_range(stop):
  accum = 0
  for w in range(1, stop + 1):
    accum += w
  return accum
  
print(sum_positive_range(6))
print()

'''Problem 14: Total Sum in Range
Write a function sum_range() that returns the sum of numbers from a given start value to a given stop value (inclusive).'''
def sum_range(start, stop):
  accum = 0
  for w in range(start, stop + 1):
    accum += w
  return accum

print("Sum in range:", sum_range(3, 9))
print()
# Example Usage: sum = sum_range(3, 9)
# Example Result: sum = 42

'''Problem 15: Negative Numbers
Write a function print_negatives() that takes a list of integers lst and prints all negative numbers in the list.'''
def print_negatives(lst):
  negatives = [w for w in lst if w < 0]
  if negatives == []:
    print("None")
  for i in negatives:
    print(i)

# Test
print_negatives([3, 2, 2, 1,-5])
print_negatives([1,2,3,4,5])
print_negatives([3,-2,2,1,-5])
print()

# Problem Set Version 2
'''Problem 6: Rock, Paper, Scissors
Write a function rock_paper_scissors() that determines the winner of a game of Rock, Paper, Scissors. The function accepts two strings as parameters: player1 and player2. Each parameter can have a value of "rock", "paper", or "scissors".

Print either "Player 1 wins!" or "Player 2 wins!" according to the following rules:
Rock wins against scissors.
Scissors wins against paper.
Paper wins against rock.

If both player1 and player2 have the same value, print "It's a tie!".'''

def rock_paper_scissors(player1, player2):
  if player1 == player2:
    return "It's a tie!"
  elif player1 == "rock" and player2 == "scissors" or player1 == "scissors" and player2 == "paper" or player1 == "paper" and player2 == "rock":
    return "Player 1 wins!"
  else:
    return "Player 2 wins!"

print(rock_paper_scissors("rock", "rock"))
print(rock_paper_scissors("scissors", "rock"))
print(rock_paper_scissors("scissors", "paper"))
print(rock_paper_scissors("rock", "paper"))
print(rock_paper_scissors("paper", "rock"))
print()

'''Problem 8: Above the Threshold'''
def above_threshold(lst, threshold):
  new_lst = [w for w in lst if w > threshold]
  return new_lst

lst = [8,2,13,11,4,10,14]
new_lst = above_threshold(lst, 10)
print(new_lst)
print()

'''Problem 9: Countdown
Write a function countdown() that takes in two positive integers m and n as parameters and prints numbers from m down to n.'''
def countdown(m, n):
  for i in range(m, n - 1, -1):
    print(i)

countdown(5, 1)
print()

'''Problem 10: Calculate Power
Write a function power() that takes in two integers base and exponent. The function should return the value of the base number to the power of the exponent.'''
def power(base, exponent):
  return base**exponent

pow1 = power(2,5)
print(pow1)
pow2 = power(3,3)
print(pow2)
print()

'''Problem 12: Calculate Factorial
Write a function factorial() that takes in an integer n as a parameter and returns its factorial. The factorial of a number is the product of all positive integers less than or equal to that number. For example, the factorial of 5 (denoted as 5!) is 5! = 5 * 4 * 3 * 2 * 1 which equals 120.'''
def factorial(n):
  num = 1
  for i in range(1, n + 1):
    num *= i
  return f"{n}! factorial is: {num}"
print(factorial(3))
print(factorial(5))
print()
#Example Usage: print(factorial(3))
#Example Output: 6

'''Problem 15: Count Evens
Write a function count_evens() that takes in a list of integers lst as a parameter. The function returns the number of even numbers in the list.'''
def count_evens(lst):
  count = 0
  for w in lst:
    if w % 2 == 0:
      count += 1
  return count

# Test
lst1 = [1,5,7,9]
count1 = count_evens(lst1)
print(count1)

lst2 = [2,4,6,8]
count2 = count_evens(lst2)
print(count2)
print()

# Session 2
'''Problem 4: Flip Signs
Write a function flip_sign() that takes in a list of integers lst as a parameter and returns a new list where each number in the original list has been multiplied by -1.'''
def flip_sign(lst):
  flipped_lst = [-1*val for val in lst]
  return flipped_lst

lst = [1,-2,-3,4]
flipped_lst = flip_sign(lst)
print(flipped_lst)
print()
# Example Output: [-1, 2, 3, -4]

'''Problem 5: Max Difference
Write a function max_difference() that takes in a list of integers lst and returns the difference between the smallest and largest value in the list.
'''
def max_difference(lst):
  lst.sort()
  return f"Difference between smallest and largest: {lst[-1] - lst[0]}"

lst = [5,22,8,10,2]
max_diff = max_difference(lst)
print(max_diff)
print()

'''Problem 6: Below Threshold
Write a function count_less_than() that takes in a list of integers numbers and an integer threshold as parameters and returns the number of items in numbers that are less than threshold.'''
def count_less_than(numbers, threshold):
  new_lst = [num for num in numbers if num < threshold] 
  return f"Count of numbers less than {threshold} in {numbers}: {len(new_lst)}"

numbers = [12,8,2,4,-4,10]
counter = count_less_than(numbers, 5)
print(counter)
print()

'''Problem 8: Multiples of Five
Write a function multiples_of_five() that prints out multiples of 5 between 1 and 100 (inclusive).'''
def multiples_of_five(num):
  assert num >= 1 and num <= 100
  multiples = [w for w in range(1, num + 1) if w % 5 == 0]
  for vals in multiples:
    print(vals)

multiples_of_five(20)
print()

'''Problem 10: FizzBuzz
Write a function fizzbuzz() that takes in an integer n as a parameter and prints the numbers from 1 to n.
For multiples of 3, print "Fizz" instead of the number.
For multiples of 5, print "Buzz" instead of the number.'''
def fizzbuzz(n):
  for i in range(1, n + 1):
    if i % 3 == 0:
      print("Fizz")
    elif i % 5 == 0:
      print("Buzz")
    else:
      print(i)

fizzbuzz(13)
print()

'''Problem 11: Print the Index
Write a function print_indices() that takes in an integer list lst as a parameter and prints out the index of each item in the given list.
Use the function range() to loop through the list indices.'''
def print_indices(lst):
  for i in range(len(lst)):
    print(i)

lst = [5,1,3,8,2]
print_indices(lst)
print()


'''Problem 12: Linear Search
Write a function linear_search() that takes in a list lst and value target as parameters. The function returns the index of target in lst if found. If target is not found in lst, return -1.'''
def linear_search(lst, target):
  if target not in lst:
    return -1

  for i, val in enumerate(lst):
    if val == target:
      return i

# Test
lst = [1,4,5,2,8]
position = linear_search(lst,5)
print(position)
# Example Output: 2

lst = [1,4,5,2,8]
position = linear_search(lst,10)
print(position)
# Example Output: -1
print()
      
# Problem Set Version 2
'''Problem 4: Check for Number
Write a function check_num() that takes in a list of integers lst and an integer num as parameters and returns True if num is a value in lst and False otherwise.'''
def check_num(lst, num):
  if num not in lst:
    return False
  for i in lst:
    if i == num:
      return True

lst = [5,2,3,9,10]
flag1 = check_num(lst,9)
flag2 = check_num(lst,4)
print(f'flag1 == {flag1}')
print(f'flag2 == {flag2}\n')

'''Problem 5: Missing Number
Write a function find_missing() that takes in a list nums containing n unique numbers in the range [0,n]. The function returns the only number in the range that is missing from the list.'''
def find_missing(nums):
  n = sorted(nums)[-1]
  missing_num_list = [i for i in range(0, n+1) if i not in nums]
  for val in missing_num_list:
    print(val)

nums = [2,4,1,0,6]
missing_num = find_missing(nums)
missing_num
print()

'''Problem 6: Reverse List
Write a function reverse_list() that takes in a list lst as a parameter and returns a new list containing the elements of lst in reverse order.'''
def reverse_list(lst):
  return lst[::-1]

lst = [1,2,3,4,5]
rev_lst = reverse_list(lst)
print(rev_lst)
print()

'''Problem 9: Create Number
Write a function list_to_number() that takes in a list digits where each item is a digit between 0-9. The function returns the number they represent when combined.'''
def list_to_number(digits):
  new_digit = ''
  for i in digits:
    new_digit += str(i)
  return int(new_digit)

digits = [1,0,3]
number = list_to_number(digits)
print(number)
print()

'''Problem 10: Move Zeroes
Write a function move_zeroes() that takes in an integer list nums and returns a new list with all the 0 values moved to the end of the list. The relative non-zero elements in the original list should be maintained.'''
def move_zeroes(nums):
  # left pointer for writing non-zero elements
  left = 0
  # right pointer for scanning array
  for right in range(len(nums)):
    # if current element is non-zero
    if nums[right] != 0:
      # swap elements at left and right pointers
      nums[left], nums[right] = nums[right], nums[left]
      left += 1
  return nums

# Example Usage:
nums = [1,0,2,3,0,0,4]
new_nums = move_zeroes(nums)
print(new_nums)
print()

'''Problem 11: Odd Indices
Write a function print_odd_indices() that takes in a list nums as a parameter and prints out items at odd indices in the list.'''

def print_odd_indices(nums):
    for i, val in enumerate(nums):
      if i % 2 != 0:
        print(val)
        
nums = [3,4,8,1,5,2]
print_odd_indices(nums)
print() 

'''Problem 12: List Occurrences
Write a function find_all_occurrences() that takes in a list lst and a value target as parameters and returns a list of all indices where target is found in lst.'''
def find_all_occurrences(lst, target):
  # # Brute force approach
  # idx_lst = []
  # for i, val in enumerate(lst):
  #   if val == target:
  #     idx_lst.append(i)
  # return idx_lst

  # Second approach
  idx_lst = []
  left = 0
  right = len(lst) - 1
  while left <= right:
    if lst[left] == target:
      idx_lst.append(left)  
      left += 1
    else:
      left += 1
  return idx_lst

# Example Usage:
lst = [1,2,6,5,2,1,3,2,2]
index_list = find_all_occurrences(lst, 2)
print(index_list)
print()

def addFun(n):
  if n <= 0:
    return 0
  if n == 1:
    return 2
  return addFun(n-1) + addFun(n-2)
print(addFun(6))