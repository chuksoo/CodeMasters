# Session 1: Strings & Arrays
# Standard Problem Set Version 1
''' Problem 1: Hundred Acre Wood
Write a function welcome() that prints the string "Welcome to The Hundred Acre Wood!".'''
def welcome():
	print("Welcome to The Hundred Acre Wood!")

'''Problem 2: Greeting
Write a function greeting() that accepts a single parameter, a string name, and prints the string 
"Welcome to The Hundred Acre Wood <name>! My name is Christopher Robin."
'''
def greeting(name):
	print(f"Welcome to The Hundred Acre Wood {name}! My name is Christopher Robin.")

'''Problem 3: Catchphrase
Write a function print_catchphrase() that accepts a string character as a parameter and prints the catchphrase of the given character as outlined in the table below.

Character	Catchphrase
"Pooh"	"Oh bother!"
"Tigger"	"TTFN: Ta-ta for now!"
"Eeyore"	"Thanks for noticing me."
"Christopher Robin"	"Silly old bear."
If the given character does not match one of the characters included above, print "Sorry! I don't know <character>'s catchphrase!"'''
def print_catchphrase(character):
	phrase_dict = {
		"Pooh": "Oh bother!",
		"Tigger": "TTFN: Ta-ta for now!",
		"Eeyore": "Thanks for noticing me.",
		"Christopher Robin": "Silly old bear."
		}
	return phrase_dict.get(character) if character in phrase_dict else "Sorry! I don't know <character>'s catchphrase!"

'''Problem 4: Return Item
Implement a function get_item() that accepts a 0-indexed list items and a non-negative integer x and returns the element at index x in items. 
If x is not a valid index of items, return None.'''
def get_item(items, x):
	return items[x] if x <= len(items) else None

'''Problem 5: Total Honey
Winnie the Pooh wants to know how much honey he has. Write a function sum_honey() that accepts a list of 
integers hunny_jars and returns the sum of all elements in the list. Do not use the built-in function sum().'''
def sum_honey(hunny_jars):
	accum = 0
	for val in hunny_jars:
		accum += val 
	return accum

'''Problem 6: Double Trouble
Help Winnie the Pooh double his honey! Write a function doubled() that accepts a list of integers 
hunny_jars as a parameter and multiplies each element in the list by two. Return the doubled list.'''
def doubled(hunny_jars):
	return [var*2 for var in hunny_jars]

'''Problem 7: Poohsticks
Winnie the Pooh and his friends are playing a game called Poohsticks where they drop sticks in a stream and race them. 
They time how long it takes each player's stick to float under Poohsticks Bridge to score each round.

Write a function count_less_than() to help Pooh and his friends determine how many players should move on to the next round of Poohsticks. 
count_less_than() should accept a list of integers race_times and an integer threshold and return the number of race times less than threshold.'''

def count_less_than(race_times, threshold):
	# count = 0
	# for i in race_times:
	# 	if i < threshold:
	# 		count += 1
	# return count
	return sum(val < threshold for val in race_times)

'''Problem 8: Pooh's To Do's
Write a function print_todo_list() that accepts a list of strings named tasks. The function should then number and print each task on a new line using the format:

Pooh's To Dos:
1. Task 1
2. Task 2
...'''
def print_todo_list(task):
	print("Pooh's To Dos:")
	for i, item in enumerate(task):
		print(f"{i+1}. {item}")
	
'''Problem 9: Pairs
Rabbit is very particular about his belongings and wants to own an even number of each thing he owns. 
Write a function can_pair() that accepts a list of integers item_quantities. Return True if each number in item_quantities is even. Return False otherwise.'''
def can_pair(item_quantities):
	for item in item_quantities:
		if item % 2 != 0:
			return False 
	return True

'''Problem 10: Split Haycorns
Piglet's has collected a big pile of his favorite food, haycorns, and wants to split them evenly amongst his friends. 
Write a function split_haycorns() to help Piglet determine the number of ways he can split his haycorns into even groups. 
split_haycorns() accepts a positive integer quantity as a parameter and returns a list of all divisors of quantity.'''
def split_haycorns(quantity):
	return [i for i in range(1, quantity + 1) if quantity % i == 0]

'''Problem 11: T-I-Double Guh-ER
Signs in the Hundred Acre Wood have been losing letters as Tigger bounces around stealing any letters he needs to spell out his name. 
Write a function tiggerfy() that accepts a string s, and returns a new string with the letters t, i, g, e, and r from it.'''
def tiggerfy(s):
	new_strg = ''
	remove_strg = ['t', 'i', 'g', 'e', 'r', 'T', 'I', 'G', 'E', 'R']
	for char in s:
		if char not in remove_strg:
			new_strg += char
	return new_strg

'''Problem 12: Thistle Hunt
Pooh, Piglet, and Roo are looking for thistles to gift their friend Eeyore. 
Write a function locate_thistles() that takes in a list of strings items and returns a list of the indices of any elements with value "thistle". 
The indices in the resulting list should be ordered from least to greatest.'''
def locate_thistles(items):
	return [i for i, val in enumerate(items) if val == 'thistle']

# Standard Problem Set Version 2
'''Problem 2: Mad Libs
Write a function madlib() that accepts one parameter, a string verb. The function should print the sentence: "I have one power. I never <verb>. - Batman".
'''
def madlib(verb):
	return f"I have one power. I never {verb}. - Batman"

'''Problem 3: Trilogy
Write a function trilogy() that accepts an integer year and prints the title of the Batman trilogy movie released that year as outlined below.

Year	Movie Title
2005	"Batman Begins"
2008	"The Dark Knight"
2012	"The Dark Knight Rises"
If the given year does not match one of the years in the table above, print "Christopher Nolan did not release a Batman movie in <year>."'''
def trilogy(year):
	movie_dict = {2005: "Batman Begins", 2008: "The Dark Knight", 2012: "The Dark Knight Rises"}
	return movie_dict[year] if year in movie_dict else "Christopher Nolan did not release a Batman movie in 1998."

'''Problem 4: Last
Implement a function get_last() that accepts a list of items items and returns the last item in the list. If the list is empty, return None.'''
def get_last(items):
	return None if items == [] else items[-1]

'''Problem 5: Concatenate
Write a function concatenate() that takes in a list of strings words and returns a string concatenated that concatenates all elements in words.
'''
def concatenate(words):
	new_word = ''
	for word in words:
		new_word += word
	return new_word

'''Problem 6: Squared
Write a function squared() that accepts a list of integers numbers as a parameter and squares each item in the list. Return the squared list.
'''
def squared(numbers):
	return [num**2 for num in numbers]

'''Problem 7: NaNaNa Batman!
Write a function nanana_batman() that accepts an integer x and prints the string "nanana batman!" where "na" is repeated x times. Do not use the * operator.
'''
def nanana_batman(x):
	if x <= 0:
		return 'batman!'
	new_strg = ''
	for i in range(x):
		new_strg += 'na'
	return new_strg + ' batman!'

'''Problem 8: Find the Villain
Write a function find_villain() that accepts a list crowd and a value villain as parameters and returns a list of all indices where the villain is found hiding in the crowd.
'''
def find_villain(crowd, villain):
	return [i for i, item in enumerate(crowd) if item == villain]

'''Problem 9: Odd
Write a function get_odds() that takes in a list of integers nums and returns a new list containing all the odd numbers in nums.
'''
def get_odds(nums):
	return [num for num in nums if num % 2 != 0]

'''Problem 10: Up and Down
Write a function up_and_down() that accepts a list of integers lst as a parameter. 
The function should return the number of odd numbers minus the number of even numbers in the list.'''
def up_and_down(lst):
	odd = even = 0
	for i in lst:
		if i % 2 != 0:
			odd += 1
		else:
			even += 1
	return odd - even

'''Problem 11: Running Sum
Write a function running_sum() that accepts a list of integers superhero_stats representing the number of crimes Batman has stopped each month in Gotham City. 
The function should modify the list to return the running sum such that superhero_stats[i] = sum(superhero_stats[0]...superhero_stats[i]). 
You must modify the list in place; you may not create any new lists as part of your solution.'''
import itertools
def running_sum(superhero_stats):
	return list(itertools.accumulate(superhero_stats))

'''Problem 12: Shuffle
Write a function shuffle() that accepts a list cards of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn]. Return the list in the form [x1,y1,x2,y2,...,xn,yn].
'''
def shuffle(cards):
	n = len(cards) // 2
	# new_lst = []
	# for i in range(len(cards)):
	# 	if i % 2 == 0:
	# 		new_lst.append(cards[i // 2])
	# 	else:
	# 		new_lst.append(cards[n + i // 2])
	# return new_lst
	return [cards[i // 2] if i % 2 == 0 else cards[n + i // 2] for i in range(len(cards))]

# Advanced Problem Set Version 1
'''Problem 1: Hunny Hunt
Write a function linear_search() to help Winnie the Pooh locate his lost items. The function accepts a list items and a target value as parameters. 
The function should return the first index of target in items, and -1 if target is not in the lst. Do not use any built-in functions.'''
def linear_search(lst, target):
	if target not in lst:
		return -1
	right = 0
	while right < len(lst):
		if lst[right] == target:
			return right
		right += 1

'''Problem 2: Bouncy, Flouncy, Trouncy, Pouncy
Tigger has developed a new programming language Tiger with only four operations and one variable tigger.

bouncy and flouncy both increment the value of the variable tigger by 1.
trouncy and pouncy both decrement the value of the variable tigger by 1.
Initially, the value of tigger is 1 because he's the only tigger around! 
Given a list of strings operations containing a list of operations, return the final value of tigger after performing all the operations.'''
def final_value_after_operations(operations):
	tigger = 1
	for i in operations:
		if i == 'bouncy' or i == 'flouncy':
			tigger += 1
		else:
			tigger -= 1
	return tigger

'''Problem 3: T-I-Double Guh-Er II
T-I-Double Guh-Er: That spells Tigger! Write a function tiggerfy() that accepts a string word and 
returns a new string that removes any substrings t, i, gg, and er from word. The function should be case insensitive.'''
def tiggerfy(word):
	result = []
	i = 0
	while i < len(word):
		if word[i:i+2] == 'gg' or word[i:i+2] == 'GG':
			i += 2
		elif word[i:i+2] == 'er' or word[i:i+2] == 'ER':
			i += 2
		elif word[i] == 't' or word[i] == 'T' or word[i] == 'i' or word[i] == 'I':
			i += 1
		else:
			result.append(word[i])
			i += 1
	return ''.join(result)
	
'''Problem 4: Non-decreasing Array
Given an array nums with n integers, write a function non_decreasing() that checks if nums could become non-decreasing by modifying at most one element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).'''	
def non_decreasing(nums):
	count = 0
	for i in range(len(nums) - 1):
		if nums[i] > nums[i + 1]:
			count += 1
			if count > 1:
				return f'{nums}: ' + str(False)
			# Case 1: Modify nums[1] (decrease it)
			if i == 0 or nums[i - 1] <= nums[i + 1]:
				nums[i] = nums[i + 1]
			# Case 2: Modify nums[i + 1] (increase it)
			else:
				nums[i + 1] = nums[i]
	return f'{nums}: ' + str(True)
		
'''Problem 5: Missing Clues
Christopher Robin set up a scavenger hunt for Pooh, but it's a blustery day and several hidden clues have blown away. 
Write a function find_missing_clues() to help Christopher Robin figure out which clues he needs to remake. 
The function accepts two integers lower and upper and a unique integer array clues. All elements in clues are within the inclusive range [lower, upper].

A clue x is considered missing if x is in the range [lower, upper] and x is not in clues.

Return the shortest sorted list of ranges that exactly covers all the missing numbers. 
That is, no element of clues is included in any of the ranges, and each missing number is covered by one of the ranges.'''
def find_missing_clues(clues, lower, upper):
   pass





if __name__ == "__main__":
	print("------ # Standard Problem Set 1 ------ ")
	welcome()
	print()
	greeting("Michael")
	greeting("Winnie the Pooh")
	print()
	character = "Pooh"
	print(print_catchphrase(character))
	character = "Piglet"
	print(print_catchphrase(character))
	print()
	items = ["piglet", "pooh", "roo", "rabbit"]
	x = 2
	print(get_item(items, x))
	items = ["piglet", "pooh", "roo", "rabbit"]
	x = 5
	print(get_item(items, x))
	print()
	hunny_jars = [2, 3, 4, 5]
	print(sum_honey(hunny_jars))
	hunny_jars = []
	print(sum_honey(hunny_jars))
	print()
	hunny_jars = [1, 2, 3]
	print(doubled(hunny_jars))
	print()
	race_times = [1, 2, 3, 4, 5, 6]
	threshold = 4
	print(count_less_than(race_times, threshold))
	race_times = []
	threshold = 4
	print(count_less_than(race_times, threshold))
	print()
	task = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
	print_todo_list(task)
	task = []
	print_todo_list(task)
	print()
	item_quantities = [2, 4, 6, 8]
	print(can_pair(item_quantities))
	item_quantities = [1, 2, 3, 4]
	print(can_pair(item_quantities))
	item_quantities = []
	print(can_pair(item_quantities))
	print()
	quantity = 6
	print(split_haycorns(quantity))
	quantity = 1
	print(split_haycorns(quantity))
	print()
	s = "suspicerous"
	print(tiggerfy(s))
	s = "Trigger"
	print(tiggerfy(s))
	s = "Hunny"
	print(tiggerfy(s))
	print()
	items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
	print(locate_thistles(items))
	items = ["book", "bouncy ball", "leaf", "red balloon"]
	print(locate_thistles(items))
	print()
	print("------ # Standard Problem Set 2 ------ ")
	verb = "give up"
	print(madlib(verb))
	verb = "nap"
	print(madlib(verb))
	print()
	year = 2008
	print(trilogy(year))
	year = 1998
	print(trilogy(year))
	print()
	items = ["spider man", "batman", "superman", "iron man", "wonder woman", "black adam"]
	print(get_last(items))
	items = []
	print(get_last(items))
	print()
	words = ["vengeance", "darkness", "batman"]
	print(concatenate(words))
	words = []
	print(concatenate(words))
	print()
	numbers = [1, 2, 3]
	print(squared(numbers))
	print()
	x = 6
	print(nanana_batman(x))
	x = 0
	print(nanana_batman(x))
	print()
	crowd = ['Batman', 'The Joker', 'Alfred Pennyworth', 'Robin', 'The Joker', 'Catwoman', 'The Joker']
	villain = 'The Joker'
	print(find_villain(crowd, villain))
	print()
	nums = [1, 2, 3, 4]
	print(get_odds(nums))
	nums = [2, 4, 6, 8]
	print(get_odds(nums))
	print()
	lst = [1, 2, 3]
	print(up_and_down(lst))
	lst = [1, 3, 5]
	print(up_and_down(lst))
	lst = [2, 4, 10, 2]
	print(up_and_down(lst))
	print()
	superhero_stats = [1, 2, 3, 4]
	print(running_sum(superhero_stats))
	superhero_stats = [1, 1, 1, 1, 1]
	print(running_sum(superhero_stats))
	superhero_stats = [3, 1, 2, 10, 1]
	print(running_sum(superhero_stats))
	print()
	cards = ['Joker', 'Queen', 2, 3, 'Ace', 7]
	print(shuffle(cards))
	cards = [9, 2, 3, 'Joker', 'Joker', 3, 2, 9]
	print(shuffle(cards))
	cards = [10, 10, 2, 2]
	print(shuffle(cards))
	print()
	print('------ # Advanced Problem Set Version 1------ ')
	items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
	target = 'hunny'
	print(linear_search(items, target))
	items = ['bed', 'blue jacket', 'red shirt', 'hunny']
	target = 'red balloon'
	print(linear_search(items, target))
	print()
	operations = ["trouncy", "flouncy", "flouncy"]
	print(final_value_after_operations(operations))
	operations = ["bouncy", "bouncy", "flouncy"]
	print(final_value_after_operations(operations))
	print()
	word = "Trigger"
	print(tiggerfy(word))
	word = "eggplant"
	print(tiggerfy(word))
	word = "Choir"
	print(tiggerfy(word))
	print()
	nums = [4, 2, 3]
	print(non_decreasing(nums))
	nums = [4, 2, 1]
	print(non_decreasing(nums))	
	nums = [6, 5, 4, 3, 2, 1]
	print(non_decreasing(nums))
	nums = [3, 4, 6, 5, 4, 2, 1]
	print(non_decreasing(nums))
	print()
	clues = [0, 1, 3, 50, 75]
	lower = 0
	upper = 99
	print(find_missing_clues(clues, lower, upper))
	clues = [-1]
	lower = -1
	upper = -1
	print(find_missing_clues(clues, lower, upper))
	print()