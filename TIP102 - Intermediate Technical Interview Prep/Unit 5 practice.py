# Session 1: OOP & Linked Lists
# Standard Problem Set Version 1
'''Problem 1: New Horizons
Step 1: Copy the following code into your IDE.

# Step 2: Instantiate an instance of the class Villager, which represents characters in Animal Crossing. Store the instance in a variable named apollo.

# The Villager object created should have the name "Apollo", the species "Eagle", and the catchphrase "pah".'''
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

# Instantiate your villager here
apollo = Villager("Apollo", "Eagle", "pah")

'''Problem 2: Greet Player
Step 1: Using the Villager class from Problem 1, add the following greet_player() method to your existing code:

def greet_player(self, player_name):
    return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"
Step 2: Create a second instance of Villager in a variable named bones.

The Villager object created should have name "Bones", species "Dog", and catchphrase "yip yip".
Step 3: Call the method greet_player() with your name and print out "Bones: Hey there, <your name>! 
How's it going, yip yip!". For example, if your name is Tram, "Bones: Hey there, Tram! How's it going, yip yip?" would be printed out to the console.'''
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []
    
    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"
    
# second instance of `Villager` in variable named "bones"
bones = Villager("Bones", "Dog", "yip yip")
    
'''Problem 3: Update Catchphrase
In Animal Crossing, as players become friends with villagers, the villagers might ask the player to suggest a new catchphrase.

Adding on to your existing code, update bones so that his catchphrase is "ruff it up" instead of its current value, "yip yip".
'''
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []
    
    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"

'''Problem 4: Set Character
In the previous exercise, we accessed and modified a player’s catchphrase attribute directly. Instead of allowing users to update their player directly, 
it is common to create setter methods that users can call to update class attributes. This has a few different benefits, including allowing us to validate data before updating our class instance.

Update your Villager class with a method set_catchphrase() that takes in one parameter new_catchphrase.

If new_catchphrase is valid, it should update the villager's catchphrase attribute to have value new_catchphrase and print "Catchphrase updated".
Otherwise, it should print out "Invalid catchphrase".
Valid catchphrases are less than 20 characters in length. They must all contain only alphabetic and whitespace characters.'''
import re
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []
	
    def set_catchphrase(self, new_catchphrase):
        if len(new_catchphrase) < 20 and re.match("^[A-Za-z ]+$", new_catchphrase):
            self.catchphrase = new_catchphrase
            print("Catchphrase updated!")
        else:
            print("Invalid catchphrase")

alice = Villager("Alice", "Koala", "guvnor")
                
'''Problem 5: Add Furniture
Players and villagers in Animal Crossing can add furniture to their inventory to decorate their house.
Update the Villager class with a new method add_item() that takes in one parameter, item_name.

The method should validate the item_name.
If the item is valid, add item_name to the player’s furniture attribute.
The method does not need to return any values.
item_name is valid if it has one of the following values: "acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", or "cacao tree".'''

class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []
	
    def set_catchphrase(self, new_catchphrase):
        if len(new_catchphrase) < 20 and re.match("^[A-Za-z ]+$", new_catchphrase):
            self.catchphrase = new_catchphrase
            print("Catchphrase updated!")
        else:
            print("Invalid catchphrase")

    def add_item(self, item_name):
            valid_lst = ["acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"]
            if item_name in valid_lst:
                self.furniture.append(item_name)

alice = Villager("Alice", "Koala", "guvnor")
    
'''Problem 6: Print Inventory
Update the Villager class with a method print_inventory() that accepts no parameters except for self.

The method should print the name and quantity of each item in a villager’s furniture list.

The name and quantity should be in the format "item1: quantity, item2: quantity, item3: quantity" for however many unique items exist in the villager's furniture list
If the player has no items, the function should print "Inventory empty".'''
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []
	
    def set_catchphrase(self, new_catchphrase):
        if len(new_catchphrase) < 20 and re.match("^[A-Za-z ]+$", new_catchphrase):
            self.catchphrase = new_catchphrase
            print("Catchphrase updated!")
        else:
            print("Invalid catchphrase")

    def add_item(self, item_name):
            valid_lst = ["acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"]
            if item_name in valid_lst:
                self.furniture.append(item_name)
        
    def print_inventory(self):
        # check if inventory is empty
        if self.furniture == []:
            print("Inventory empty")
        else: 
            item_dict = {}
            for item in self.furniture:
                if item in item_dict:
                    item_dict[item] += 1
                else:
                    item_dict[item] = 1
                
            parts = [f"{item}: {item_dict[item]}" for item in item_dict]
            print(", ".join(parts))

alice = Villager("Alice", "Koala", "guvnor")


'''Problem 7: Group by Personality
The Villager class has been updated below to include the new string attribute personality representing the character's personality type.

Outside of the Villager class, write a function of_personality_type(). Given a list of Villager instances townies and a string personality_type as parameters, 
return a list containing the names of all villagers in townies with personality personality_type. Return the names in any order.'''       
class Villager:
    def __init__(self, name, species, personality, catchphrase):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
	
    def set_catchphrase(self, new_catchphrase):
        if len(new_catchphrase) < 20 and re.match("^[A-Za-z ]+$", new_catchphrase):
            self.catchphrase = new_catchphrase
            print("Catchphrase updated!")
        else:
            print("Invalid catchphrase")

    def add_item(self, item_name):
            valid_lst = ["acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"]
            for item in valid_lst:
                if item == item_name:
                    self.furniture.append(item_name)
        
    def print_inventory(self):
        # check if inventory is empty
        if not self.furniture:
            print("Inventory empty")
        else: 
            item_dict = {}
            for item in self.furniture:
                if item in item_dict:
                    item_dict[item] += 1
                else:
                    item_dict[item] = 1
                
            parts = [f"{item}: {item_dict[item]}" for item in item_dict]
            print(", ".join(parts))

def of_personality_type(townies, personality_type):
    names = []
    for villager in townies:
        if villager.personality == personality_type:
            names.append(villager.name)
    return names

'''Problem 8: Telephone
The Villager constructor has been updated to include an additional attribute neighbor. A villager's neighbor is another Villager instance and represents their closest neighbor. 
By default, a Villager's neighbor is set to None.

Given two Villager instances start_villager and target_villager, write a function message_received() that returns True 
if you can pass a message from the start_villager to the target_villager through a series of neighbors and False otherwise.'''
class Villager:
    def __init__(self, name, species, personality, catchphrase, neighbor=None):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
        self.neighbor = neighbor
	
    def set_catchphrase(self, new_catchphrase):
        if len(new_catchphrase) < 20 and re.match("^[A-Za-z ]+$", new_catchphrase):
            self.catchphrase = new_catchphrase
            print("Catchphrase updated!")
        else:
            print("Invalid catchphrase")

    def add_item(self, item_name):
            valid_lst = ["acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"]
            for item in valid_lst:
                if item == item_name:
                    self.furniture.append(item_name)
        
    def print_inventory(self):
        # check if inventory is empty
        if not self.furniture:
            print("Inventory empty")
        else: 
            item_dict = {}
            for item in self.furniture:
                if item in item_dict:
                    item_dict[item] += 1
                else:
                    item_dict[item] = 1
                
            parts = [f"{item}: {item_dict[item]}" for item in item_dict]
            print(", ".join(parts))

def message_received(start_villager, target_villager):
    visited = set()
    current = start_villager

    while current is not None and current not in visited:
        if current == target_villager:
            return True
        
        visited.add(current)
        current = current.neighbor
    return False

'''Problem 9: Nook's Cranny
A linked list is a new data type that, similar to a normal list or array, allows us to store pieces of data sequentially. 
The difference between a linked list and a normal list lies in how each element is stored in a computer’s memory.

In a normal list, individual elements of the list are stored in adjacent memory locations according to the order they appear in the list. 
If we know where the first element of the list is stored, it’s really easy to find any other element in the list.

In a linked list, the individual elements called nodes are not stored in sequential memory locations. Each node may be stored in an unrelated memory location. 
To connect nodes together into a sequential list, each node stores a reference or pointer to the next node in the list.

Using the provided Node class below, create a linked list Tom Nook -> Tommy where the instance tom_nook has value "Tom Nook" which points to the instance tommy that has value "Tommy".'''
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

'''Problem 10: Timmy and Tommy
In a linked list, pointers can be redirected to any place in the list.

Using the linked list from Problem 9, create a new Node timmy with value "Timmy" and place it between tom_nook and tommy so the new linked list is tom_nook -> timmy -> tommy.'''
timmy = Node("Timmy")

'''Problem 11: Saharah
Using the linked list from Problem 10, remove the tom_nook node and add in a node saharah with value "Saharah" to the end of the list so that the resulting list is timmy -> tommy -> saharah.'''
saharah = Node("Saharah")

'''Problem 12: Print List
Write a function print_list() that takes in the head of a linked list and returns a string linking together the values of the list with the separator "->".

Note: The "head" of a linked list is the first element in the linked list. Equivalent to lst[0] of a normal list.'''
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end = " -> " if current.next else "\n")
        current = current.next
    return 

# Standard Problem Set Version 2
'''Problem 1: Player Class
Step 1: Copy the following code into your IDE.

Step 2: Instantiate an instance of the class Player and store it in a variable named player_one.

The Player object should have the character "Yoshi" and the kart "Super Blooper".'''
class Player:
    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []

player_one = Player("Yoshi", "Super Blooper")

'''Problem 2: Get Player
Step 1: Using the Player class from Problem 1, add the following get_player() method to your existing code:

def get_player(self):
    return f"{self.character} driving the {self.kart}"
Step 2: Create a second instance of Player in a variable named player_two.

The Player object created should have character "Bowser" and kart "Pirahna Prowler".
Step 3: Use the method get_player() below to print out "Match: Yoshi driving the Super Blooper vs Bowser driving the Pirahna Prowler".'''
class Player:
    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []

    def get_player(self):
        return f"{self.character} driving the {self.kart}"
    
player_two = Player("Bowser", "Pirahna Prowler")

'''Problem 3: Update Kart
Players might want to update their choice of kart for their next race.

Update player_one so that their kart is "Dolphin Dasher" instead of its current value, "Super Blooper".'''
class Player:
    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []

    def get_player(self):
        return f"{self.character} driving the {self.kart}"

player_one = Player("Yoshi", "Super Blooper")

'''Problem 4: Set Character
In the previous exercise, we accessed and modified a player’s kart attribute directly. Instead of allowing users to update their player directly, 
it is common to create setter methods that users can call to update class attributes. This has a few different benefits, including allowing us to validate data before updating our class instance.

Update your Player class with a method set_character() that takes in one parameter name.

If name is valid, it should update the player’s character attribute to have value name and print "Character updated".
Otherwise, it should print out "Invalid character".
Valid character names are "Mario", "Luigi", "Peach", "Yoshi", "Toad", "Wario", "Donkey Kong", and "Bowser".'''
class Player():
    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []
        
    def set_character(self, name):
        valid_names = ["Mario", "Luigi", "Peach", "Yoshi", "Toad", "Wario", "Donkey Kong", "Bowser"]
        if name in valid_names:
            self.character = name
            print("Character Updated")
        else:
            print("Invalid Character")
        return self.character

player_three = Player("Donkey Kong", "Standard Kart")

'''Problem 5: Add Special Item
Players can pick up special items as they race.

Update the Player class with a new method add_item() that takes in one parameter, item_name.

The method should validate the item_name.

If the item is valid, add item_name to the player’s items attribute.
The method does not need to return any values.
item_name is valid if it has one of the following values: "banana", "green shell", "red shell", "bob-omb", "super star", "lightning", "bullet bill".'''

class Player():
    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []
        
    def add_item(self, item_name):
        valid_items = ["banana", "green shell", "red shell", "bob-omb", "super star", "lightning", "bullet bill", "super smash"]
        if item_name in valid_items:
            self.items.append(item_name)

'''Problem 6: Print Inventory
Update the Player class with a method print_inventory() that accepts no parameters except for self.

The method should print the name and quantity of each item in a player’s items list.

If the player has no items, the function should print "Inventory empty".
'''
class Player():
    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []
        
    def add_item(self, item_name):
        valid_items = ["banana", "green shell", "red shell", "bob-omb", "super star", "lightning", "bullet bill", "super smash"]
        if item_name in valid_items:
            self.items.append(item_name)

    def print_inventory(self):
        if self.items == []:
            print("Inventory empty")
        else:
            item_freq = {}
            for item in self.items:
                if item in item_freq:
                    item_freq[item] += 1
                else:
                    item_freq[item] = 1
            
            inventory = [f"{item}: {item_freq[item]}" for item in item_freq]
            print(f"Inventory: ", ", ".join(inventory))

'''Problem 7: Race Results
Given a list race_results of Player objects where the first player in the list came first in the race, second player in the list came second, etc., write a function print_results() that prints the players in place.'''
class Player():
    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []
        
    def add_item(self, item_name):
        valid_items = ["banana", "green shell", "red shell", "bob-omb", "super star", "lightning", "bullet bill", "super smash"]
        if item_name in valid_items:
            self.items.append(item_name)

    def print_inventory(self):
        if self.items == []:
            print("Inventory empty")
        else:
            item_freq = {}
            for item in self.items:
                if item in item_freq:
                    item_freq[item] += 1
                else:
                    item_freq[item] = 1
            
            inventory = [f"{item}: {item_freq[item]}" for item in item_freq]
            print(f"Inventory: ", ", ".join(inventory))

def print_results(race_results):
    for i, result in enumerate(race_results):
        print(f"{i+1}. {result.character}")

'''Problem 8: Get Rank
The Player class has been updated below with a new attribute ahead to represent the player currently directly ahead of them in the race.

Write a function get_rank() that accepts a Player object my_player and returns their current place number in the race.'''
class Players:
    def __init__(self, character, kart, opponent=None):
        self.character = character
        self.kart = kart
        self.items = []
        self.ahead = opponent
        
def get_rank(my_player):
    rank = 1
    current = my_player
    while current.ahead is not None:
        rank += 1
        current = current.ahead
    return rank

'''Problem 9: Tom and Jerry
A linked list is a new data type that, similar to a normal list or array, allows us to store pieces of data sequentially. The difference between a linked list and a normal list lies in how each element is stored in a computer’s memory.

In a normal list, individual elements of the list are stored in adjacent memory locations according to the order they appear in the list. If we know where the first element of the list is stored, it’s really easy to find any other element in the list.

In a linked list, the individual elements called nodes are not stored in sequential memory locations. Each node may be stored in an unrelated memory location. 
To connect nodes together into a sequential list, each node stores a reference or pointer to the next node in the list.

Using the provided Node class below, create a linked list cat -> mouse where the instance cat has value "Tom" which points to the instance mouse that has value "Jerry".'''
mouse = Node("Jerry")
cat = Node("Tom", mouse)

'''Problem 10: Chase List
In a linked list, pointers can be redirected at any place in the list. Using the linked list from Problem 9, create a new Node dog with value "Spike" and point it to the cat node so that the full list now looks like dog -> cat -> mouse.'''
dog = Node("Spike", cat)

'''Problem 11: Update Chase
Using the linked list from Problem 10, remove the dog node and add in a node cheese with value "Gouda" to the end of the list so that the resulting list is cat -> mouse -> cheese.'''
cheese = Node("Gouda")
mouse = Node("Jerry", cheese)
cat = Node("Tom", mouse)

'''Problem 12: Chase String
Write a function chase_list() that takes in the head of a linked list and returns a string linking together the values of the list with the separator "chases".

Note: The "head" of a linked list is the first element in the linked list, equivalent to lst[0] of a normal list.'''
def chase_list(head):
    if head is None:
        return ""
    
    current = head 
    while current is not None:
        print(current.value, end = " chases " if current.next else "\n")
        current = current.next
    return 

# Advanced Problem Set Version 1
'''Problem 6: Got One!
Imagine that behind the scenes, Animal Crossing uses a linked list to represent the order fish will appear to a player who is fishing in the river. The head of the list represents the next fish that a player will catch if they keep fishing.

Write a function catch_fish() that accepts the head of a list. The function should:

Print the name of the fish in the head node using the format "I caught a <fish name>!".
Remove the first node in the list.
The function should return the new head of the list. If the list is empty, print "Aw! Better luck next time!" and return None.

A function print_linked_list() which accepts the head, or first element, of a linked list and prints the list data has also been provided for testing purposes.'''
class Node_fish:
    def __init__(self, fish_name, next=None):
        self.fish_name = fish_name
        self.next = next

# For testing
def print_linked_list_fish(head):
    current = head
    while current:
        print(current.fish_name, end=" -> " if current.next else "\n")
        current = current.next

def catch_fish(head):
    if not head:
        print("Aw! Better luck next time!")
        return None
    
    print(f"I caught a {head.fish_name}!")
    new_head = head.next
    return new_head

'''Problem 7: Fishing Probability
Imagine that Animal Crossing is still using a linked list to represent the order fish will appear to a player who is fishing in the river! 
The head of the list represents the next fish that a player will catch if they keep fishing.

Write a function fish_chances() that accepts the head of a list and a string fish_name. Return the probability rounded down to the nearest hundredth that the player will catch a fish of type fish_name.

A function print_linked_list() which accepts the head, or first element, of a linked list and prints the list data has also been provided for testing purposes.'''
class Node_fish:
    def __init__(self, fish_name, next=None):
        self.fish_name = fish_name
        self.next = next

def fish_chances(head, fish_name):
    current = head 
    count = 0
    fish_val = 0
    while current:
        if current.fish_name == fish_name:
            fish_val += 1
        current = current.next
        count += 1
    return "{:.2f}".format(0) if fish_val == 0 else round((fish_val / count), 2)

'''Problem 8: Restocking the Lake
Imagine that Animal Crossing is still using a linked list to represent the order fish will appear to a player who is fishing! The head of the list represents the next fish that a player will catch if they keep fishing.

Write a function restock() that accepts the head of a linked list and a string new_fish, and adds a Node with the fish_name new_fish to the end of the list. Return the head of the modified list.

A function print_linked_list() which accepts the head, or first element, of a linked list and prints the list data has also been provided for testing purposes.'''
class Node_fish:
    def __init__(self, fish_name, next=None):
        self.fish_name = fish_name
        self.next = next

def restock(head, new_fish):
    new_node = Node_fish(new_fish)

    # if list is empty, return new_node
    if head is None:
        return new_node
    
    # traverse to the end of the list
    current = head
    while current.next:
        current = current.next

    # add new node at the end
    current.next = new_node
    return head


# Session 2: Linked Lists
# Standard Problem Set Version 1
'''Problem 1: Mutual Friends
In the Villager class below, each villager has a friends attribute, which is a list of other villagers they are friends with.

Write a method get_mutuals() that takes one parameter, a Villager instance new_contact, 
and returns a list with the name of all friends the current villager and new_contact have in common.'''
class Villager_two:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.friends = []

    def get_mutuals(self, new_contact):
        return [friend.name for friend in new_contact.friends if friend in self.friends]

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
    if head is None:
        return head 
    
    current = head
    current.value = head.value / 2
    while current.next:
        current = current.next 
        current.value = current.value / 2
    return head

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
    if head is None:
        return None
    
    if head.next is None:
        return None 

    # find the second to the last node
    current = head
    while current.next.next:
        current = current.next
    
    current.next = None
    return head

'''Problem 6: Find Minimum in Linked List
Write a function find_min() that takes in the head of a linked list and returns the minimum value in the linked list. You can assume the linked list will contain only numeric values.'''
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

def find_min(head):
    # base case
    if head is None:
        return head 
    
    min_val = float('inf')
    current = head 
    while current:
        if current.value < min_val:
            min_val = current.value 
        current = current.next
    return min_val

'''Problem 7: Remove From Inventory
Imagine a linked list used to store a player's inventory. Write a function delete_item() that takes in the head of a linked list and a value item as parameters.

The function should remove the first node it finds in the linked list with the value item and return the head of the modified list. If no node can be found with the value item, return the list unchanged.'''
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

def delete_item(head, item):
    if head is None:
        return None
    
    if head.value == item:
        return head.next

    prev = head
    current = head.next
    while current is not None:
        if current.value == item:
            prev.next = current.next
            break
        prev = current
        current = current.next
    return head
    
'''Problem 8: Move Tail to Front of Linked List
Write a function tail_to_head() that takes in the head of a linked list as a parameter and moves the tail of the linked list to the front.'''
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

def tail_to_head(head):
    # if the list is empty or has only one node, nothing changes
    if head is None or head.next is None:
        return head 
    
    # traverse to the second-to-last node
    current = head
    while current.next.next is not None:
        current = current.next
        
    # 'current' now points to the second-to-last node
    tail = current.next
    current.next = None

    # move the old tail to the front
    tail.next = head
    head = tail
    return head

'''Problem 9: Create Double Links
One of the drawbacks of a linked list is that it's difficult to go backwards because each Node only knows about the Node in front of it. (E.g., A -> B -> C)

A doubly linked list solves this problem! Instead of just having a next attribute, a doubly linked list also has a prev attribute that points to the Node before it. (E.g., A <-> B <-> C)

Update the Node constructor below so that the code creates a doubly linked list with head <-> tail.'''
class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

# link them in both directions
head = Node("Isabelle")
tail = Node("K.K. Slider")

# demonstrate the bidirectional links
head.next = tail
tail.prev = head

'''Problem 10: Print Backwards
Write a function print_reverse() that takes in the tail of a doubly linked list as a parameter.

It should print out the values of the linked list in reverse order, each separated by a space.'''
class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

def print_reverse(tail):
    # if list is empty, return nothing
    if tail is None:
        return 
    
    current = tail
    while current is not None:
        print(current.value, end="  " if current.prev else "\n")
        current = current.prev



if __name__ == "__main__":
    print("-------- # Session 1: OOP & Linked Lists -------- ")
    print("------ # Standard Problem Set Version 1 ------ ")
    print("Problem 1: New Horizons")
    print(apollo.name)  
    print(apollo.species)  
    print(apollo.catchphrase) 
    print(apollo.furniture) 
    print()
    print("Problem 2: Greet Player")
    print(bones.name)
    print(bones.species)  
    print(bones.catchphrase) 
    print(bones.furniture) 
    print(bones.greet_player("Chuks"))
    print()
    print("Problem 3: Update Catchphrase")
    bones.catchphrase = "ruff it up"
    print(bones.greet_player("Samia"))
    print()
    print("Problem 4: Set Character")
    alice.set_catchphrase("sweet dreams")
    print(alice.catchphrase)
    alice.set_catchphrase("#?!")
    print(alice.catchphrase)   
    print()
    print("Problem 5: Add Furniture")
    print(alice.furniture)
    alice.add_item("acoustic guitar")
    print(alice.furniture)
    alice.add_item("cacao tree")
    print(alice.furniture)
    alice.add_item("nintendo switch")
    print(alice.furniture)
    print()
    print("Problem 6: Print Inventory")
    alice.furniture = []
    alice.print_inventory()
    alice.furniture = ["acoustic guitar", "ironwood kitchenette", "kotatsu", "kotatsu"]
    alice.print_inventory()
    print()
    print("Problem 7: Group by Personality")
    isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
    bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
    stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")
    print(of_personality_type([isabelle, bob, stitches], "Lazy"))
    print(of_personality_type([isabelle, bob, stitches], "Cranky"))
    print()
    print("Problem 8: Telephone")
    isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
    tom_nook = Villager("Tom Nook", "Raccoon", "Cranky", "yes, yes")
    kk_slider = Villager("K.K. Slider", "Dog", "Lazy", "dig it")
    isabelle.neighbor = tom_nook
    tom_nook.neighbor = kk_slider
    print(message_received(isabelle, kk_slider))
    print(message_received(kk_slider, isabelle))
    print()
    print("Problem 9: Nook's Cranny")
    tom_nook = Node("Tom Nook")
    tommy = Node("Tommy") 
    tom_nook.next = tommy 
    print(tom_nook.value) 
    print(tom_nook.next.value) 
    print(tommy.value) 
    print(tommy.next) 
    print(f"{tom_nook.value} -> {tommy.value}")
    print()
    print("Problem 10: Timmy and Tommy")
    tom_nook = Node("Tom Nook")
    tommy = Node("Tommy") 
    timmy = Node("Timmy")
    tom_nook.next = timmy 
    timmy.next = tommy
    print(tom_nook.value)
    print(tom_nook.next.value)
    print(timmy.value)
    print(timmy.next.value)
    print(tommy.value)
    print(tommy.next)
    print(f"{tom_nook.value} -> {timmy.value} -> {tommy.value}")
    print()
    print("Problem 11: Saharah")
    tom_nook = Node("")
    saharah = Node("Saharah")
    tommy.next = saharah
    print(tom_nook.next) 
    print(timmy.value) 
    print(timmy.next.value)  
    print(tommy.value) 
    print(tommy.next.value)
    print(saharah.value)  
    print(saharah.next) 
    print()
    print("Problem 12: Print List")
    isabelle = Node("Isabelle")
    saharah = Node("Saharah")
    cj = Node("C.J.")
    isabelle.next = saharah
    saharah.next = cj
    print_linked_list(isabelle)
    print()
    print("------ # Standard Problem Set Version 2 ------ ")
    print("Problem 1: Player Class")
    print(player_one.character)
    print(player_one.kart)
    print(player_one.items)
    print()
    print("Problem 2: Get Player")
    print(player_two.character)
    print(player_two.kart)
    print(player_two.items)
    print(f"Match: {player_one.character} driving the {player_one.kart} vs {player_two.character} driving the {player_two.kart}")
    print()
    print("Problem 3: Update Kart")
    player_one.kart = "Dolphin Dasher"
    print(player_one.get_player())
    print()
    print("Problem 4: Set Character")
    player_three.set_character("Peach")
    print(player_three.character)
    player_three.set_character("Baby Peach")
    print(player_three.character)
    print()
    print("Problem 5: Add Special Item")
    player_one = Player("Yoshi", "Dolphin Dasher")
    print(player_one.items)

    player_one.add_item("red shell")
    print(player_one.items)

    player_one.add_item("super star")
    print(player_one.items)

    player_one.add_item("super smash")
    print(player_one.items)
    print()
    print("Problem 6: Print Inventory")
    player_one = Player("Yoshi", "Super Blooper")
    player_one.items = ["banana", "bob-omb", "banana", "super star"]
    player_two = Player("Peach", "Dolphin Dasher")

    player_one.print_inventory()
    player_two.print_inventory()
    print()
    print("Problem 7: Race Results")
    peach = Player("Peach", "Daytripper")
    mario = Player("Mario", "Standard Kart M")
    luigi = Player("Luigi", "Super Blooper")
    race_one = [peach, mario, luigi]

    print_results(race_one)
    print()
    print("Problem 8: Get Rank")
    peach = Players("Peach", "Daytripper")
    mario = Players("Mario", "Standard Kart M", peach)
    luigi = Players("Luigi", "Super Blooper", mario)
    print(get_rank(luigi))
    print(get_rank(peach))
    print(get_rank(mario))
    print()
    print("Problem 9: Tom and Jerry")
    print_linked_list(cat)
    print(cat.value)
    print(cat.next)
    print(cat.next.value)
    print(mouse.value)
    print(mouse.next)
    print()
    print("Problem 10: Chase List")
    print_linked_list(dog)
    print(dog.value)
    print(dog.next)
    print(dog.next.value)
    print(cat.next)
    print(cat.next.value)
    print(mouse.next)
    print()
    print("Problem 11: Update Chase")
    print_linked_list(cat)
    print()
    print("Problem 12: Chase String")
    dog = Node("Spike")
    cat = Node("Tom")
    mouse = Node("Jerry")
    cheese = Node("Gouda")
    dog.next = cat
    cat.next = mouse
    mouse.next = cheese
    chase_list(dog)
    print()
    print("------ # Advanced Problem Set Version 1 ------ ")
    print("Problem 6: Got One!")
    fish_list = Node_fish("Carp", Node_fish("Dace", Node_fish("Cherry Salmon")))
    empty_list = None

    print_linked_list_fish(fish_list)
    print_linked_list_fish(catch_fish(fish_list))
    print(catch_fish(empty_list))
    print()
    print("Problem 7: Fishing Probability")
    fish_list = Node_fish("Carp", Node_fish("Dace", Node_fish("Cherry Salmon")))
    print(fish_chances(fish_list, "Dace"))
    print(fish_chances(fish_list, "Rainbow Trout"))
    print()
    print("Problem 8: Restocking the Lake")
    fish_list = Node_fish("Carp", Node_fish("Dace", Node_fish("Cherry Salmon")))
    print_linked_list_fish(restock(fish_list, "Rainbow Trout"))
    print()
    print("-------- # Session 2: Linked Lists -------- ")
    print("------ # Standard Problem Set Version 1 ------ ")
    print("Problem 1: Mutual Friends")
    bob = Villager_two("Bob", "Cat", "pthhhpth")
    marshal = Villager_two("Marshal", "Squirrel", "sulky")
    ankha = Villager_two("Ankha", "Cat", "me meow")
    fauna = Villager_two("Fauna", "Deer", "dearie")
    raymond = Villager_two("Raymond", "Cat", "crisp")
    stitches = Villager_two("Stitches", "Cub", "stuffin")

    bob.friends = [stitches, raymond, fauna]
    marshal.friends = [raymond, ankha, fauna]
    print(bob.get_mutuals(marshal))

    ankha.friends = [marshal]
    print(bob.get_mutuals(ankha))
    print()
    print("Problem 2: Linked Up")
    kk_slider = Node("K.K. Slider")
    harriet = Node("Harriet")
    saharah = Node("Saharah")
    isabelle = Node("Isabelle")
    kk_slider.next = harriet
    harriet.next = saharah
    saharah.next = isabelle
    print_linked_list(kk_slider)
    print()
    print("Problem 3: Daily Tasks")
    task_1 = Node("shake tree")
    task_2 = Node("dig fossils")
    task_3 = Node("catch bugs")
    task_1.next = task_2
    task_2.next = task_3
    # Linked List: shake tree -> dig fossils -> catch bugs
    print_linked_list(add_first(task_1, "check turnip prices"))
    print()
    print("Problem 4: Halve List")
    node_one = Node(5)
    node_two = Node(6)
    node_three = Node(7)
    node_one.next = node_two
    node_two.next = node_three
    # Input List: 5 -> 6 -> 7
    print_linked_list(halve_list(node_one))
    print()
    print("Problem 5: Remove Last")
    butterfly = Node("Common Butterfly")
    ladybug = Node("Ladybug")
    beetle = Node("Scarab Beetle")
    butterfly.next = ladybug
    ladybug.next = beetle
    # Input List: butterfly -> ladybug -> beetle
    print_linked_list(delete_tail(butterfly))
    print()
    print("Problem 6: Find Minimum in Linked List")
    head1 = Node(5, Node(6, Node(7, Node(8))))
    head2 = Node(8, Node(5, Node(6, Node(7))))

    # Linked List: 5 -> 6 -> 7 -> 8
    print(find_min(head1))

    # Linked List: 8 -> 5 -> 6 -> 7
    print(find_min(head2))
    print()
    print("Problem 7: Remove From Inventory")
    slingshot = Node("Slingshot")
    peaches = Node("Peaches")
    beetle = Node("Scarab Beetle")
    slingshot.next = peaches
    peaches.next = beetle
    # Linked List: slingshot -> peaches -> beetle
    print_linked_list(delete_item(slingshot, "Peaches"))
    # Linked List: slingshot -> beetle
    print_linked_list(delete_item(slingshot, "Triceratops Torso"))
    print()
    print("Problem 8: Move Tail to Front of Linked List")
    daisy = Node("Daisy")
    mario = Node("Mario")
    toad = Node("Toad") 
    peach = Node("Peach")
    daisy.next = mario
    mario.next = toad
    toad.next = peach

    # Linked List: Daisy -> Mario -> Toad -> Peach
    print_linked_list(tail_to_head(daisy))
    print()
    print("Problem 9: Create Double Links")
    print(head.value, "<->", head.next.value)
    print(tail.prev.value, "<->", tail.value)
    print()
    print("Problem 10: Print Backwards")
    isabelle = Node("Isabelle")
    kk_slider = Node("K.K. Slider")
    saharah = Node("Saharah")
    isabelle.next = kk_slider
    kk_slider.next = saharah
    saharah.prev = kk_slider
    kk_slider.prev = isabelle

    # Linked List: Isabelle <-> K.K. Slider <-> Saharah
    print_reverse(saharah)
    print()