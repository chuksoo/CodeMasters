"""
# Unit 6: Advanced Linked Lists
# Problem Set Version 1
"""

"""Problem 1: Nested Constructors
Step 1: Copy the following code into Replit.
Step 2: Add a line of code (outside of the class) to create the linked list 4 -> 3 -> 2 in a single assignment statement.
"""
class Node:
  def __init__(self, value, next = None):
    self.value = value
    self.next = next

def nested_constructor(head):
  current = head
  while current:
    print(current.value, end = " -> " if current.next else "")
    current = current.next
  print()
    
head = Node(4, Node(3, Node(2)))
nested_constructor(head)
print()

"""Problem 2: Find Frequency
Given the head of a linked list and a value val, return the frequency of val in the list. Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity."""

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def count_element(head, val):
  count = 0
  current = head
  while current:
    if current.value == val:
      count += 1
    current = current.next
  return count

head = Node(3, Node(1, Node(2, Node(1))))
print(count_element(head, 1))
print()

"""Problem 3: Remove Tail
The following code attempts to remove the tail of a singly linked list. However, it has a bug!
Step 1: Copy this code into Replit.
Step 2: Create your own test cases to run the code against, and use print statements and the stack trace to identify and fix the bug so that the function correctly removes the tail of the list.
"""
class Node:
  def __init__(self, value=None, next=None):
      self.value = value
      self.next = next

# Helper function to print the linked list
def print_list(node):
  current = node
  while current:
      print(current.value, end=" -> " if current.next else "")
      current = current.next
  print()

# I have a bug! 
def remove_tail(head):
  if head is None: # If the list is empty, return None
      return None
  if head.next is None: # If there's only one node, removing it leaves the list empty
      return None 

  # Start from the head and find the second-to-last node
  current = head
  while current.next.next: 
      current = current.next
  current.next = None # Remove the last node by setting second-to-last node to None
  return head

linkedLst = Node(1, Node(2, Node(3, Node(4))))
print("Linked list before removing tail")
print_list(linkedLst)
print("Linked list after removing tail")
print_list(remove_tail(linkedLst))
print()

"""Problem 4: Find the Middle
A variation of the two-pointer technique introduced in Unit 4 is to have a slow and a fast pointer that increment at different rates. Given the head of a linked list, use the slow-fast pointer technique to find the middle node of a linked list. If there are two middle nodes, return the second middle node.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity."""

class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def find_middle_element(head):
  if head is None and head.next is None:
    return head
    
  slow, fast = head, head
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
  return slow.value
  
def remove_tail(head):
  if head is None: # If the list is empty, return None
      return None
    
  if head.next is None: # If there's only one node, removing it leaves the list empty
      return None 

  # Start from the head and find the second-to-last node
  current = head
  while current.next.next: 
      current = current.next
  current.next = None # Remove the last node by setting second-to-last node to None
  return head

def print_list(node):
  current = node
  while current:
      print(current.value, end=" -> " if current.next else "")
      current = current.next
  print()

head = Node(1, Node(2, Node(3, Node(4))))
print("This is the complete node")
print_list(head)
print("Value of the middle node:", find_middle_element(head))

print("Node after removing tail")
print_list(remove_tail(head))
print("Value of middle node after removing tail:", find_middle_element(remove_tail(head)))
print()

"""Problem 5: Is Palindrome?
Given the head of a singly linked list, return True if the values of the linked list are palindromic and False otherwise. Use the two-pointer technique in your solution.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity."""

class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def reverse_linked_list(slow):
  prev = None
  next = None
  current = slow
  while current:
    next = current.next
    current.next = prev
    prev = current
    current = next
  return prev

def is_palindrome(head):
  # check if head is None
  if head is None or head.next is None:
    return None

  # initialize slow and fast pointer
  slow, fast = head, head
  # traverse the linked list using pointers at different speed
    # continue until fast reaches the end and slow points to the middle
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    
  # reverse the second half of the list
  second_half = reverse_linked_list(slow)

  # compare first half with reversed second half
  # if both halves match, then the list is palindrome, else not
  first_half = head
  while first_half and second_half:
    if first_half.value != second_half.value:
      return False
    first_half = first_half.next
    second_half = second_half.next
  return True

head = Node(2, Node(4, Node(6, Node(4, Node(2)))))
print("This is the complete node")
print_list(head)
print("Is this a palindome:", is_palindrome(head))
print()
head2 = Node(5, Node(4, Node(7, Node(9, Node(4, Node(5))))))
print("This is the complete node")
print_list(head2)
print("Is this a palindome:", is_palindrome(head2))
print()
head3 = Node(0, Node(5, Node(4, Node(5, Node(0)))))
print("This is the complete node")
print_list(head3)
print("Is this a palindome:", is_palindrome(head3))
print()

"""Problem 6: Put it in Reverse
Given the head of a singly linked list, reverse the list, and return the reversed list. You must reverse the list in place. Return the head of the reversed list.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity."""
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def reverse(head):
  if head is None and head.next is None:
    return None

  # initiate three pointer - prev, current, and next
  prev = None
  next = None
  current = head

  while current:
    next = current.next
    current.next = prev
    prev = current
    current = next
  return prev

head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print("This is the complete node")
print_list(head)
print("Reversed linked list:")
print_list(reverse(head))
print()
# Input List: 1 -> 2 -> 3 -> 4
# Input: head = 1
# Expected Return Value: 4
# Expected Result List: 4 -> 3 -> 2 -> 1

"""Problem Set Version 2
Problem 1: One to Many
The assignment statement to the head variable below creates the linked list Mario -> Luigi -> Wario. Break apart the assignment statement into multiple lines with one call to the Node constructor per line to recreate the list."""
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

# Function to print the linked list for verification
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()
# Create each node separately and link them together
wario = Node("Wario")
luigi = Node("Luigi", wario)
mario = Node("Mario", luigi)

# Assign the head of the list to the "Mario" node
head = mario
# Verify the linked list structure
print_linked_list(head)
print()

"""Problem 2: Find Max
Given the head of a linked list where each node is an integer value, return the maximum value in the linked list."""

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def find_max(head):
  if head is None:
    return None

  max_val = -99999
  current = head
  while current:
    if current.value > max_val:
      max_val = current.value
    current = current.next
  return max_val

head = Node(5, Node(6, Node(7, Node(8, Node(2)))))
print("Maximum value in linked list is:", find_max(head))
print()
# Linked List: 5 -> 6 -> 7 -> 8 -> 2
# Expected Output: 8

"""Problem 3: Remove First Value
The following code attempts to remove the first node with a given value from a singly linked list based but it contains a bug!

Step 1: Copy this code into Replit.

Step 2: Create your own test cases to run the code against, and use print statements and the stack trace to identify and fix the bug so that the function correctly removes a node by value from the list."""
class Node:
  def __init__(self, value=None, next=None):
      self.value = value
      self.next = next

# Function with a bug!
def remove_by_value(head, val):
  # Check if the list is empty
  if head is None:
      return None

  # If the node to be removed is the head of the list
  if head.value == val:
      return head.next

  # Initialize pointers
  previous = head
  current = head.next

  # Traverse the list to find the node to remove
  while current:
      if current.value == val:
          previous.next = current.next
          return head
      previous = current
      current = current.next
  # If no node was found with the value `val`, return the original head
  return head

val = 3
head = Node(1, Node(2, Node(3, Node(4))))
print(f"Linked list before removing {val}:")
print_linked_list(head)
print(f"Linked list after removing {val}:")
print_linked_list(remove_by_value(head, val))
print()
# Input List: 1 -> 2 -> 3 -> 4
# Value to Remove: 3
# Expected Return Value: 1
# Expected Result List: 1 -> 2 -> 4

"""Problem 4: Middle Match
A variation of the two-pointer technique introduced in Unit 4 is to have a slow and a fast pointer that increment at different rates. Given the head of a linked list, and a value val, use the slow-fast pointer technique to determine if val matches the middle node of the list. If there are two middle nodes, return True if the second middle node matches the value val.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity."""

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def middle_match(head, val):
  if head is None or head.next is None:
    return False

  slow, fast = head, head
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
  return slow.value == val

val = 2
head1 = Node(1, Node(2, Node(3)))
print(middle_match(head1, val))
head2 = Node(1, Node(2, Node(3, Node(4))))
print(middle_match(head2, val))
print()
# Input List:
# 1 -> 2 -> 3
# Input: head = 1, val = 2

# Input List:
# 1 -> 2 -> 3 -> 4
# Input: head = 1, val = 2

# Expected Return Value: True
# Expected Return Value: False

"""Problem 5: Where Do We Begin?
A linked list contains a cycle if the tail element points back to another element in the list. Given the head of a linked list, use the fast and slow pointer method to determine the node where the cycle starts. If the linked list does not contain a cycle, return None.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity."""

class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next
        
def get_loop_start(head):
  if head is None or head.next is None:
    return None

  slow, fast = head, head
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
      break

  if fast is None or fast.next is None:
    return None

  slow = head
  while slow != fast:
    slow = slow.next
    fast = fast.next
  return slow

node4 = Node(4)
node3 = Node(3, node4)
node2 = Node(2, node3)
node1 = Node(1, node2)
node4.next = node2  # Creating a cycle
head = node1
cycle_start = get_loop_start(head)
if cycle_start:
  print(f"Cycle starts at node with value: {cycle_start.value}")  # Output: 2
else:
  print("No cycle detected")
print()

"""Problem 6: Was That a Crit?
Given the head of a singly linked list, return the number of critical points. A critical point is a local minima or maxima. - The head and tail nodes are not considered critical points. - A node is a local minima if both the next and previous elements are greater than the current element - A node is a local maxima if both the next and previous elements are greater than the current element.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity."""

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def count_critical_points(head):
  if head is None or head.next is None or head.next.next is None:
    return 0

  count = 0
  prev = head
  current = head.next
  next = head.next.next
  while next is not None:
    if (current.value > prev.value and current.value > next.value) or (current.value < prev.value and current.value < next.value):
      count += 1
    prev = current
    current = next
    next = next.next

  return count

head = Node(1, Node(2, Node(3, Node(3, Node(3, Node(5, Node(1, Node(3))))))))
print_linked_list(head)
print("Number of Critical points are: ", count_critical_points(head))
print()
# Input List: 1 -> 2 -> 3 -> 3 -> 3 -> 5 -> 1 -> 3
# Input: head = 3

# Expected Return Value: 2
# Explanation:
#  - Critical point 1 (local maxima) 3 -> 5 -> 1
#  - Critical point 2 (local minima): 5 -> 1 -> 3

"""Problem Set Version 3
Problem 1: The Power of One
The following code creates the linked list Ash -> Misty -> Brock. Refactor the code to create the same list with a single line of code."""

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

# Recreate this list in a single line of code
head = Node("Ash", Node("Misty", Node("Luigi", Node("Brock"))))
print_linked_list(head)
print()

"""Problem 2: Frequency Map
Given the head of a linked list, return a dictionary that maps each unique element in the list to its frequency.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity."""

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def frequency_map(head):
  if head is None or head.next is None:
    return {}

  freq = {}
  current = head
  while current:
    freq[current.value] = freq.get(current.value, 0) + 1
    current = current.next
  return freq

head = Node(1, Node(2, Node(3, Node(4, Node(2, Node(3))))))
print_linked_list(head)
print(frequency_map(head))
print()
# Input List: 1 -> 2 -> 3 -> 4 -> 2 -> 3
# Input: head = 1
# Expected Output: { 1: 1, 2: 2, 3: 2, 4: 1}

"""Problem 3: Get it Out of Here!
The following code attempts to remove the first node with a given value from a singly linked list based but it contains a bug!

Step 1: Copy this code into Replit.
Step 2: Create your own test cases to run the code against, and use print statements and the stack trace to identify and fix the bug so that the function correctly removes a node by value from the list."""

class Node:
  def __init__(self, value=None, next=None):
    self.value = value
    self.next = next

# Helper function to print the linked list
def print_list(node):
  current = node
  while current:
    print(current.value, end=" -> " if current.next else "")
    current = current.next
  print()

# Function with a bug!
def remove_by_value(head, val):
  # Handle empty list and removal from the head
  if not head:
    return None
  if head.value == val:
    return head.next  # Return the second node as the new head

  prev = head
  current = head.next
  while current:
    if current.value == val:
      prev.next = current.next  # Skip the node with the value
      return head  # Return the original head
    prev = current
    current = current.next

  # If no node was found with the value `val`, return the original head
  return head

val = 3
head = Node(1, Node(2, Node(3, Node(4))))
print_list(head)
print_list(remove_by_value(head, val))
# Input List: 1 -> 2 -> 3 -> 4
# Value to Remove: 3
# Expected Return Value: 1
# Expected Result List: 1 -> 2 -> 4
print()

"""Problem 4: Does it Cycle?
Given the head of a linked list, return True if the list has a cycle in it and false otherwise. A linked list has a cycle if at some point in the list, the node’s next pointer points back to a previous node in the list.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity."""

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def has_cycle(head):
  if head is None and head.next is None:
    return False

  slow, fast = head, head
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
      return True
  return False

node4 = Node(4)
node3 = Node(3, node4)
node2 = Node(2, node3)
node1 = Node(1, node2)
node4.next = node2  # Creating a cycle
head = node1
print("This linked list has a cycle:", has_cycle(head))
print()
# Input List:
# 1 -> 2 -> 3 -> 4
#      ^         | 
#      |---------|
# Input: head = 1
# True

"""Problem 5: Are We There Yet?
Given the head of a linked list, return the length of its cycle.
A linked list has a cycle if at some point in the list, the node’s next pointer points back to a previous node in the list.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity."""

class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def cycle_length(head):
  if head is None and head.next is None:
    return 0

  slow, fast = head, head
  count  = 0
  while fast and fast.next:
    count += 1
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
      return count

node4 = Node(4)
node3 = Node(3, node4)
node2 = Node(2, node3)
node1 = Node(1, node2)
node4.next = node2  # Creating a cycle
head = node1
print(cycle_length(head))
print()    
# Input List
# 1 -> 2 -> 3 -> 4
#      ^         |
#      |_________|
# Input: head = 1
# Output: 3

"""Problem 6: Reverse Them, K?
Given the head of a singly linked list and an integer k, reverse the first k elements of the linked list. Return the new head of the linked list. If k is larger than the length of the list, reverse the entire list.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity."""

class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def reverse_first_k(head, k):
  if head is None or k <= 1:
    return head

  dummy = Node(0)
  dummy.next = head
  prev = dummy

  next = None
  current = head
  count = 0
  while count < k and current:
    next = current.next
    current.next = prev
    prev = current
    current = next
    count += 1
  
  if count < k:
    dummy.next.next = None
    return prev

  dummy.next.next = current
  return prev

k = 3
head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print_list(head)
# Input List: 1 —> 2 —> 3 —> 4 —> 5
# Input: head = 1, k = 3
print_list(reverse_first_k(head, k))
# 3 -> 2 -> 1 -> 4 -> 5
print()

"""
# Session 2
# Problem Set Version 1
Problem 1: Detect Circular Linked List
A circular linked list is a linked list where the tail node points at the head node. Given the head of a linked list, write a function is_circular() that returns True if the linked list is circular and False otherwise.

Note: a circular list is more than just a cycle - specifically connecting the first and last nodes.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity."""
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def is_circular(head):
  if head is None:
    return False
  
  slow, fast = head, head
  while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
      return True
  return False
  
num1 = Node(1)
num2 = Node(2)
num3 = Node(3)
num1.next = num2
num2.next = num3
num3.next = num1
# num1 -> num2 -> num3 -> num1
print(is_circular(num1))

var1 = Node(1)
var2 = Node(2)
var3 = Node(3)
var1.next = var2
var2.next = var3
# var1 -> var2 -> var3
print(is_circular(var1))
print()

"""Problem 2: Find Last Node in a Linked List Cycle
Given the head of a singly linked list, write a function that returns the last node in the cycle. If there is no cycle in the linked list, return None."""

def find_last_node_in_cycle(head):
  if head is None:
    return None
  slow, fast = head, head
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
      return slow.value

num_4 = Node("num4")
num_3 = Node("num3", num_4)
num_2 = Node("num2", num_3)
num_1 = Node("num1", num_2)
num_4.next = num_2  # Creating a cycle
head = num_1
print(find_last_node_in_cycle(head))
# Example Input: num1 -> num2 -> num3 -> num4 -> num2
# Example Output: num4
print()

"""Problem 3: Partition List Around Value
Given the head of a linked list and a value val, partition a linked list around val such that all nodes with values less than val come before nodes with values greater than or equal to val."""

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def partition(head, val):
  if head is None:
    return None

  less_head = Node(0)
  less_tail = less_head
  greater_head = Node(0)
  greater_tail = greater_head

  current = head
  while current:
    if current.value < val:
      less_tail.next = current
      less_tail = less_tail.next
    else:
      greater_tail.next = current
      greater_tail = greater_tail.next
    current = current.next

  less_tail.next = greater_head.next
  greater_tail.next = None

  return less_head.next

val = 3
head = Node(1, Node(4, Node(3, Node(2, Node(5, Node(2))))))
print_linked_list(partition(head, val))

# 1 -> 4 -> 3 -> 2 -> 5 -> 2
# head = 1, val = 3
# Result Linked List: 1 -> 2 -> 2 -> 4 -> 3 -> 5 or 2 -> 2 -> 1 -> 5 -> 4 -> 3
print()

"""Problem 4: Convert Binary Number in a Linked List to Integer
You are given the head of a linked list. Each value in the linked list is either 0 or 1, and the entire linked list represents a binary number. Return an integer that is the decimal value of the number represented by the linked list. The most significant bit is at the head of the linked list."""

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def binary_to_int(head):
  if head is None:
    return 0

  count = 0
  bin_val = 0
  temp_head = head
  while temp_head:
    count += 1
    temp_head = temp_head.next

  current = head
  while current:
    bin_val += int(current.value) * 2**(count - 1)
    count -= 1
    current = current.next
  return bin_val

# 1 -> 0 -> 1
num1 = Node(1)
num2 = Node(0)
num3 = Node(1)
num1.next = num2
num2.next = num3
int_num = binary_to_int(num1)
# 101 in binary 
print(int_num) # Example Output: 5
print()

"""Problem 5: Add Two Numbers Represented by Linked Lists
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list."""

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def reverse_list(head):
  if head is None or head.next is None:
    return None

  # initialize three pointer
  prev = None
  next = None
  current = head

  # traverse the list and switch pointers
  while current:
    next = current.next
    current.next = prev
    prev = current
    current = next
  return prev

def get_val_from_list (head):
  current = head
  val_holder = ''
  while current:
    val_holder += str(current.value)
    current = current.next
  return val_holder

def add_two_numbers(head_a, head_b):
  if head_a is None or head_b is None or head_a.next is None or head_b.next is None:
    return None
    
  reversed_a = reverse_list(head_a)
  a_val = get_val_from_list(reversed_a)
  
  reversed_b = reverse_list(head_b)
  b_val = get_val_from_list(reversed_b)
  sum_val = int(a_val) + int(b_val)

  reversed_sum = str(sum_val)[::-1]
  return " -> ".join(str(reversed_sum))

# list 1: 2 -> 4 -> 3 (342)
# list 2: 5 -> 6 -> 4 (465)
# head_a = 2, head_b = 5

head_a = Node(2, Node(4, Node(3)))
head_b = Node(5, Node(6, Node(4)))
# print_list(reverse_list(head_b))
sum = add_two_numbers(head_a, head_b)
print(sum) # Explanation: 342 + 465 = 807, so the list is 7 -> 0 -> 8.
print()

"""Delete the Middle Node of a Linked List
You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x."""

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def deleteMiddle(head):
  if head is None or head.next is None:
      return None

  prev = None
  slow, fast = head, head

  while fast and fast.next:
      fast = fast.next.next
      prev = slow
      slow = slow.next

  prev.next = slow.next
  return head

head = Node(1, Node(3, Node(4, Node(7, Node(1, Node(2, Node(6)))))))
print_list(deleteMiddle(head))
print()


"""Intersection of Two Linked Lists
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null."""
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def getIntersectionNode(headA, headB):
  if not headA or not headB:
       return None

  ptrA = headA
  ptrB = headB
  while ptrA != ptrB:
      ptrA = ptrA.next if ptrA else headB
      ptrB = ptrB.next if ptrB else headA
  return ptrA.value

# Create the intersecting part
intersection = Node(8, Node(4, Node(5)))

# Create the nodes
headA = Node(4, Node(1, intersection))
headB = Node(5, Node(6, Node(1, intersection)))

# Test the function
result = getIntersectionNode(headA, headB)
print("The two nodes intersect at node:", getIntersectionNode(headA, headB))
print()

