# Session 1: OOP & Linked Lists
# Standard Problem Set Version 1
# '''Problem 1: New Horizons
# Step 1: Copy the following code into your IDE.

# # Step 2: Instantiate an instance of the class Villager, which represents characters in Animal Crossing. Store the instance in a variable named apollo.

# # The Villager object created should have the name "Apollo", the species "Eagle", and the catchphrase "pah".'''
# class Villager:
#     def __init__(self, name, species, catchphrase):
#         self.name = name
#         self.species = species
#         self.catchphrase = catchphrase
#         self.furniture = []

# # Instantiate your villager here
# apollo = Villager("Apollo", "Eagle", "pah")

# '''Problem 2: Greet Player
# Step 1: Using the Villager class from Problem 1, add the following greet_player() method to your existing code:

# def greet_player(self, player_name):
#     return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"
# Step 2: Create a second instance of Villager in a variable named bones.

# The Villager object created should have name "Bones", species "Dog", and catchphrase "yip yip".
# Step 3: Call the method greet_player() with your name and print out "Bones: Hey there, <your name>! 
# How's it going, yip yip!". For example, if your name is Tram, "Bones: Hey there, Tram! How's it going, yip yip?" would be printed out to the console.'''


# if __name__ == "__main__":
#     print("-------- # Session 1: OOP & Linked Lists -------- ")
#     print("------ # Standard Problem Set Version 1 ------ ")
#     print(apollo.name)  
#     print(apollo.species)  
#     print(apollo.catchphrase) 
#     print(apollo.furniture) 
#     print()
    # print(bones.name)
    # print(bones.species)  
    # print(bones.catchphrase) 
    # print(bones.furniture) 
    # print()


# '''Problem 4: Set Character
# In the previous exercise, we accessed and modified a player’s catchphrase attribute directly. Instead of allowing users to update their player directly, 
# it is common to create setter methods that users can call to update class attributes. This has a few different benefits, including allowing us to validate data before updating our class instance.

# Update your Villager class with a method set_catchphrase() that takes in one parameter new_catchphrase.

# If new_catchphrase is valid, it should update the villager's catchphrase attribute to have value new_catchphrase and print "Catchphrase updated".
# Otherwise, it should print out "Invalid catchphrase".
# Valid catchphrases are less than 20 characters in length. They must all contain only alphabetic and whitespace characters.'''
# import re
# class Villager:
#     def __init__(self, name, species, catchphrase):
#         self.name = name
#         self.species = species
#         self.catchphrase = catchphrase
#         self.furniture = []
	
#     def set_catchphrase(self, new_catchphrase):
#         if len(new_catchphrase) < 20 and re.match("^[A-Za-z ]+$", new_catchphrase):
#             self.catchphrase = new_catchphrase
#             print("Catchphrase updated!")
#         else:
#             print("Invalid catchphrase")
                
        
        
# alice = Villager("Alice", "Koala", "guvnor")

# alice.set_catchphrase("sweet dreams")
# print(alice.catchphrase)
# alice.set_catchphrase("#?!")
# print(alice.catchphrase)   

# '''Problem 5: Add Furniture
# Players and villagers in Animal Crossing can add furniture to their inventory to decorate their house.
# Update the Villager class with a new method add_item() that takes in one parameter, item_name.

# The method should validate the item_name.
# If the item is valid, add item_name to the player’s furniture attribute.
# The method does not need to return any values.
# item_name is valid if it has one of the following values: "acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", or "cacao tree".'''

# class Villager:
#     def __init__(self, name, species, catchphrase):
#         self.name = name
#         self.species = species
#         self.catchphrase = catchphrase
#         self.furniture = []
	
#     def set_catchphrase(self, new_catchphrase):
#         if len(new_catchphrase) < 20 and re.match("^[A-Za-z ]+$", new_catchphrase):
#             self.catchphrase = new_catchphrase
#             print("Catchphrase updated!")
#         else:
#             print("Invalid catchphrase")

#     def add_item(self, item_name):
#             valid_lst = ["acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"]
#             for item in valid_lst:
#                 if item == item_name:
#                     self.furniture.append(item_name)
    

    
# alice = Villager("Alice", "Koala", "guvnor")
# print(alice.furniture)

# alice.add_item("acoustic guitar")
# print(alice.furniture)

# alice.add_item("cacao tree")
# print(alice.furniture)

# alice.add_item("nintendo switch")
# print(alice.furniture)

# Session 2: Linked Lists
# Standard Problem Set Version 1
'''Problem 1: Mutual Friends
In the Villager class below, each villager has a friends attribute, which is a list of other villagers they are friends with.

Write a method get_mutuals() that takes one parameter, a Villager instance new_contact, 
and returns a list with the name of all friends the current villager and new_contact have in common.'''
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.friends = []

    def get_mutuals(self, new_contact):
        return [friend.name for friend in new_contact.friends if friend in self.friends]

bob = Villager("Bob", "Cat", "pthhhpth")
marshal = Villager("Marshal", "Squirrel", "sulky")
ankha = Villager("Ankha", "Cat", "me meow")
fauna = Villager("Fauna", "Deer", "dearie")
raymond = Villager("Raymond", "Cat", "crisp")
stitches = Villager("Stitches", "Cub", "stuffin")

bob.friends = [stitches, raymond, fauna]
marshal.friends = [raymond, ankha, fauna]
print(bob.get_mutuals(marshal))

ankha.friends = [marshal]
print(bob.get_mutuals(ankha))
print()

'''Problem 2: Linked Up
A linked list is a data structure that, similar to a normal list or array, allows us to store pieces of data sequentially. 
The key difference is how the elements are stored in memory.

In a normal list, elements are stored in adjacent memory locations. If we know the location of the first element, we can easily access any other element in the list.
In a linked list, individual elements, called nodes, are not stored in sequential memory locations. 
Instead, each node stores a reference or pointer to the next node in the list, allowing us to traverse the list.

Connect the provided node instances below to create the linked list kk_slider -> harriet -> saharah -> isabelle.
A function print_linked_list() which accepts the head, or first element, of a linked list and prints the values of the list has also been provided for testing purposes.'''

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

kk_slider = Node("K.K. Slider")
harriet = Node("Harriet")
saharah = Node("Saharah")
isabelle = Node("Isabelle")
kk_slider.next = harriet
harriet.next = saharah
saharah.next = isabelle
print_linked_list(kk_slider)

'''Problem 3: Daily Tasks
Imagine a linked list used as a daily task list where each node represents a task. 
Write a function add_task() that takes in the head of a linked list and adds a new node to the front of the task list.

The function should insert a new Node object with the value task as the new head of the linked list and return the new node.

Note: The "head" of a linked list is the first element in the linked list. It is equivalent to lst[0] of a normal list.'''

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

def add_first(head, task):
    new_node = Node(task)
    new_node.next = head
    return new_node

task_1 = Node("shake tree")
task_2 = Node("dig fossils")
task_3 = Node("catch bugs")
task_1.next = task_2
task_2.next = task_3

# Linked List: shake tree -> dig fossils -> catch bugs
print_linked_list(add_first(task_1, "check turnip prices"))

'''Problem 4: Halve List
Write a function halve_list() that accepts the head of a linked list whose values are integers and divides each value by two. Return the head of the modified list.'''
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

def halve_list(head):


node_one = Node(5)
node_two = Node(6)
node_three = Node(7)
node_one.next = node_two
node_two.next = node_three

# Input List: 5 -> 6 -> 7
print_linked_list(halve_list(node_one))

'''Problem 5: Remove Last
Write a function delete_tail() that accepts the head of a linked list and removes the last node in the list. Return the head of the modified list.

Note: The "tail" of a list is the last element in the linked list. It is equivalent to lst[-1] in a normal list.'''
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

def delete_tail(head):
    pass

butterfly = Node("Common Butterfly")
ladybug = Node("Ladybug")
beetle = Node("Scarab Beetle")
butterfly.next = ladybug
ladybug.next = beetle

# Input List: butterfly -> ladybug -> beetle
print_linked_list(delete_tail(butterfly))