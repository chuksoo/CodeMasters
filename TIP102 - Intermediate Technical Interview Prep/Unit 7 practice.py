###################################################
# Session 1: Linked Lists II
###################################################
# Standard Problem Set Version 1
# -------------------------------------------------
'''Problem 1: Counting Iron Man's Suits
Tony Stark, aka Iron Man, has designed many different suits over the years. Given a list of strings suits where each string is a suit in Stark's collection, count the total number of suits in the list.

Implement the solution iteratively without the use of the len() function.
Implement the solution recursively.
Discuss: what are the similarities between the two solutions? What are the differences?'''
def count_suits_iterative(suits):
    count = 0
    for suit in suits:
        count += 1
    return count

def count_suits_recursive(suits):
    if not suits:
        return 0
    return 1 + count_suits_recursive(suits[1:])

'''Problem 2: Collecting Infinity Stones
Thanos is collecting Infinity Stones. Given an array of integers stones representing the power of each stone, return the total power using a recursive approach.

Evaluate the time complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.'''
def sum_stones(stones):
    if not stones:
        return 0
    return stones[0] + sum_stones(stones[1:])

'''Problem 3: Counting Unique Suits
Some of Iron Man's suits are duplicates. Given a list of strings suits where each string is a suit in Stark's collection, count the total number of unique suits in the list.

Implement the solution iteratively.
Implement the solution recursively.
Discuss: what are the similarities between the two solutions? What are the differences?
Evaluate the time complexity of each solution. Are they the same? Define your variables and provide a rationale for why you believe your solution has the stated time complexity.'''
def count_suits_iterative(suits):
    seen = set()
    for suit in suits:
        if suit not in seen:
            seen.add(suit)
    return len(seen)

def count_suits_recursive(suits):
    suit_one = suits[0] # First element
    rest = count_suits_iterative(suits[1:])

    if not suits:
        return 
    
    # if else condition
    if suit_one in suits[1:]:
        return rest
    else:
        return 1 + rest
    
'''Problem 4: Calculating Groot's Growth
Groot grows according to a pattern similar to the Fibonacci sequence. Given n, find the height of Groot after n months using a recursive method.

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Evaluate the time complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.'''
def fibonacci_growth(n):
    if n == 0:
        return 0
    
    if n == 1 or n == 2:
        return 1
    return fibonacci_growth(n - 1) + fibonacci_growth(n - 2)
    
'''Problem 5: Calculating the Power of the Fantastic Four
The superhero team, The Fantastic Four, are training to increase their power levels. Their power level is represented as a power of 4. 
Write a recursive function that calculates the power of 4 raised to the nth power to determine their training level.

Evaluate the time complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.'''
def power_of_four(n):
    # Base Case
    if n == 0:
        return 1
    
    # Handle negative exponents
    if n < 0:
        return 1 / power_of_four(-n)
    
    # recursive case
    return 4 * power_of_four(n - 1)

'''Problem 6: Strongest Avenger
The Avengers need to determine who is the strongest. Given a list of their strengths, find the maximum strength using a recursive approach without using the max() function.

Evaluate the time complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.'''
def strongest_avenger(strengths):
    pass



if __name__ == "__main__":
    print("-------- # Session 1: Recursion -------- ")
    print("------ # Standard Problem Set Version 1 ------ ")
    print("Problem 1: Counting Iron Man's Suits")
    print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
    print(count_suits_recursive(["Mark I", "Mark I", "Mark III", "Mark IV"]))
    print()
    print("Problem 2: Collecting Infinity Stones")
    print(sum_stones([5, 10, 15, 20, 25, 30]))
    print(sum_stones([12, 8, 22, 16, 10]))
    print()
    print("Problem 3: Counting Unique Suits")
    print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
    print(count_suits_recursive(["Mark I", "Mark I", "Mark III"]))
    print()
    print("Problem 4: Calculating Groot's Growth")
    print(fibonacci_growth(5))
    print(fibonacci_growth(8))
    print()
    print("Problem 5: Calculating the Power of the Fantastic Four")
    print(power_of_four(2))
    print(power_of_four(-3))
    print()
    print("Problem 6: Strongest Avenger")
    print(strongest_avenger([88, 92, 95, 99, 97, 100, 94]))
    print(strongest_avenger([50, 75, 85, 60, 90]))
    print()