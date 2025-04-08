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
    # base case
    if len(strengths) == 1:
        return strengths[0]
    
    # recursive case
    current = strengths[0]
    max_element = strongest_avenger(strengths[1:])

    # compare current element and max of rest and return larger one
    if current > max_element:
        return current
    else:
        return max_element
    
'''Problem 7: Counting Vibranium Deposits
In Wakanda, vibranium is the most precious resource, and it is found in several deposits. Each deposit is represented by a character in a string (e.g., "V" for vibranium, "G" for gold, etc.)

Given a string resources, write a recursive function count_deposits() that returns the total number of distinct vibranium deposits in resources.

Evaluate the time complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.'''
def count_deposits(resources):
    # base case
    if not resources:
        return 0
    
    if resources[0] != "V":
        return count_deposits(resources[1:])
    
    # recursive case
    return 1 + count_deposits(resources[1:])

'''Problem 8: Merging Missions
The Avengers are planning multiple missions, and each mission has a priority level represented as a node in a linked list. 
You are given the heads of two sorted linked lists, mission1 and mission2, where each node represents a mission with its priority level.

Implement a recursive function merge_missions() which merges these two mission lists into one sorted list, ensuring that the combined list maintains the correct order of priorities. 
The merged list should be made by splicing together the nodes from the first two lists.

Return the head of the merged mission linked list.'''
class Node:
  def __init__(self, value, next=None):
      self.value = value
      self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def merge_missions(mission1, mission2):
    if mission1 is None:
        return mission2
    
    if mission2 is None:
        return mission1
    
    if mission1.value <= mission2.value:
        mission1.next = merge_missions(mission1.next, mission2)
        return mission1
    else:
        mission2.next = merge_missions(mission1, mission2.next)
        return mission2

'''Problem 9: Merging Missions II
Below is an iterative solution to the merge_missions() function from the previous problem. Compare your recursive solution to the iterative solution below.

Discuss with your podmates. Which solution do you prefer?'''
def merge_missions_iterative(mission1, mission2):
    temp = Node(0)  # Temporary node to simplify the merging process
    tail = temp

    while mission1 and mission2:
        if mission1.value < mission2.value:
            tail.next = mission1
            mission1 = mission1.next
        else:
            tail.next = mission2
            mission2 = mission2.next
        tail = tail.next

    # Attach the remaining nodes, if any
    if mission1:
        tail.next = mission1
    elif mission2:
        tail.next = mission2

    return temp.next  # Return the head of the merged linked list


###################################################
# Session 2: Binary Search and Divide and Conquer
###################################################
# Standard Problem Set Version 1
# -------------------------------------------------



''''''
# def find_cruise_length(cruise_lengths, vacation_length):
#     # if list is empty, return False
#     if not cruise_lengths:
#         return False

#     # define two pointer low and high
#     low, high = 0, len(cruise_lengths) - 1
#     # while loop
#     while low <= high:
#         # get middle of the list
#         mid_point = (low + high) // 2
#         if cruise_lengths[mid_point] == vacation_length:
#             return True
#         # perform binary search
#         elif cruise_lengths[mid_point] > vacation_length:
#             high = mid_point - 1
#         else:
#             low = mid_point + 1
#     return False

# print(find_cruise_length([9, 10, 11, 12, 13, 14, 15], 13))
# print(find_cruise_length([8, 9, 12, 13, 13, 14, 15], 11))
# print()

# def find_cabin_index(cabins, preferred_deck):
#     # if list is empty, return 0
#     if not cabins:
#          return 0
    
#     n = len(cabins)
#     return recursive_binary_search(cabins, 0, n, preferred_deck)
    
# def recursive_binary_search(arr, low, high, target):
#     if high > low:
#         mid = (low + high) // 2

#         if arr[mid] == target:
#             return mid
#         elif arr[mid] > target:
#             return recursive_binary_search(arr, low, mid - 1, target)
#         else:
#             return recursive_binary_search(arr, mid + 1, high, target)
#     elif high == low:
#         return low
 
# print(find_cabin_index([1, 3, 5, 6], 5)) # 2  low=0, high = 4 mid = 2 
# print(find_cabin_index([1, 3, 5, 6], 2)) # 1  low=0, high = 4 mid = 2  call2:low=0, high =1 mid =0 call3: low=1, high =1 mid =1 call4:l=1,h=0
# print(find_cabin_index([1, 3, 5, 6], 7)) # 4
# print()

# def count_checked_in_passengers(rooms):
#     low, high = 0, len(rooms) - 1
#     # calculate mid point
#     while low <= high:
#         mid = (low + high) // 2
#         # if element at mid point is a 1
#         if rooms[mid] == 0:
#             # update low
#             low = mid + 1
#         else:
#             high = mid - 1
       
#     return len(rooms) - low

# rooms1 = [0, 0, 0, 1, 1, 1, 1]
# rooms2 = [0, 0, 0, 0, 0, 1]
# rooms3 = [0, 0, 0, 0, 0, 0]

# print(count_checked_in_passengers(rooms1))  # 4
# print(count_checked_in_passengers(rooms2))  # 1
# print(count_checked_in_passengers(rooms3))  # 0


# def is_profitable(excursion_counts):
#     pass

# print(is_profitable([3, 5, 6, 8, 9, 12])) # 6 excursions
# print(is_profitable([0, 0]))
# print(0 // 2)   






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
    print("Problem 7: Counting Vibranium Deposits")
    print(count_deposits("VVVVV"))
    print(count_deposits("VXVYGA"))
    print()
    print("Problem 8: Merging Missions")
    mission1 = Node(1, Node(2, Node(4)))
    mission2 = Node(1, Node(3, Node(4)))
    print_linked_list(merge_missions(mission1, mission2))
    print()
    print("Problem 9: Merging Missions II")
    mission1 = Node(1, Node(2, Node(4)))
    mission2 = Node(1, Node(3, Node(4)))
    print_linked_list(merge_missions_iterative(mission1, mission2))
    print()

