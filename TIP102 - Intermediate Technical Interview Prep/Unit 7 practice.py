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

# -------------------------------------------------
# Standard Problem Set Version 2
# -------------------------------------------------
'''Problem 1: Calculating Village Size
In the kingdom of Codepathia, the queen determines how many resources to distribute to a village based on its class. 
A village's class is equal to the number of digits in its population. Given an integer population, write a function get_village_class() that returns the number of digits in population.

Implement the solution iteratively.
Implement the solution recursively.
Discuss: what are the similarities between the two solutions? What are the differences?'''
def get_village_class_iterative(population):
    # base case
    if population == 0:
        return 1
    
    count = 0
    n = abs(population)
    while n > 0:
        n = n // 10
        count += 1
    return count

def get_village_class_recursive(population):
    # base case
    if abs(population) < 10:
        return 1
    # recursive step - remove rightmost digit and add one
    else:
        return 1 + get_village_class_recursive(abs(population) // 10)

'''Problem 2: Counting the Castle Walls
In a faraway kingdom, a castle is surrounded by multiple defensive walls, where each wall is nested within another. 
Given a list of lists walls where each list [] represents a wall, write a recursive function count_walls() that returns the total number of walls.

Evaluate the time complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.
'''
def count_walls(walls):
    count  = 1
    for item in walls:
        if isinstance(item, list):
            count = count + count_walls(item)
        else:
            continue
    return count 

'''Problem 3: Reversing a Scroll
A wizard is deciphering an ancient scroll and needs to reverse the letters in a word to reveal a hidden message. 
Write a recursive function to reverse the letters in a given scroll and returns the reversed scroll. Assume scroll only contains alphabetic characters.

Evaluate the time complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.'''
def reverse_scroll(scroll):
    # base case
    if len(scroll) <= 1:
        return scroll
    
    # recursive case
    return reverse_scroll(scroll[1:]) + scroll[0]
    
'''Problem 4: Palindromic Name
Queen Ada is superstitious and believes her children will only have good fortune if their name is symmetrical and reads the same forward and backward. 
Write a recursive function that takes in a string comprised of only lowercase alphabetic characters name and returns True if the name is palindromic and False otherwise.

Evaluate the time complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.'''
def is_palindrome(name):
    # check for empty sting
    if len(name) == 0:
        return False
    
    # base case
    if len(name) == 1:
        return True
    
    # compare first and last character
    if name[0] != name[-1]:
        return False
    else:
        return is_palindrome(name[1:-1])

'''Problem 5: Doubling the Power of a Spell
The court magician is practicing a spell that doubles its power with each incantation. Given an integer initial_power and a non-negative integer n, 
write a recursive function that doubles initial_power n times.

Evaluate the time complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.'''    
def double_power(initial_power, n):
    # base case
    if n == 0:
        return initial_power
    # recursive case
    return double_power(initial_power * 2, n - 1)
    
'''Problem 6: Checking the Knight's Path
A knight is traveling along a path marked by stones, and each stone has a number on it. The knight must check if the numbers on the stones form a strictly increasing sequence. 
Write a recursive function to determine if the sequence is strictly increasing.

Evaluate the time complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.'''
def is_increasing_path(path):
    # if list is empty, return False
    if len(path) <= 1:
        return True
    
    # base case
    if path[0] > path[1]:
        return False
    return is_increasing_path(path[1:])

'''Problem 7: Finding the Longest Winning Streak
In the kingdom's grand tournament, knights compete in a series of challenges. A knight's performance in the challenge is represented by a string challenges, 
where a success is represented by an S and each other outcome (like a draw or loss) is represented by an "O". Write a recursive function to find the length of 
the longest consecutive streak of successful challenges ("S").

Evaluate the time complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.'''
def longest_streak(frames, current_length=0, max_length=0):
    # base case
    if not frames:
        return max_length
    
    # recursive case
    if frames[0] == 'S':
        new_length = current_length + 1
        new_max_length = max(max_length, new_length)
    else:
        new_length = 0
        new_max_length = new_length
    
    return longest_streak(frames[1:], new_length, new_max_length)

'''Problem 8: Weaving Spells
A magician can double a spell's power if they merge two incantations together. Given the heads of two linked lists spell_a and spell_b 
where each node in the lists contains a spell segment, write a recursive function weave_spells() that weaves spells in the pattern:

a1 -> b1 -> a2 -> b2 -> a3 -> b3 -> ...'''
def weave_spells_recursive(spell_a, spell_b):
    if spell_a is None:
        return spell_b
    
    if spell_b is None:
        return spell_a

    if spell_a.value <= spell_b.value:
        spell_a.next = weave_spells_recursive(spell_a.next, spell_b)
        return spell_a
    else:
        spell_b.next = weave_spells_recursive(spell_a, spell_b.next)
        return spell_b
    
'''Problem 9: Weaving Spells II
Below is an iterative solution to the weaving_spells() function from the previous problem. Compare your recursive solution to the iterative solution below.

Discuss with your podmates. Which solution do you prefer?'''
def weave_spells_iterative(spell_a, spell_b):
    # If either list is empty, return the other
    if not spell_a:
        return spell_b
    if not spell_b:
        return spell_a

    # Start with the first node of spell_a
    head = spell_a
    
    # Loop through both lists until one is exhausted
    while spell_a and spell_b:
        # Store the next pointers
        next_a = spell_a.next
        next_b = spell_b.next
        
        # Weave spell_b after spell_a
        spell_a.next = spell_b
        
        # If there's more in spell_a, weave it after spell_b
        if next_a:
            spell_b.next = next_a
        
        # Move to the next nodes
        spell_a = next_a
        spell_b = next_b

    # Return the head of the new woven list
    return head

# -------------------------------------------------
# Advanced Problem Set Version 1
# -------------------------------------------------
'''Problem 1: Counting the Layers of a Sandwich
You're working at a deli, and need to count the layers of a sandwich to make sure you made the order correctly. 
Each layer is represented by a nested list. Given a list of lists sandwich where each list [] represents a sandwich layer, 
write a recursive function count_layers() that returns the total number of sandwich layers.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your 
solution has the stated time and space complexity.'''
def count_layers(sandwich):
    count = 1
    for item in sandwich:
        if isinstance(item, list):
            count = count + count_layers(item)
        else:
            continue
    return count

'''Problem 2: Reversing Deli Orders
The deli counter is busy, and orders have piled up. To serve the last customer first, you need to reverse the order of the deli orders. 
Given a string orders where each individual order is separated by a single space, write a recursive function reverse_orders() that 
returns a new string with the orders reversed.

Evaluate the time and space complexity of your solution. Define your variables and
 provide a rationale for why you believe your 
solution has the stated time and space complexity.'''
def reverse_orders(orders):
    # base case
    if not orders or " " not in orders:
        return orders
    
    tokens = orders.split(" ")
    if len(tokens) == 1:
        return tokens[0]
    
    # recursive case
    first_token = tokens[0]
    rest_string = " ".join(tokens[1:])

    return reverse_orders(rest_string) + " " + first_token

'''Problem 3: Sharing the Coffee
The deli staff is in desperate need of caffeine to keep them going through their shift and has decided to divide the coffee supply equally among themselves. 
Each batch of coffee is stored in containers of different sizes. Write a recursive function can_split_coffee() that accepts a list of integers coffee 
representing the volume of each batch of coffee and returns True if the coffee can be split evenly by volume among n staff and False otherwise.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.'''
def can_split_coffee(coffee, n):
    total_volume = sum(coffee) 
    
    # If the total volume isn't divisible by n, return False
    if total_volume % n != 0:
        return False
    
    target = total_volume // n 
    return can_divide(coffee, n, target, 0)

def can_divide(coffee, n, target, current_sum):
    if n == 0:
        return True  # If we've successfully partitioned for all staff
    if current_sum == target:  # Current staff member has a full share
        return can_divide(coffee, n - 1, target, 0)  # Move to the next staff member
    if not coffee:
        return False  # No more coffee batches to partition

    # Try including the first batch of coffee in the current partition
    include = can_divide(coffee[1:], n, target, current_sum + coffee[0]) 
    
    # Try excluding the first batch of coffee from the current partition
    exclude = can_divide(coffee[1:], n, target, current_sum) 
    
    return include or exclude

'''Problem 4: Super Sandwich
A regular at the deli has requested a new order made by merging two different sandwiches on the menu together. Given the heads of two linked lists sandwich_a and sandwich_b 
where each node in the lists contains a spell segment, write a recursive function merge_orders() that merges the two sandwiches together in the pattern:

a1 -> b1 -> a2 -> b2 -> a3 -> b3 -> ...

Return the head of the merged sandwich.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.'''
def merge_orders_iterative(sandwich_a, sandwich_b):
    # base case
    if sandwich_a is None:
        return sandwich_b
    if sandwich_b is None:
        return sandwich_a
    
    dummy = Node('dummy')
    current = dummy

    while sandwich_a is not None and sandwich_b is not None:
        # attach current node from sandwich_a
        current.next = sandwich_a
        sandwich_a = sandwich_a.next
        current = current.next

        # attach current node from sandwich_b
        current.next = sandwich_b
        sandwich_b = sandwich_b.next
        current = current.next

    # attach any remaining node
    if sandwich_a is not None:
        current.next = sandwich_a
    else:
        current.next = sandwich_b
    return dummy.next

def merge_orders_recursive(sandwich_a, sandwich_b):
    # base case
    pass



###################################################
# Session 2: Binary Search and Divide and Conquer
###################################################
# Standard Problem Set Version 1
# -------------------------------------------------

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

# ------------------------------------------------
# Sorting algorithm
# Selection Sort Algorithm - Total Time - (O(N^2))
def findSmallest(arr): # Time - O(N)
  smallest = arr[0]       
  smallest_index = 0      
  for i in range(1, len(arr)): 
    if arr[i] < smallest:
      smallest = arr[i]
      smallest_index = i
  return smallest_index

def selectionSort(arr):                      
  newArr = []
  copiedArr = list(arr) 
  for i in range(len(copiedArr)):           # O(N)
      smallest = findSmallest(copiedArr)    # O(N)
      newArr.append(copiedArr.pop(smallest)) 
  return newArr

#--------------------------------------------------




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
    print("------ # Standard Problem Set Version 2 ------ ")
    print("Problem 1: Calculating Village Size")
    print(get_village_class_iterative(432))
    print(get_village_class_recursive(432))
    print(get_village_class_iterative(9))
    print(get_village_class_recursive(9))
    print()
    print("Problem 2: Counting the Castle Walls")
    walls = ["outer", ["inner", ["keep", []]]]
    print(count_walls(walls))
    print(count_walls([]))
    print()
    print("Problem 3: Reversing a Scroll")
    print(reverse_scroll("cigam"))
    print(reverse_scroll("lleps"))
    print()
    print("Problem 4: Palindromic Name")
    print(is_palindrome("eve"))
    print(is_palindrome("ling"))
    print(is_palindrome(""))
    print()
    print("Problem 5: Doubling the Power of a Spell")
    print(double_power(5, 3))
    print(double_power(7, 2))
    print()
    print("Problem 6: Checking the Knight's Path")
    print(is_increasing_path([1, 2, 3, 4, 5]))
    print(is_increasing_path([3, 5, 2, 8]))
    print()
    print("Problem 7: Finding the Longest Winning Streak")
    print(longest_streak("SSOSSS"))
    print(longest_streak("SOSOSOSO"))
    print()
    print("Problem 8: Weaving Spells")
    spell_a = Node('A', Node('C', Node('E')))
    spell_b = Node('B', Node('D', Node('F')))
    print_linked_list(weave_spells_recursive(spell_a, spell_b))
    print()
    print("Problem 9: Weaving Spells II")
    spell_a = Node('A', Node('C', Node('E')))
    spell_b = Node('B', Node('D', Node('F')))
    print_linked_list(weave_spells_iterative(spell_a, spell_b))
    print()
    print("------ # Advanced Problem Set Version 1 ------ ")
    print('Problem 1: Counting the Layers of a Sandwich')
    sandwich1 = ["bread", ["lettuce", ["tomato", ["bread"]]]]
    sandwich2 = ["bread", ["cheese", ["ham", ["mustard", ["bread"]]]]]
    print(count_layers(sandwich1))
    print(count_layers(sandwich2))
    print()
    print("Problem 2: Reversing Deli Orders")
    print(reverse_orders("Bagel Sandwich Coffee"))
    print()
    print("Problem 3: Sharing the Coffee")
    print(can_split_coffee([4, 4, 8], 2))
    print(can_split_coffee([5, 10, 15], 4))
    print()
    print("Problem 4: Super Sandwich")
    sandwich_a1 = Node('Bacon', Node('Lettuce', Node('Tomato')))
    sandwich_b = Node('Turkey', Node('Cheese', Node('Mayo')))
    sandwich_a2 = Node('Bacon', Node('Lettuce', Node('Tomato')))
    sandwich_c = Node('Bread')
    print_linked_list(merge_orders_iterative(sandwich_a1, sandwich_b))
    print_linked_list(merge_orders_iterative(sandwich_a2, sandwich_c))
    print()
    sandwich_a1 = Node('Bacon', Node('Lettuce', Node('Tomato')))
    sandwich_b = Node('Turkey', Node('Cheese', Node('Mayo')))
    sandwich_a2 = Node('Bacon', Node('Lettuce', Node('Tomato')))
    sandwich_c = Node('Bread')
    print_linked_list(merge_orders_recursive(sandwich_a1, sandwich_b))
    print_linked_list(merge_orders_recursive(sandwich_a2, sandwich_c))
    print()
    print()
    print()
    print("Selection Sort Algorithm")
    print(selectionSort([5, 3, 6, 2, 10]))
    print(7 // 10)


