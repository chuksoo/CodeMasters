# attributes: title, length, likes, comments, quality
class Video:
  def __init__(self, title, length, likes, comments, quality):
    self.title = title
    self.length = length
    self.likes = likes
    self.comments = comments
    self.quality = quality

  def isTrending(self, comments):
    return comments > 100

video = Video('Democracy', 20, 5, 10, 720)
trends = video.isTrending(20)
print(trends)
print()

"""Problem Set Version 1
Problem 1: Pokemon Class"""
class Pokemon:
  def __init__(self, name, types):
      self.name = name
      self.types = types
      self.is_caught = False

my_pokemon=Pokemon("Pikachu", "Electric")
print()

"""Problem 2: Create Squirtle"""
class Pokemon:
  def __init__(self, name, types):
      self.name = name
      self.types = types
      self.is_caught = False

  def print_pokemon(self):
      print({
          "name": self.name,   # Output: "name": "Squirtle",
          "types": self.types, # Output: "types": ["Water"],
          "is_caught": self.is_caught # Output: "is_caught": False
      })

squirtle = Pokemon("Squirtle", ["Water"])
Pokemon.print_pokemon(squirtle)
print()

"""Problem 3: Is Caught"""
class Pokemon():
  def __init__(self, name, types):
    self.name = name
    self.types = types
    self.is_caught = False

  def catch(self):
    self.is_caught = True
    
  def print_pokemon(self):
    print({
        "name": self.name,   # Output: "name": "Squirtle",
        "types": self.types, # Output: "types": ["Water"],
        "is_caught": self.is_caught # Output: "is_caught": False
    })

my_pokemon = Pokemon("rattata", ["Normal"])
my_pokemon.print_pokemon()

my_pokemon.catch()
my_pokemon.print_pokemon()
print()

"""Problem 5: Choose Pokemon
Update the Pokemon class with a new method choose() that takes in no parameters except self.
If the Pokemon is caught, the method should print the string "<Pokemon name> I choose you!".
Otherwise, it should print "<Pokemon name> is wild! Catch them if you can!"."""

class Pokemon():
  def __init__(self, name, types):
    self.name = name
    self.types = types
    self.is_caught = False

  def catch(self):
    self.is_caught = True

  def print_pokemon(self):
    print({
        "name": self.name,   # Output: "name": "Squirtle",
        "types": self.types, # Output: "types": ["Water"],
        "is_caught": self.is_caught # Output: "is_caught": False
    })
	
  def choose(self):
    if self.is_caught == True:
      print(f"{self.name.capitalize()} I choose you!")
    else:
      print(f"{self.name.capitalize()} is wild! Catch them if you can!")

my_pokemon = Pokemon("rattata", ["Normal"])
my_pokemon.print_pokemon()

my_pokemon.choose()
my_pokemon.catch()
my_pokemon.choose()
print()

"""Problem 6: Add Pokemon Type
Update the Pokemon class with a new method add_type() that takes in a string new_type as a parameter. It should add new_type to the Pokemon's list of types."""
class Pokemon():
  def __init__(self, name, types):
    self.name = name
    self.types = types
    self.is_caught = False

  def catch(self):
    self.is_caught = True

  def print_pokemon(self):
    print({
        "name": self.name,   # Output: "name": "Squirtle",
        "types": self.types, # Output: "types": ["Water"],
        "is_caught": self.is_caught # Output: "is_caught": False
    })

  def choose(self):
    if self.is_caught == True:
      print(f"{self.name.capitalize()} I choose you!")
    else:
      print(f"{self.name.capitalize()} is wild! Catch them if you can!")

  def add_type(self, new_type):
    self.types.append(new_type)
    
jigglypuff = Pokemon("Jigglypuff", ["Normal"])
jigglypuff.print_pokemon()

jigglypuff.add_type("Fairy")
jigglypuff.print_pokemon()
print()

"""Problem 7: Get Pokemon
Outside the Pokemon class, write a new function get_by_type() that takes in a list of Pokemon instances my_pokemon and a string pokemon_type as parameters.

The function should return a list of all Pokemon instances from my_pokemon that have the type pokemon_type.
Hint: To test, loop over Pokemon in return list and print the Pokemon's name"""
class Pokemon():
  def __init__(self, name, types):
    self.name = name
    self.types = types
    self.is_caught = False

  def catch(self):
    self.is_caught = True

  def print_pokemon(self):
    print({
        "name": self.name,   # Output: "name": "Squirtle",
        "types": self.types, # Output: "types": ["Water"],
        "is_caught": self.is_caught # Output: "is_caught": False
    })

  def choose(self):
    if self.is_caught == True:
      print(f"{self.name.capitalize()} I choose you!")
    else:
      print(f"{self.name.capitalize()} is wild! Catch them if you can!")

  def add_type(self, new_type):
    self.types.append(new_type)

def get_by_type(my_pokemon, pokemon_type):
  pokemons = []
  for pokemon in my_pokemon:
     if pokemon_type in pokemon.types:
       pokemons.append(pokemon.name.lower())
  return pokemons
    
# initializing pokemons
jigglypuff = Pokemon("Jigglypuff", ["Normal", "Fairy"])
diglett = Pokemon("Diglett", ["Ground"])
meowth = Pokemon("Meowth", ["Normal"])
pidgeot = Pokemon("Pidgeot", ["Normal", "Flying"])
blastoise = Pokemon("Blastoise", ["Water"])

my_pokemon = [jigglypuff, diglett, meowth, pidgeot, blastoise]
normal_pokemon = get_by_type(my_pokemon, "Normal")
print(normal_pokemon)
print()

"""Problem 8: Pokemon Evolution
Some Pokemon can evolve into other species of Pokemon. In the updated Pokemon class below, each instance of Pokemon has an attribute evolution. The attribute will either be the default value of None or another Pokemon instance.

Write a function get_evolutionary_line() that takes in a Pokemon object starter_pokemon as a parameter. The function should return a list of itself and the Pokemon that the starter_pokemon can evolve into."""
class Pokemon:
  def  __init__(self, name, types, evolution = None):
    self.name = name
    self.types = types
    self.is_caught = False
    self.evolution = evolution

  def catch(self):
    self.is_caught = True

  def print_pokemon(self):
    print({
        "name": self.name,   # Output: "name": "Squirtle",
        "types": self.types, # Output: "types": ["Water"],
        "is_caught": self.is_caught # Output: "is_caught": False
    })

  def choose(self):
    if self.is_caught == True:
      print(f"{self.name.capitalize()} I choose you!")
    else:
      print(f"{self.name.capitalize()} is wild! Catch them if you can!")

  def add_type(self, new_type):
    self.types.append(new_type)

def get_by_type(my_pokemon, pokemon_type):
  pokemons = []
  for pokemon in my_pokemon:
     if pokemon_type in pokemon.types:
       pokemons.append(pokemon.name.lower())
  return pokemons

def get_evolutionary_line(starter_pokemon):
  list = []
  curr = starter_pokemon
  while curr:
    list.append(curr.name)
    curr = curr.evolution
  return list

charizard = Pokemon("Charizard", ["fire", "flying"])
charmeleon = Pokemon("Charmeleon", ["fire"], charizard)
charmander = Pokemon("Charmander", ["fire"], charmeleon)

charmander_list = get_evolutionary_line(charmander)
print(charmander_list)

charmeleon_list = get_evolutionary_line(charmeleon)
print(charmeleon_list)

charizard_list = get_evolutionary_line(charizard)
print(charizard_list)
print()

"""Problem 9: Node Class
A linked list is a new data type that, similar to a normal list or array, allows us to store pieces of data sequentially. The difference between a linked list and a normal list lies in how each element is stored in a computer’s memory.

In a normal list, individual elements of the list are stored in adjacent memory locations according to the order they appear in the list. If we know where the first element of the list is stored, it’s really easy to find any other element in the list.

In a linked list, the individual elements called nodes are not stored in sequential memory locations. Each node may be stored in an unrelated memory location. To connect nodes together into a sequential list, each node stores a reference or pointer to the next node in the list.

Using the provided Node class below, create two nodes:

The first node should have value a and be stored in a variable node_one.
The second node should have value b and be stored in a variable node_two.
You do not need to connect the nodes together yet."""
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

node_one = Node('a')
node_two = Node('b')
print(node_one.value) 
print(node_one.next) 
print(node_two.value)
print(node_two.next) 
print()

"""Problem 10: Linking Nodes
To link the nodes, we can set a node's next attribute to hold another node. Update node_one from the Problem 9 to point to node_two.
"""
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

node_one = Node('a')
node_two = Node('b')
node_one.next = node_two
print(node_one.value)
print(node_one.next.value)
print(node_two.value)
print()

"""Problem 11: Mario Party
Create the list ["Mario", "Luigi", "Wario", "Toad"] as a linked list given the Node class:
"""
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next
    
list = ["Mario", "Luigi", "Wario", "Toad"]
node_4 = Node(list[3])
node_3 = Node(list[2], node_4)
node_2 = Node(list[1], node_3)
node_1 = Node(list[0], node_2)
print(node_1.value, "->", node_1.next.value)
print(node_2.value, "->", node_2.next.value)
print(node_3.value, "->", node_3.next.value)
print(node_4.value, "->", node_4.next)
print()

"""Problem 12: Printing Linked List
Write a function print_linked_list() that takes in a head node as a parameter and prints the linked list using the string " -> " to separate each node.
"""
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def print_linked_list(head):
  current = head
  while current is not None:
    print(current.value, end="")
    if current.next is not None:
      print(' -> ', end="")
    current = current.next

# Creating the linked list: a -> b -> c -> d -> e
e = Node("e")
d = Node("d", e)
c = Node("c", d)
b = Node("b", c)
a = Node("a", b)

# input linked list: a->b->c->d->e
print_linked_list(a)
print()
'''
U - Understand
Share 2 questions you would ask to help understand the question:
(1)
(2)

P - Plan
Write out in plain English what you want to do:
Translate each sub-problem into pseudocode:
(1)
(2)
(3)

I - Implement
Translate the pseudocode into Python and share your final answer:
'''

"""Problem Set Version 2
Problem 1: Card Class
Step 1: Copy the following code into Replit.
Step 2: Instantiate an instance of the class Card and store it in a variable named card. The Card object should have the suit "Spades" and the rank "8".
Step 3: Update the Card class with the new method print_card() provided below:
Step 4: Create an instance of the class and store it in a variable named card. The object should have suit "Clubs" and rank "Ace".
"""
class Card():
  def  __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank

def print_card(self):
  return f"{self.rank} of {self.suit}"
  
card = Card("Spades", "8")
card1 = Card("Clubs", "Ace")
print(print_card(card))
print(print_card(card1))
print()

"""Problem 3: Verify Update
Step 1: Using the same Card class from Problem 2, update your code so that the suit of card is "Hearts" instead of "Clubs".
Step 2: Use the print_card() method to verify that card was updated."""

card2 = Card("Hearts", "Ace")
print(print_card(card2))
print()

"""Problem 4: Valid Card
Update the Card class with a new method is_valid() that takes in no parameters except self. The method should return True if:

The suit is one of the following values: "Hearts", "Spades", "Clubs", "Diamonds"
The rank is one of the following values: "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"
Otherwise, the method should return False"""
class Card():
  def  __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank
  
  def is_valid(self):
    suit_lst = ["Hearts", "Spades", "Clubs", "Diamonds"]
    rank_lst = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    if self.suit in suit_lst and self.rank in rank_lst:
      return True
    else:
      return False

def print_card(self):
  return f"{self.rank} of {self.suit}"
  
my_card = Card("Hearts", "7")
print(my_card.is_valid())

second_draw = Card("Spades", "Joker")
print(second_draw.is_valid())
print()

"""Problem 5: Get Value
Update the Card class with a new method get_value() that takes in no parameters except self.
The function returns the card's value depending on the card's rank:
If the card has rank 2, 3, 4, 5, 6, 7, 8, 9, 10, the method should return the rank as an integer
If the card has rank Ace, the method should return 1 as the card's value
If the card has rank Jack, the method should return 11 as the card's value
If the card has rank Queen, the method should return 12 as the card's value
If the card has rank King, the method should return 13 as the card's value
If the card is invalid, the method should return None"""

class Card():
  def  __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank

  def get_value(self):
    rank_lst = ["2", "3", "4", "5", "6", "7", "8", "9", "10"]
    if self.rank in rank_lst:
      return self.rank
    elif self.rank == "Ace":
      return "1"
    elif self.rank == "Jack":
      return "11"
    elif self.rank == "Queen":
      return "12"
    elif self.rank == "King":
      return "13"
    else:
      return None
    
card = Card("Hearts", "7")
print(card.get_value())

card_two = Card("Spades", "Jack")
print(card_two.get_value())
print()

"""Problem 6: Hand Class
Step 1: Add the following Hand class to your code that represents a player's hand of cards.
A new instance of Hand is always empty.
Step 2: Add two methods add_card() and remove_card() to the Hand class that each accept a Card object as a parameter. add_card() should add the Card to the player's Hand. remove_card() should remove the card from the player's Hand."""

class Card():
  def  __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank 

  def __str__(self):
    return f"{self.rank} of {self.suit}"

  def __repr__(self):
    return self.__str__()
    
class Hand:
  def __init__(self):
    self.cards = []

  def add_card(self, card):
    self.cards.append(card)
    return self.cards

  def remove_card(self, card):
    if card in self.cards:
      self.cards.remove(card)
    else:
      print(f"Card {card} not in hand")
    return self.cards

card_one = Card("Hearts", "3")
card_two = Card("Spades", "8")

player1_hand = Hand()
# cards = []

cards_lst = player1_hand.add_card(card_one)
print(cards_lst)
# cards = [card_one]

cards_lst2 = player1_hand.add_card(card_two)
print(cards_lst2)
# cards = [card_one, card_two]

cards_lst3 = player1_hand.remove_card(card_one)
print(cards_lst3)
# cards = [card_two]
print()

"""Problem 7: Sum of Cards
Write a function sum_hand() that takes in an instance of Hand as a parameter and returns the summed value of all cards in the hand.

Use the methods from Problems 5-7 to assist you.
If any card in the hand is invalid, return None."""
class Card():
  def  __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank 

  def __str__(self):
    return f"{self.rank} of {self.suit}"

  def __repr__(self):
    return self.__str__()
    
  def get_value(self):
    rank_lst = ["2", "3", "4", "5", "6", "7", "8", "9", "10"]
    if self.rank in rank_lst:
      return self.rank
    elif self.rank == "Ace":
      return "1"
    elif self.rank == "Jack":
      return "11"
    elif self.rank == "Queen":
      return "12"
    elif self.rank == "King":
      return "13"
    else:
      return None

class Hand:
  def __init__(self):
    self.cards = []

  def add_card(self, card):
    self.cards.append(card.get_value())
    return self.cards

def sum_hand(hand):
  sums = 0
  for card in hand.cards:
    sums += int(card)
  return sums

card_one = Card("Hearts", "3")
card_two = Card("Hearts", "Jack")
card_three = Card("Spades", "3")

hand = Hand()
hand.add_card(card_one)
hand.add_card(card_two)
hand.add_card(card_three)

sum = sum_hand(hand)
print(sum) # prints 17
print()

"""Problem 8: Print Hand
The class Card has been updated below with a new attribute next to represent the card that comes after it in a hand of cards.

Write a function print_hand() that accepts a Card object and returns a list of all cards in the hand that come after it."""

class Card():
  def  __init__(self, suit, rank, next = None):
    self.suit = suit
    self.rank = rank
    self.next = next

  def get_value(self):
    return f"{self.rank} of {self.suit}"

def print_hand(starting_card):
  card_lst = []
  current = starting_card
  while current is not None:
    card_lst.append(current.get_value())
    if current.next is not None:
      current = current.next
    else:
      break
  return card_lst

card_one = Card("Hearts", "3")
card_two = Card("Hearts", "4")
card_three = Card("Diamonds", "King")

card_one.next = card_two
card_two.next = card_three
print(print_hand(card_one)) # [card_one, card_two, card_three]
print()

"""Problem 9: Head and Tail Nodes
A linked list is a new data type that, similar to a normal list or array, allows us to store pieces of data sequentially. The difference between a linked list and a normal list lies in how each element is stored in a computer’s memory.

In a normal list, individual elements of the list are stored in adjacent memory locations according to the order they appear in the list. If we know where the first element of the list is stored, it’s really easy to find any other element in the list.

In a linked list, the individual elements called nodes are not stored in sequential memory locations. Each node may be stored in an unrelated memory location. To connect nodes together into a sequential list, each node stores a reference or pointer to the next node in the list.

Using the provided Node class below, create two nodes.

The first node should have value 100 and be stored in a variable head.
The second node should have value 200 and be stored in a variable tail.
Set head to point to tail.
"""
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

tail = Node(200)
head = Node(100, tail.value)
print(head.value) # 100
print(head.next)  # 200
print(tail.value) # 200
print(tail.next)  # None
print()

"""Problem 10: Middle Node
Within a linked list, we can redirect pointers to insert nodes at any place in the list.

Create a new Node middle with value 150 and insert it between head and tail from Problem 9."""
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

middle = Node(150)
tail = Node(200)
head = Node(100)

# linking nodes
middle.next = tail
head.next = middle

print(head.next.value)   # 150
print(middle.next.value) # 200
print(tail.next)   # None
print()

"""Problem 11: Zodiac Signs
Create the list ["aries", "taurus", "gemini", "cancer"] as a linked list using the Node class:"""

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

node_4 = Node("cancer")
node_3 = Node("gemini", node_4)
node_2 = Node("taurus", node_3)
node_1 = Node("aries", node_2)

print(node_1.value, "->", node_1.next.value) # aries -> taurus
print(node_2.value, "->", node_2.next.value) # taurus -> gemini
print(node_3.value, "->", node_3.next.value) # gemini -> cancer
print(node_4.value, "->", node_4.next)       # cancer -> None
print()

"""Problem 12: Print Linked List
Write a function print_linked_list() that takes in a head of a linked list as a parameter. The function prints and returns a list of all the values in the linked list in the order they appear in the linked list.

Note: The "head" of a linked list is the first element in the linked list, equivalent to lst[0] of a normal list.
"""
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next= next

def print_linked_list(head):
  if head is None:
    print("Empty list")
    return []

  linked_values = []
  current = head
  while current:
    print(current.value, end=" -> " if current.next else "\n")
    linked_values.append(current.value)
    current = current.next
  print(linked_values)
  print()

# input linked list: a->b->c->d->e
e = Node("e")
d = Node("d", e)
c = Node("c", d)
b = Node("b", c)
a = Node("a", b)
print_linked_list(a)
#print()

"""Problem Set Version 3
Problem 1: Player Class
Step 1: Copy the following code into Replit.
Step 2: Instantiate an instance of the class Player and store it in a variable named player_one.
The Player object should have the character "Yoshi" and the kart "Super Blooper"."""

class Player():
  def  __init__(self, character, kart):
    self.character = character
    self.kart = kart
    self.items = []

player_one = Player("Yoshi", "Super Blooper")

"""Problem 2: Get Player
Step 1: Using the Player class from Problem 1, add the following get_player() method to your Replit code:
def get_player(self):
    return f"{self.character} driving the {self.kart}"
Step 2: Create a second instance of Player in a variable named player_two.
The Player object created should have character "Bowser" and kart "Pirahna Prowler".
Step 3: Use the method get_player() below to print out "Match: Yoshi driving the Super Blooper vs Bowser driving the Pirahna Prowler"."""
class Player():
  def  __init__(self, character, kart):
    self.character = character
    self.kart = kart
    self.items = []

  def get_player(self):
    return f"{self.character} driving the {self.kart}"

player_one = Player("Yoshi", "Super Blooper")
player_two = Player("Bowser", "Pirahna Prowler")
print(f"Match: {player_one.get_player()} vs {player_two.get_player()}")
print()

"""Problem 3: Update Kart
Players might want to update their choice of kart for their next race.

Update player_one so that their kart is "Dolphin Dasher" instead of it's current value, "Super Blooper"."""

class Player():
  def  __init__(self, character, kart):
    self.character = character
    self.kart = kart
    self.items = []

  def get_player(self):
    return f"{self.character} driving the {self.kart}"

  def update_kart(self, new_kart):
    self.kart = new_kart

player_one = Player("Yoshi", "Super Blooper")
print(player_one.get_player())

player_one.update_kart("Dolphin Dasher")
print(player_one.get_player())
print()

"""Problem 4: Set Character
In the previous exercise, we accessed and modified a player’s kart attribute directly. Instead of allowing users to update their player directly, it is common to create setter methods that users can call to update class attributes. This has a few different benefits, including allowing us to validate data before updating our class instance.

Update your Player class with a method set_character() that takes in one parameter name.

If name is valid, it should update the player’s character attribute to have value name and print "Character updated".
Otherwise, it should print out "Invalid character".
Valid character names are "Mario", "Luigi", "Peach", "Yoshi", "Toad", "Wario", "Donkey Kong", and "Bowser"."""
class Player():
  def  __init__(self, character, kart):
    self.character = character
    self.kart = kart
    self.items = []

  def get_player(self):
    return f"{self.character} driving the {self.kart}"

  def update_kart(self, new_kart):
    self.kart = new_kart

  def set_player(self, name):
    valid = ["Mario", "Luigi", "Peach", "Yoshi", "Toad", "Wario", "Donkey Kong", "Bowser"]
    if name in valid:
      print("Character updated")
    else:
      print("Invalid character")
      print()
      
player_one = Player("Yoshi", "Super Blooper")
player_two = Player("Bowser", "Pirahna Prowler")
player_one.set_player("Peach")
player_two.set_player("Kermit")

"""Problem 5: Add Special Item
Players can pick up special items as they race.

Update the Player class with a new method add_item() that takes in one parameter, item_name.

The method should validate the item_name.

If the item is valid, add item_name to the player’s items attribute.
The method does not need to return any values.
item_name is valid if it has one of the following values: "banana", "green shell", "red shell", "bob-omb", "super star", "lightning", "bullet bill"."""

class Player():
  def  __init__(self, character, kart):
    self.character = character
    self.kart = kart
    self.items = []

  def add_item(self, item_name):
    valid_items = ["banana", "green shell", "red shell", "bob-omb", "super star", "lightning", "bullet bill"]
    if item_name in valid_items:
      self.items.append(item_name)
    print(self.items)

player_one = Player("Yoshi", "Dolphin Dasher")
# items = []

player_one.add_item("red shell")
# items = ["red shell"]

player_one.add_item("super star")
# items = ["red shell", "super star"]

player_one.add_item("super smash")
# items = ["red shell", "super star"]
print()

"""Problem 6: Print Inventory
Update the Player class with a method print_inventory() that accepts no parameters except for self.
The method should print the name and quantity of each item in a player’s items list. If the player has no items, the function should print "Inventory empty".""
"""
class Player():
  def  __init__(self, character, kart):
    self.character = character
    self.kart = kart
    self.items = []

  def print_inventory(self):
    if not self.items:
      return "Inventory empty"
      
    item_dict = {}
    for i in self.items:
      item_dict[i] = item_dict.get(i, 0) + 1
    inventory_str = ", ".join([f"{key}: {value}" for key, value in item_dict.items()])
    return f"Inventory: {inventory_str}"

player_one = Player("Yoshi", "Super Blooper")
player_one.items = ["banana", "bob-omb", "banana", "super star"]
player_two = Player("Peach", "Dolphin Dasher")

print(player_one.print_inventory()) # Inventory: banana: 2, bob-omb: 1, super star: 1
print(player_two.print_inventory()) # Inventory empty
print()

"""Problem 7: Race Results
Given a list race_results of Player objects where the first player in the list came first in the race, second player in the list came second, etc., write a function print_results() that prints the players in place."""

class Player:
  def __init__(self, character, kart):
    self.character = character
    self.kart = kart
    self.items = []
    
  def get_player(self):
    return f"{self.character}"

def print_results(race_results):
  for i, names in enumerate(race_results):
    print(f"{i + 1}"+".", names.get_player())

peach = Player("Peach", "Daytripper")
mario = Player("Mario", "Standard Kart M")
luigi = Player("Luigi", "Super Blooper")
race_one = [peach, mario, luigi]
print_results(race_one)
print()

"""Problem 8: Get Rank
The Player class has been updated below with a new attribute ahead to represent the player currently directly ahead of them in the race.

Write a function get_rank() that accepts a Player object my_player and returns their current place number in the race."""
class Player:
    def __init__(self, character, kart, opponent=None):
        self.character = character
        self.kart = kart
        self.items = []
        self.ahead = opponent

def get_place(my_player):
  if my_player == "Peach":
    current = peach
  elif my_player == "Luigi":
    current = luigi
  elif my_player == "Mario":
    current = mario
  else:
    return "player not found"
    
  rank = 1
  while current.ahead is not None:
    rank += 1
    current = current.ahead
  return rank
  
peach = Player("Peach", "Daytripper")
mario = Player("Mario", "Standard Kart M", peach)
luigi = Player("Luigi", "Super Blooper", mario)

player1_rank = get_place("Luigi")
print(player1_rank) # 3

player2_rank = get_place("Peach")
print(player2_rank) # 1

player3_rank = get_place("Mario")
print(player3_rank) # 2
print()

"""Problem 9: Tom and Jerry
Using the provided Node class below, create a linked list cat -> mouse where the instance cat has value "Tom" which points to the instance mouse that has value "Jerry"."""

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

mouse = Node("Jerry")
cat = Node("Tom", mouse)
print(cat.value) # Tom
print(cat.next) # mouse
print(cat.next.value) # Jerry
print(mouse.value) # Jerry
print(mouse.next) # None
print()

"""Problem 10: Chase List
In a linked list, pointers can be redirected at any place in the list.

Using the linked list from Problem 9, create a new Node dog with value "Spike" and point it to the cat node so that the full list now looks like dog -> cat -> mouse."""
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

mouse = Node("Jerry")
cat = Node("Tom", mouse)
dog = Node("Spike", cat)
print(dog.value) # Spike
print(dog.next) # cat
print(dog.next.value) # Tom
print(cat.next) # mouse
print(cat.next.value) # Jerry
print(mouse.next) # None
print()

"""Problem 11: Update Chase
Using the linked list from Problem 10, remove the dog node and add in a node cheese with value "Gouda" to the end of the list so that the resulting list is cat -> mouse -> cheese."""

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def print_linkedlst(head):
  current = head
  while current:
    if current == cat:
      current.value = "cat"
    elif current == mouse:
      current.value = "mouse"
    elif current == cheese:
      current.value = "cheese"
    else:
      return "node not found"
    print(current.value, end=" -> " if current.next else "")
    current = current.next

cheese = Node("Gouda")
mouse = Node("Jerry", cheese)
cat = Node("Tom", mouse)
print_linkedlst(cat)
print()

"""Problem 12: Chase String
Write a function chase_list() that takes in a head of a linked list and returns a string linking together the values of the list with the separator "chases".

Note: The "head" of a linked list is the first element in the linked list. Equivalent to lst[0] of a normal list."""
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def chase_list(head):
  result = []
  current = head
  while current:
    result.append(current.value)
    current = current.next
  return " chases ".join(result)

dog = Node("Spike")
cat = Node("Tom")
mouse = Node("Jerry")
cheese = Node("Gouda")

dog.next = cat
cat.next = mouse
mouse.next = cheese
cheese.next = None
print()
print(chase_list(dog)) #"Spike chases Tom chases Jerry chases Gouda"
print()

"""
********** Session 2 ************
Problem Set Version 1
Problem 1: Battle Pokemon
Given the Pokemon class below, copy the code and add it to your Replit.
Then, write a method attack() that takes in a Pokemon object opponent and decreases opponent's hp by their self's damage amount.

If damaging the opponent leads to the opponent having an hp of 0 or less, the function should set the opponent's hp to 0 and print out "<Opponent name> fainted>.

Otherwise, the function should print out "<Pokemon name> dealt <damage> damage to <opponent name>".
"""
class Pokemon():
  def  __init__(self, name, hp, damage):
    self.name = name
    self.hp = hp # hit points
    self.damage = damage # The amount of damage this pokemon does to its opponent every attack

  def attack(self, opponent):
    x = opponent.hp - self.damage
    if x <= 0:
      print (f'{opponent.name} fainted!')
    else:
      print (f'{self.name} dealt {self.damage} damage to {opponent.name}')

pikachu = Pokemon("Pikachu", 35, 20)
bulbasaur = Pokemon("Bulbasaur", 45, 30) 
opponent = bulbasaur
pikachu.attack(opponent)
print()

"""
Problem 2: Convert to Linked List
Using the provided Node class below, create the normal Python list ["Jigglypuff", "Wigglytuff"] as a linked list.
print(node_1.value, "->", node_1.next.value)
print(node_2.value, "->", node_2.next)
"""
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

node_1 = Node("JigglyPuff")
node_2 = Node("WigglyPuff")
node_1.next = node_2
print(node_1.value, "->", node_1.next.value)
print(node_2.value, "->", node_2.next)
print()

"""Problem 3: Add First
Write a function add_first() that takes in a head of a linked list and a new_node from the Node class as parameters.

It should insert new_node as the new head of the linked_list. The function returns new_node.

Note: The "head" of a linked list is the first element in the linked list. Equivalent to lst[0] of a normal list."""

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def add_first(head, new_node):
  new_node.next = head
  return new_node    

# Using the Linked List from Problem 2
node_1 = Node("JigglyPuff")
node_2 = Node("WigglyPuff")
node_1.next = node_2
print(node_1.value, "->", node_1.next.value) # Jigglypuff -> Wigglytuff 

new_node = Node("Ditto")
node_1 = add_first(node_1, new_node)
print(node_1.value, "->", node_1.next.value) # Ditto -> Jigglypuff
print()

"""Problem 4: Get Tail
Write a function get_tail() that takes in the head of a linked list as a parameter. It should print out the value of the tail of the list.

If the list is empty (head is None), return None.
Note: The "tail" of a list is the last element in the linked list. Equivalent to lst[-1] in a normal list."""

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def get_tail(head):
  if head is None:
    return None

  current = head
  while current.next is not None:
    current = current.next
  return current.value

# linked list: num1->num2->num3
# create linked list
num1 = Node(1)
num2 = Node(2)
num3 = Node(3)

# define next nodes
num1.next = num2
num2.next = num3

# test function
head = num1
tail = get_tail(num1)
print(tail)
print()

"""Problem 5: Replace Node
Using the Node class, write a function ll_replace() that takes a head of a linked list and two values, original and replacement as parameters.

The function updates any node with value original to have value replacement."""

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def print_linked_list(head):
  current = head
  while current is not None:
      print(current.value, end=" -> " if current.next else "")
      current = current.next
  print()

def ll_replace(head, original, replacement):
  # If the list is empty, return
  if head is None:
    return 

  # Start at the head of the list
  current = head

  # Traverse the list
  while current is not None:
    # If the current node's value matches the original value
    if current.value == original:
      # Replace the value with the replacement value
      current.value = replacement
    # Move to the next node
    current = current.next
    
num3 = Node(5)
num2 = Node(6, num3)
num1 = Node(5, num2)
# initial linked list: 5 -> 6 -> 5
print_linked_list(num1)

head = num1
ll_replace(head, 5, "banana")
# updated linked list: "banana" -> 6 -> "banana"
print_linked_list(num1)
print()

"""Problem 6: List Nodes
Write a function listify_first_n() that takes in a head of a linked list and a non-negative integer n as parameters.

The function returns a list of values of the first n nodes.
If n is greater than the length of the linked list, return a list of the values of all nodes in the linked list."""
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def listify_first_n(head, n):
  # if the list is empty, return 
  if head is None:
    return ""

  result = []
  count = 0
  current = head
  while current is not None and count != n:
    result.append(current.value)
    count += 1
    current = current.next
  return result
    
# linked list: a -> b -> c
c = Node("c")
b = Node("b", c)
a = Node("a", b)
head = a
lst = listify_first_n(head, 2)
print(lst) # [`a`, `b`]

# linked list: j -> k -> l 
l = Node("l")
k = Node("k", l)
j = Node("j", k)
head2 = j
lst2 = listify_first_n(head2, 5)
print(lst2) # [`j`, `k`, `l`]
print()

"""Problem 7: Insert Value
Write a function ll_insert() that takes in a head of a linked list, a value val, and an index i as parameters.
The function should insert a new Node with value val at index i of the linked list, then return the head of the linked list.

If i is greater than the length of the list, insert the new node at the end of the list.
Hint: Linked lists do not have built-in indices so you will need to track the indices yourself."""

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def print_linked_list2(head):
  current = head
  while current is not None:
    print(current.value, end = " -> " if current.next else "")
    current = current.next
  print()

def ll_insert(head, val, i):
  # If the list is empty, return
  if head is None:
    return 

  result_lst = []
  count = 0
  # start at the head of the list
  current = head
  # traverse the list
  while current is not None: 
    count += 1
    result_lst.append(str(current.value))
    current = current.next
    if count == i:
      result_lst.append(str(val))
  return " -> ".join(result_lst)

# linked list: 3 -> 8 -> 12 -> 9
num4 = Node(9)
num3 = Node(12, num4)
num2 = Node(8, num3)
num1 = Node(3, num2)
head = num1
print_linked_list2(head)
# result linked list: 3 -> 8 -> 20 -> 12 -> 9
print(ll_insert(head, 20, 2))
print()

"""Problem 8: Linked Listify
Write a function list_to_linked_list() that takes in a list lst as a parameter and converts it to a linked list. The function should return the head of the linked list."""

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def list_to_linked_list(lst):
  if not lst:
    return None

  head = Node(lst[0])
  current = head

  for item in lst[1:]:
    new_node = Node(item)
    current.next = new_node
    current = new_node
  return head.value
    
normal_list = ["Betty", "Veronica", "Archie", "Jughead"]
linked_list = list_to_linked_list(normal_list)
print(linked_list) # Only prints the head element! # Betty 
# Linked list : Betty -> Veronica -> Archie -> Jughead
print()

"""Problem 9: Doubly Linked List
One of the drawbacks of a linked list is that it's difficult to go backwards, because each Node only knows about the Node in front of it. (E.g., A -> B -> C)

A doubly linked list solves this problem! Instead of just having a next attribute, a doubly linked list also has a prev attribute that points to the Node before it. (E.g., A <-> B <-> C)

Given the Node class for a doubly linked list below, recreate the list ["Poliwag", "Poliwhirl", "Poliwrath"] as a doubly linked list."""

class Node:
  def __init__(self, value, next = None, prev = None):
    self.value = value
    self.next = next
    self.prev = prev

poliwag = Node("Poliwag")
poliwrath = Node("Poliwrath")
poliwhirl = Node("Poliwhirl", poliwrath, poliwag)
poliwag.next = poliwhirl
poliwrath.prev = poliwhirl
print(poliwhirl.prev.value, "<->", poliwhirl.value, "<->", poliwhirl.next.value) # 'Poliwag' <-> 'Poliwhirl' <-> 'Poliwrath'`
print()

"""Problem 10: Print Backwards
Write a function print_reverse() that takes in the tail of a doubly linked list as a parameter.
It should print out the values of the linked list in reverse order, each separated by a space."""

class Node:
  def __init__(self, value, next = None, prev = None):
    self.value = value
    self.next = next
    self.prev = prev

def print_reverse(tail):
  current = tail
  while current:
    print(current.value, end = " " if current.prev is not None else "")
    current = current.prev
  print()
  
poliwag = Node("Poliwag")
poliwrath = Node("Poliwrath")
poliwhirl = Node("Poliwhirl", poliwrath, poliwag)
poliwag.next = poliwhirl
poliwrath.prev = poliwhirl
#              (head)                       (tail)
# Linked List: Poliwag <-> Poliwhirl <-> Poliwrath
print_reverse(poliwrath) # Output: Poliwrath Poliwhirl Poliwag
print()

"""Problem Set Version 2
Problem 1: Poker Two-Pair Hand
In poker, players are given a hand of five cards. A player has a "two-pair" hand if they have two cards of the same rank and another two cards of another rank. The fifth card isn’t used here.

Given the Card class below, write a function is_two_pair() that takes in a list player_hand that contains 5 Card objects.

The function returns True if the player has a two pair hand and False otherwise.
Cards in the hand are guaranteed to be unique and are guaranteed to have on the following suits and ranks:

The suit is one of the following values: "Hearts", "Spades", "Clubs", "Diamonds"
The rank is one of the following values: '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace'"""
class Card():
  def  __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank

def is_two_pair(player_hand):
  player_dict = {}
  for card in player_hand:
    player_dict[card.rank] = player_dict.get(card.rank, 0) + 1
  pairs_dict = {k:v for k, v in player_dict.items() if v == 2}
  return len(pairs_dict) == 2

card_one = Card("Hearts", "Ace")
card_two = Card("Hearts", "4")
card_three = Card("Diamonds", "Ace")
card_four = Card("Diamonds", "4")
card_five = Card("Diamonds", "6")
card_six = Card("Diamonds", "7")

player_one_hand = [card_one, card_two, card_three, card_four, card_five]
print(is_two_pair(player_one_hand)) # True  # Two Aces + Two 4s (+ Unused 6)

player_two_hand = [card_two, card_three, card_four, card_five, card_six]
print(is_two_pair(player_two_hand)) # False # Two 4s (+ Ace + 6 + 7)
print()

"""Problem 2: Barbie Linked List
Using the provided Node class below, recreate the list ['Barbie', 'President Barbie', 'Weird Barbie', 'Ken'] as a linked list."""

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

node_4 = Node("Ken")
node_3 = Node("Weird Barbie", node_4)
node_2 = Node("President Barbie", node_3)
node_1 = Node("Barbie", node_2)

print(node_1.value, "->", node_1.next.value)
print(node_2.value, "->", node_2.next.value)
print(node_3.value, "->", node_3.next.value)
print(node_4.value, "->", node_4.next)
print()

"""Problem 3: Insert Value First
Using the Node class, write a function add_first() that takes in the head of a linked list and a value object val as parameters.

The function shoud insert a new Node object with value val as the new head of the linked list and return the new node.

Note: The "head" of a linked list is the first element in the linked list. Equivalent to lst[0] of a normal list."""

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def print_linkedlist(head):
  if head is None:
    return None
    
  current = head
  while current:
    print(current.value, end = " -> " if current.next is not None else "")
    current = current.next
  print()

def add_first(head, val):
  new_node = Node(val)
  new_node.next = head
  return new_node

node_c = Node("C")
node_b = Node("B", node_c)
node_a = Node("A", node_b)

# Linked List: A -> B -> C
new_list = add_first(node_a, 0) # New List: 0 -> A -> B -> C
print_linkedlist(new_list)
print()

"""Problem 4: Linked List Length
Write a function ll_length() that takes in a head of a linked list as a parameter and returns the length of the linked list."""
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def ll_length(head):
  if head is None:
    return 0

  current = head
  count = 0
  while current:
    current = current.next
    count += 1
  return count

# Linked List: num1 -> num2 -> num3
num3 = Node("num3")
num2 = Node("num2", num3)
num1 = Node("num1", num2)
head = num1
print(ll_length(head)) # 3

# Empty Linked List
head = None
print(ll_length(head)) # 0
print()
  
"""Problem 5: Delete Tail
Write a function delete_tail() that takes in a head of a linked list as a parameter and removes the tail from the end of the list.

The function does not need to return any value, as it modifies the linked list in place.

Note: The "tail" of a list is the last element in the linked list. Equivalent to lst[-1] in a normal list."""

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def delete_tail(head):
  if head is None:
    return 

  if head.next is None:
    return None
    
  current = head
  while current.next:
    print(current.value, end = " -> " if current.next.next else "")
    current = current.next
  print()
    
# linked list: num1 -> num2 -> num3
num3 = Node("num3")
num2 = Node("num2", num3)
num1 = Node("num1", num2)
delete_tail(num1) # linked list: num1 -> num2
print()

"""Problem 6: Greatest Node
Write a function find_max() that takes in a head of a linked list as a parameter where each node is an integer value.

The function should return the maximum value in the linked list."""

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def find_max(head):
  max_val = -9999
  current = head
  while current:
    if int(current.value) > max_val:
      max_val = int(current.value)
    current = current.next
  return max_val
  
num4 = Node(10)
num3 = Node(30, num4)
num2 = Node(15, num3)
num1 = Node(20, num2)

# linked list: num1 -> num2 -> num3 -> num4
max_val = find_max(num1)
print(max_val)
print()

"""Problem 7: Pop Node
Write a function ll_pop() that takes in the head of a linked_list and an index i as parameters.

The function should remove the node at index i of the linked list and return the head of the list.

If i is greater than the length of the list, do nothing.
Hint: Linked lists do not have built-in indices so you will need to track the indices yourself."""

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def ll_pop(head, i):
  if head is None:
    return 

  current = head
  count = 0
  while current:
    print(current.value, end = " -> " if current.next else "")
    current = current.next
    count += 1
    if current is not None and count == i:
      current = current.next
  print()    
    
  
num3 = Node("num3")
num2 = Node("num2", num3)
num1 = Node("num1", num2)
# linked list: num1 -> num2 -> num3
ll_pop(num1, 1) # result: num1 -> num3
print()

"""Problem 8: Find Middle Node
Write a function find_middle_node() that takes in the head of a linked list and returns the "middle" node.

If the linked list has an even length and there are two "middle" nodes, return the first middle node.
(E.g., "1 -> 2 -> 3 -> 4" would return 2, not 3.)"""
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def find_middle_node(head):
  if not head:
    return None

  slow = head
  fast = head
  while fast.next and fast.next.next:
    slow = slow.next
    fast = fast.next.next
  return slow
    
# linked list: num1 -> num2 -> num3 -> num4
num4 = Node("num4")
num3 = Node("num3", num4)
num2 = Node("num2", num3)
num1 = Node("num1", num2)
head = num1
mid = find_middle_node(head) # mid == num2
print(mid.value)
print()

"""Problem 9: Create Double Links
One of the drawbacks of a linked list is that it's difficult to go backwards, because each Node only knows about the Node in front of it. (E.g., A -> B -> C)

A doubly linked list solves this problem! Instead of just having a next attribute, a doubly linked list also has a prev attribute that points to the Node before it. (E.g., A <-> B <-> C)

Update the Node constructor below so that the code creates a doubly linked list with head <-> tail."""

class Node:
  def __init__(self, value, next = None, prev = None):
    self.value = value
    self.next = next
    self.prev = prev
    
head = Node("First")
tail = Node("Last")

head.next = tail
tail.prev = head
print(head.value, "<->", head.next.value) # First <-> Last
print(tail.prev.value, "<->", tail.value) # First <-> Last
print()

"""Problem 10: Double to Single
Below are the node classes for a singly linked list and a doubly linked list. Write a function dll_to_sll() that takes in the head of a doubly linked list as a parameter and recreates it as a singly linked list.

The function returns the head of the new singly linked list."""

class SLLNode:
  def __init__(self, value, next = None):
    self.value = value
    self.next = next

class DLLNode:
  def __init__(self, value, next = None, prev = None):
    self.value = value
    self.next = next
    self.prev = prev

def dll_to_sll(dll_head):
  if not dll_head:
    return None

  sll_head = SLLNode(dll_head.value)
  current_sll = sll_head
  current_dll = dll_head.next

  while current_dll:
    new_node = SLLNode(current_dll.value)
    current_sll.next = new_node
    current_sll = new_node
    current_dll = current_dll.next
  return sll_head
  
def print_dll(head):
  current = head
  dll_str = ""
  while current:
      dll_str += str(current.value)
      if current.next:
          dll_str += " <-> "
      current = current.next
  print("DLL:", dll_str)

def print_sll(head):
  current = head
  sll_str = ""
  while current:
      sll_str += str(current.value)
      if current.next:
          sll_str += " -> "
      current = current.next
  print("SLL:", sll_str)

# Create the doubly linked list: Ice <-> Water <-> Steam
Ice = DLLNode("Ice")
Water = DLLNode("Water")
Steam = DLLNode("Steam")

Ice.next = Water
Water.prev = Ice
Water.next = Steam
Steam.prev = Water

# DLL: Ice <-> Water <-> Steam
dll_head = Ice

# Print the original doubly linked list
print_dll(dll_head)

# Convert DLL to SLL
sll_head = dll_to_sll(dll_head)

# Print the resulting singly linked list
print_sll(sll_head)
#SLL: Ice -> Water -> Steam
print()

"""Problem Set Version 3
Problem 1: Calculate Tournament Placement
In the Player class below, each player has a race_outcomes attribute which holds a list of integers describing what place they came in for each race in a tournament.

Write a method get_tournament_place() that takes in one parameter opponents, a list of other player objects also participating in the tournament, and returns the place in the overall tournament.

Rank in the tournament is determined by the lowest average race outcome. (1st place is better than 2nd!)
Each opponent in opponents is guaranteed to have participated in the same number of races as the current player."""
class Player:
  def __init__(self, character, kart, outcomes):
    self.character = character
    self.kart = kart
    self.items = []
    self.race_outcomes = outcomes

  def get_tournament_place(self, opponents):
    from statistics import mean
    my_average = mean(self.race_outcomes)
    opponent_averages = [mean(self.race_outcomes) for opponent in opponents]
    ranks = sorted([my_average] + opponent_averages)
    return ranks.index(my_average) + 1
    
# Example usage
player1 = Player("Mario", "Standard", [1, 2, 1, 1, 3])
player2 = Player("Luigi", "Standard", [2, 1, 3, 2, 2])
player3 = Player("Peach", "Standard", [3, 3, 2, 3, 1])

opponents = [player2, player3]
print(f"{player1.character} was number {player1.get_tournament_place(opponents)}") #Mario was number 1 # Mario's average place is 1.6, Luigi's is 2.0, and Peach's is 2.4
print()

"""Problem 2: Update Linked List Sequence
Using the provided Node class and linked list below, update the current linked list red -> yellow -> blue to be red -> orange -> yellow -> green -> blue."""

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def print_link_sequence(head):
  if head is None:
    return None

  current = head
  while current:
    print(current.value, end = " -> " if current.next else "")
    current = current.next
  print()

red = Node('red')
orange = Node("orange")
yellow = Node('yellow')
green = Node("green")
blue = Node('blue')
red.next = orange
orange.next = yellow
yellow.next = green
green.next = blue
# Current list: red -> yellow -> blue
# Desired list: red -> orange -> yellow -> green -> blue
print_link_sequence(red)
print()

"""Problem 3: Insert Node as Second Element
Write a function add_second() that takes in the head of a linked list and a value object val as parameters. It should insert val as the second node in the linked list and return the head of the linked list. (You can assume head is not None.)

Note: The "head" of a linked list is the first element in the linked list. Equivalent to lst[0] of a normal list."""

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next
def print_link_sequence(head):
  if head is None:
    return None

  current = head
  while current:
    print(current.value, end = " -> " if current.next else "")
    current = current.next
  print()
  
def add_second(head, val):
  new_node = Node(val)
  new_node.next = head.next
  head.next = new_node
  return head
      
num4 = Node(4)
num3 = Node(3, num4)
num1 = Node(1, num3)
insert_node = add_second(num1, 2)
print_link_sequence(insert_node)
# linked list: 1 -> 3 -> 4
# add_second(head, 2)
# result: 1 -> 2 -> 3 -> 4
print()

"""Problem 4: Increment Linked List Node Values
Write a function increment_ll() that takes in the head of a linked list of integer values and returns the same list, but with each node's value incremented by 1. Return the head of the list."""
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def print_link_sequence(head):
  if head is None:
    return None

  current = head
  while current:
    print(current.value, end = " -> " if current.next else "")
    current = current.next
  print()
  
def increment_ll(head):
  current = head
  while current:
    current.value += 1
    current = current.next
  return head
    
val3 = Node(7)
val2 = Node(6, val3)
val1 = Node(5, val2)
print("Original linked list:")
print_link_sequence(val1)
# my_list: 5 -> 6 -> 7

# Increment the values in the linked list and print the updated list
my_list = increment_ll(val1)
print("Linked list after incrementing values:")
print_link_sequence(my_list)

# Increment the values again and print the updated list
my_list = increment_ll(val1)
print("Linked list after incrementing values again:")
print_link_sequence(my_list)
print()

"""Problem 5: Copy Linked List
Write a function copy_ll() that takes in the head of a linked_list, and creates a complete copy of that linked list.

The function should return the head of a new linked list which is identical to the given list in terms of its structure and contents, but does not use any of the node objects from the original list."""

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def copy_ll(head):
  if head is None:
    return None

  new_head = Node(head.value)
  copy_current = new_head
  current = head.next

  while current:
    new_node = Node(current.value)
    copy_current.next = new_node

    current = current.next
    copy_current = copy_current.next
  return new_head
  
val3 = Node(7)
val2 = Node(6, val3)
val1 = Node(5, val2)
head = val1
# Linked List: 5 -> 6 -> 7
copy = copy_ll(head) # Linked List Copy: 5 -> 6 -> 7
print(head.value, copy.value)

# Change original list -- should not affect the copy
head.value = 10
print(head.value, copy.value)
print()

"""Problem 6: Find Minimum in Linked List
Write a function find_min() that takes in the head of a linked_list, and returns the minimum value in the linked list. You can assume the linked list will contain only numeric values."""

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def find_min(head):
  if head is None:
    return None

  current = head
  min_val = 99999
  while current:
    if current.value < min_val:
      min_val = current.value
    current = current.next
  return min_val

val4 = Node(8)
val3 = Node(7, val4)
val2 = Node(6, val3)
val1 = Node(5, val2)
head = val1
print(find_min(head))
# Linked List: 5 -> 6 -> 7 -> 8
# Input: head = 5
# Expected Output: 5

val4 = Node(7)
val3 = Node(2, val4)
val2 = Node(5, val3)
val1 = Node(8, val2)
head = val1
print(find_min(head))
# Linked List: 8 -> 5 -> 2 -> 7
# Input: head = 8
# Expected Output: 2
print()

"""Problem 7: Remove Node by Value from Linked List
Write a function ll_remove() that takes in the head of a linked list and a value val as parameters.

The function should remove the first node it finds in the linked list with value val and return the head of the linked list. If no node can be found with the value val, return the list unchanged."""

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def ll_remove(head, val):
  if head is None:
    return None

  if head.value == val:
    return head.next
  
  current = head
  while current.next:
    if current.next.value == val:
      current.next = current.next.next
      return head
    current = current.next
  return head

val4 = Node(8)
val3 = Node(7, val4)
val2 = Node(6, val3)
val1 = Node(5, val2)
head = val1

print("Original linked list:")
print_link_sequence(head)

my_list = ll_remove(head, 6)
print("Linked list after removing nodes:")
print_link_sequence(my_list)
# Linked List: 5 -> 6 -> 7 -> 8
# Input: head = 5, val = 6
# Expected Output: 5 -> 7 -> 8
print()

"""Problem 8: Move Tail to Front of Linked List
Write a function tail_to_head() that takes in the head of a linked list as a parameter, and moves the tail of the linked list to the front."""

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def tail_to_head(head):
  if head is None:
    return None

  current = head
  while current.next.next:
    current = current.next

  last_node = current.next
  current.next = None
  last_node.next = head
  return last_node

val4 = Node(4)
val3 = Node(3, val4)
val2 = Node(2, val3)
val1 = Node(1, val2)
head = val1
print("Linked list before moving")
print_link_sequence(head)
print("Linked list after moving tail to front")
tail_moved = tail_to_head(head)
print_link_sequence(tail_moved)
# Input: 1 -> 2 -> 3 -> 4
# Output: 4 -> 1 -> 2 -> 3
print()

"""Problem 9: Convert Singly Linked List to Doubly Linked List
One of the drawbacks of a linked list is that it's difficult to go backwards, because each Node only knows about the Node in front of it. (E.g., A -> B -> C)

A doubly linked list solves this problem! Instead of just having a next attribute, a doubly linked list also has a prev attribute that points to the Node before it. (E.g., A <-> B <-> C)

Update the code below to convert the singly linked list a doubly linked list."""

class Node:
  def __init__(self, value, next=None, prev=None):
    self.value = value
    self.next = next
    self.prev = prev

def single_to_doubly_linked_list(head):
  if head is None or head.next is None:
    return head

  current = head
  current.prev = None

  while current.next:
    new_node = current.next
    new_node.prev = current
    current = current.next
  return head

crazy_in_love = Node("Crazy in Love")
formation = Node("Formation")
texas_hold_em = Node("Texas Hold 'Em")
crazy_in_love.next = formation
formation.next = texas_hold_em
head = crazy_in_love
sll_dll = single_to_doubly_linked_list(head)
print_sll(head)
print_dll(sll_dll)
print()
# Current Singly Linked List: Crazy in Love -> Formation -> Texas Hold 'Em
# Desired Doubly Linked List: Crazy in Love <-> Formation <-> Texas Hold 'Em

"""Problem 10: Find Length of Doubly Linked List from Any Node
Write a function get_length() that takes in a node at an unknown position within a doubly linked list. The function should return the length of the entire list."""

class Node:
  def __init__(self, value, next=None, prev=None):
    self.value = value
    self.next = next
    self.prev = prev

def get_length(node):
  if not node:
    return 0
    
  count = 1
  # traverse towards the head
  left = node
  while left.prev:
    left = left.prev
    count += 1

  # travers towards the tail
  right = node
  while right.next:
    right = right.next
    count += 1
  return count  
  
node1 = Node(3)
node2 = Node(5)
node3 = Node(6)
node4 = Node(7)
node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2
node3.next = node4
node4.prev = node3
print_dll(node1)
print(get_length(node3))
# List: 3 <-> 5 <-> 6 <-> 7
# Input: node = 6
# Output: 4
print()

"""Return the value of the last node"""
class Node:
  def __init__(self, value, next_node = None):
    self.value = value
    self.next = next_node
    
def get_last(head):
  if not head:
    return None
    
  current = head
  while current.next:
    current = current.next
  return current.value
  
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3
print(get_last(node1))
print()

""" Get Grandchildren 
The following Person class defines a person with a last name, first name, and list of children. Each child in the list of children is an instance of Person.

The method add_child() adds a child to a person’s list of children. Add a method to the Person class called get_grandchildren() that returns a list of the person’s grandchildren."""

class Person:
  def __init__(self, first, last):
    self.last_name = last
    self.first_name = first
    self.children = []

  def add_child(self, child):
    self.children.append(child)

  def get_grandchildren(self):
    grandchildren = []
    for child in self.children:
      grandchildren.extend(child.children)
    return grandchildren
    
# Example 1:
johndoe = Person("John", "Doe")
janedoe = Person("Jane", "Doe")
jimmydoe = Person("Jimmy", "Doe")
johndoe.add_child(janedoe)
janedoe.add_child(jimmydoe)
grandchildren = johndoe.get_grandchildren()
print("Example 1 grandchildren:")
for grandchild in grandchildren:
    print(f"{grandchild.first_name} {grandchild.last_name}")
# Output: # [jimmydoe]
# Example 2:
johndoe = Person("John", "Doe")
janedoe = Person("Jane", "Doe")
johndoe.add_child(janedoe)
grandchildren2 = johndoe.get_grandchildren()
print("\nExample 2 grandchildren:")
for grandchild in grandchildren2:
    print(f"{grandchild.first_name} {grandchild.last_name}")
# Output: # []
print()

"""Extend Linked List Correct
Given the tail of a linked list and a list of values, write a function that adds each element in values as a
node with value values[i] to the end of the linked list. The nodes added to the linked list should maintain
the same order as the elements in value. The function does not need to return anything.

# linked list = a->b->c
# Example input: tail = c, values = ['d', 'e', 'f']
# expected output: a->b->c->d->e->f"""

class Node:
  def __init__(self, value, next_node = None):
    self.value = value
    self.next = next_node

def extend_linked_list(tail, values):
  current = tail
  for value in values:
    new_node = Node(value)
    current.next = new_node
    current = new_node
  return tail

a = Node("a")
b = Node("b")
c = Node("c")
a.next = b
b.next = c
head = a
tail = c
values = ['d', 'e', 'f']
extended_tail = extend_linked_list(tail, values)
print("Extended tail from tail c")
print_link_sequence(extended_tail)
print("All linked list")
print_link_sequence(head)
print()

"""Copy First N Nodes (LL) Correct
Given the head of a linked list and a positive integer n, create a new linked list that copies the first n nodes
of the original linked list. Return the head of the new list. If n is greater than or equal to the length of the
original list, the function should copy the entire list. If the list contains no nodes, return `None`.
Example Input: head=node1 , n=3
Hint: Make sure you are creating new Nodes for the copy list -- if you re-use the same nodes, it's not a true
copy!"""
class Node:
  def __init__(self, value, next_node = None):
    self.value = value
    self.next = next_node

def copy_first_n_nodes(head, n):
  if not head or n <= 0:
    return None

  new_head = Node(head.value)
  new_current = new_head
  current = head.next
  count = 1

  while current and count < n:
    new_node = Node(current.value)
    new_current.next = new_node
    new_current = new_current.next
    current = current.next
    count += 1
  return new_head

# Create a sample linked list: 1 -> 2 -> 3 -> 4 -> 5
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# Copy the first 3 nodes
new_head = copy_first_n_nodes(head, 3)

# Print the new list
current = new_head
while current:
    print(current.value, end=" -> " if current.next else "")
    current = current.next
# Output: 1 -> 2 -> 3
print()

from collections import defaultdict
dict = defaultdict(int)
str = "loveleetcode"
for i in str:
  dict[i] += 1
print(dict)
print()

from collections import Counter
c = Counter(str)
print(c)
print()

dict = {}
for i in str:
  dict[i] = dict.get(i, 0) + 1
print(dict)
print()

"""Problem 6: Put it in Reverse
Given the head of a singly linked list, reverse the list, and return the reversed list. You must reverse the list in place. Return the head of the reversed list.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity."""
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def print_list(node):
  current = node
  while current:
      print(current.value, end=" -> " if current.next else "")
      current = current.next
  print()

def reverse(head):
  if head is None and head.next is None:
    return None

  # initialize slow and fast pointer
  slow, fast = head, head

  # initialize three variables - next and prev pointing to None, current pointing to head
  prev = None
  next = None
  current = head
  # traverse the linked list while head is not None
  while current:
  # next points to current.next, current.next points to prev, prev points to current, current points to next
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