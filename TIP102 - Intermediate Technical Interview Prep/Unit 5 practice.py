# Session 1: OOP & Linked Lists
# Standard Problem Set Version 1
'''Problem 1: New Horizons
Step 1: Copy the following code into your IDE.

# Step 2: Instantiate an instance of the class Villager, which represents characters in Animal Crossing. Store the instance in a variable named apollo.

# The Villager object created should have the name "Apollo", the species "Eagle", and the catchphrase "pah".'''
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

alice.set_catchphrase("sweet dreams")
print(alice.catchphrase)
alice.set_catchphrase("#?!")
print(alice.catchphrase)   

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
            for item in valid_lst:
                if item == item_name:
                    self.furniture.append(item_name)
    

    
alice = Villager("Alice", "Koala", "guvnor")
print(alice.furniture)

alice.add_item("acoustic guitar")
print(alice.furniture)

alice.add_item("cacao tree")
print(alice.furniture)

alice.add_item("nintendo switch")
print(alice.furniture)