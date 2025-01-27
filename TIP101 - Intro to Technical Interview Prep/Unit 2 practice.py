# Session 1: Dictionaries in Python
# Problem Set Version 1
'''Problem 1: Subsequence
Write a function is_subsequence() that takes in a list of integers lst and a list of integers sequence as parameters. Given these two lists, determine whether the sequence list is a subsequence of the lst list. A subsequence of a list is a set of numbers that aren't necessarily adjacent but are in the same relative order as they appear in the list. Return True if sequence is a subsequence, and False otherwise.'''

def is_subsequence(lst, sequence):
	empty_list = []
	for num in lst:
		if num in sequence:
			empty_list.append(num)
	return empty_list == sequence

# Example usage:
lst = [1, 2, 3, 4, 5]
sequence = [2, 4]
print(is_subsequence(lst, sequence))  # Output: True

sequence = [2, 5, 4]
print(is_subsequence(lst, sequence))  # Output: False

lst = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
print(is_subsequence(lst, sequence))
print()

'''Problem 2: Create a Dictionary
Write a function create_dictionary() that takes in a list of keys and a list of values as parameters. The function returns a dictionary where each item in keys is paired with a corresponding item in values.

keys[i] should be paired with values[i] in the dictionary where 0 <= i <= len(keys). You may assume keys and values are the same length.'''
# def create_dictionary(keys, values):
#   return dict(zip(keys, values))

def create_dictionary(keys, values):
	dict = {}
	for k, v in zip(keys, values):
		dict[k] = v
	return dict

# Example Input:
keys = ["peanut", "dragon", "star", "pop", "space"]
values = ["butter", "fly", "fish", "corn", "ship"]
print(create_dictionary(keys, values))
print()

'''Problem 3: Print Pair
Write a function print_pair() that takes in a dictionary `dictionary` and a key `target` as parameters. The function looks for the `target` and when found, it prints the key and it's associated value as "Key: <key>" followed by "Value: <value>". If `target` is not in `dictionary`, print "That pair does not exist!".'''

def print_pair(dictionary, target):
	for k in dictionary:
		if k == target:
			return f"Key: {k} \nValue: {dictionary[k]}"
	return "That pair does not exist!"
	
dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
print(print_pair(dictionary, "patrick"))
print(print_pair(dictionary, "plankton"))
print(print_pair(dictionary, "spongebob"))
print()

'''Problem 4: Keys Versus Values
Write a function keys_v_values() that takes in a dictionary `dictionary` whose keys and values are both integers. The function should find the sum of all keys in the dictionary and the sum of all values.
If the sum of all keys is greater than the sum of all values, the function should return the string "keys".
If the sum of all values is greater than the sum of all keys, the function should return the string "values".
If keys and values have equal sums, the function should return the string "balanced".'''
def keys_v_values(dictionary):
	sum_keys = 0
	sum_values = 0
	for k, v in dictionary.items():
		sum_keys += k
		sum_values += v
	if sum_keys > sum_values:
		return "keys"
	elif sum_keys < sum_values:
		return "values"
	return "balanced"

dictionary1 = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
print(keys_v_values(dictionary1))   

dictionary2 = {100:10, 200:20, 300:30, 400:40, 500:50, 600:60}
print(keys_v_values(dictionary2))

dictionary2 = {100:100, 200:200, 300:300, 400:400, 500:500, 600:600}
print(keys_v_values(dictionary2))
print()

'''Problem 5: Restock Inventory
Write a function restock_inventory() that updates an inventory dictionary based on a restock list. It accepts two parameters:

current_inventory: a dictionary where each key-value pair represents an item and its current stock in the inventory
restock_list: a dictionary where each key-value pair represents an item and the quantity to be added to the inventory
If an item in restock_list is not present in the current_inventory, it should be added. The function should return the updated dictionary current_inventory.'''
def restock_inventory(current_inventory, restock_list):
	for keys in restock_list:
		if keys in current_inventory:
			current_inventory[keys] += restock_list[keys]
		else:
			current_inventory[keys] = restock_list[keys]
	return current_inventory

current_inventory = {
	"apples": 30,
	"bananas": 15,
	"oranges": 10
}

restock_list = {
	"oranges": 20,
	"apples": 10,
	"pears": 5
}
# Test
print(restock_inventory(current_inventory, restock_list))
print()

'''Problem 6: Calculate GPA
Write a function calculate_gpa() that calculates the grade point average (GPA) for a student based on their course grades and returns the gpa as a float. The function takes in a dictionary report_card as a parameter where each key-value pair represents a course and the grade received in that course respectively. The grades are represented as strings ("A", "B", "C", "D", "F") and each grade corresponds to a certain number of grade points:

"A" = 4
"B" = 3
"C" = 2
"D" = 1
"F" = 0

A GPA is calculated by finding the average of all grade points.'''
def calculate_gpa(report_card):
	gpa_rating = {"A":4, "B":3, "C":2, "D":1, "F":0}
	new_gpa = 0
	for key, value in report_card.items():
		new_gpa += gpa_rating[value] 
	return f'GPA: {round(new_gpa / len(report_card.keys()), 2)}'
		
# Test
report_card = {"Math": "A", "Science": "C", "History": "A", "Art": "B", "English": "B", "Spanish": "A"}
print(calculate_gpa(report_card))
print()

'''Problem 7: Best Book
Imagine you are working on a book review software like Goodreads. Write a function named highest_rated() that returns the book with the highest rating.

The function should take in a list of dictionaries named books as a parameter. Each dictionary represents data associated with a book, including its title, author, and rating. The function should return the dictionary for the book with the highest rating.'''
def highest_rated(books):
	max_val = -9999
	max_dict = {}
	for lst in books:
		if lst['rating'] > max_val:
			max_val = lst['rating']
			max_dict = lst
	return max_dict
	
# Test
books = [
    {"title": "Tomorrow, and Tomorrow, and Tomorrow",
     "author": "Gabrielle Zevin",
     "rating": 4.18
    },
    {"title": "A Fortune For Your Disaster",
     "author": "Hanif Abdurraqib",
     "rating": 4.47
    },
    {"title": "The Seven Husbands of Evenlyn Hugo",
     "author": "Taylor Jenkins Reid",
     "rating": 4.40
    }
]
print(highest_rated(books))
print()

# Problem Set Version 2
'''Problem 1: Is Monotonic
Write a function is_monotonic() that takes in a list nums as a parameter and checks if it is either monotone increasing or monotone decreasing.
A list is monotone increasing if every element is either greater than or equal to the element before it.
A list is monotone decreasing if every element is either less than or equal to the element before it.
The function should return True if the given list is either monotone increasing or decreasing and False otherwise.'''
def is_monotonic(nums):
	# check if list is monotonically increasing
	is_increasing = all(nums[i] <= nums[i+1] for i in range(len(nums) - 1))	
	# check if list is monotonically decreasing
	is_decreasing = all(nums[i] >= nums[i+1] for i in range(len(nums) - 1))
	return is_increasing or is_decreasing

nums1 = [1,2,2,3,10]
print(is_monotonic(nums1))

nums2 = [12,9,8,3,1]
print(is_monotonic(nums2))

nums3 = [1,1,1]
print(is_monotonic(nums3))

nums4 = [1,9,8,3,5]
print(is_monotonic(nums4))
print()

'''Problem 4: Sum Even Values
Write a function sum_even_values() that returns the sum of all even values in a given dictionary. Assume the dictionary values are all integers.'''

def sum_even_values(dictionary):
	sum_val = 0
	for k in dictionary:
		if dictionary[k] % 2 == 0:
			sum_val += dictionary[k]
	return sum_val

dictionary = {"a": 4, "b": 1, "c": 2, "d": 8, }
print(sum_even_values(dictionary))
print()

'''Problem 5: Merge Catalogs
Write a function merge_catalogs() that combines two product catalogs, catalog1 and catalog2 as parameters. Each parameter is a dictionary where each key-value pair represents a product name and its price, respectively. If the same product exists in both catalogs, the price from the second catalog should overwrite the price in the first. Return the updated first catalog dictionary.'''
def merge_catalogs(catalog1, catalog2):
	catalog1.update(catalog2)
	return catalog1
			
catalog1 = {"apple": 1.0, "banana": 0.5}
catalog2 = {"banana": 0.75, "cherry": 1.25}
print(merge_catalogs(catalog1, catalog2))
print()

'''Problem 6: Items to Restock
Write a function get_items_to_restock() that takes in a dictionary products that maps product names to their quantities and an integer restock_threshold as parameters. The function returns a list of products that have a value less than restock_threshold and need to be restocked. If products is empty, the function return an empty list.'''

def get_items_to_restock(products, restock_threshold):
	restock_list = []
	if not products:
		return restock_list
	for item, val in products.items():
		if val < restock_threshold:
			restock_list.append(item)
	return restock_list

products = {"Product1": 10, "Product2": 2, "Product3": 5, "Product4": 3}
restock_threshold = 5 # Example Output: ["Product2", "Product4"]
print(get_items_to_restock(products, restock_threshold))
print()

# Session 2: Dictionaries in Python II
# Problem Set Version 1
'''Problem 1: Cast Vote
Write a function cast_vote() that records a vote for a candidate in an election. The function accepts a dictionary votes that maps candidates to their current number of votes and a string candidate that represents the candidate the user would like to vote for. If the candidate doesn't exist, add them to the dictionary. The function should return the updated dictionary.'''

def cast_vote(votes, candidate):
	# loop through the dictionary list, if candidate exist, add 1 to candidate vote
	for item in votes:
		if candidate == item:
			votes[item] += 1
	# if they don't exist, update candidate vote with new record
	if candidate not in votes:
		votes[candidate] = 1
	return votes

votes = {"Alice": 5, "Bob": 3}
cast_vote(votes, "Alice")
print(votes)
cast_vote(votes, "Gina")
print(votes)
print()

'''Problem 2: Keys in Common
Write a function that takes in two dictionaries, dict1 and dict2 and finds all keys common to both dictionaries. The function returns a list of common keys.'''

def common_keys(dict1, dict2):
	common = [item for item in dict1 if item in dict2]
	return common

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}
common_list = common_keys(dict1, dict2)
print(common_list)
print()

'''Problem 4: Frequency Count
Write a function that takes in a list of integers nums and counts the number of occurrences of each integer. The function returns the result as a dictionary with integers as keys and their counts as values.'''

def count_occurrences(nums):
	my_dict = {}
	for num in nums:
		if num not in my_dict:
			my_dict[num] = 1
		else:
			my_dict[num] += 1
	return my_dict
	
nums = [1, 2, 2, 3, 3, 3, 4] # Example Output: {1: 1, 2: 2, 3: 3, 4: 1}
print(count_occurrences(nums))
print()

# Find mystery key
def mystery_fxn(key, val, dictionary):
	if key in dictionary:
		dictionary[key].append(val)
	else:
		dictionary[key] = val
	return dictionary

my_dict = {'a': [1, 2], 'b': [2, 5], 'c': [2, 6]}
output = mystery_fxn('c', 5, my_dict)
print(output)
print()

'''Problem 5: Find Majority Element
Write a function find_majority_element() that takes in a list of integers elements and finds the majority element in the list. A majority element is an element that appears more than n/2 times where n is the size of the list. If there is no majority element, return None.'''

def find_majority_element(elements):
	from collections import Counter
	my_count = Counter(elements)
	for item, val in my_count.items():
		if val > len(elements) // 2:
			return item
	return None

elements = [2, 2, 1, 1, 1, 2, 2]
print(find_majority_element(elements))
print()

'''Problem 4: Group By Frequency
Write a function group_by_frequency() that takes in a list lst and returns a dictionary where keys represent the frequency of unique elements within lst and values represent a list of elements with the same frequency.'''

def group_by_frequency(lst):
	from collections import defaultdict
	freq_count = defaultdict(int)
	for item in lst:
		freq_count[item] += 1
		
	result = defaultdict(list)
	for element, count in freq_count.items():
		result[count].append(element)
	return dict(result)

lst = ['a', 'b', 'c', 'd', 'd', 'c', 'e', 'e', 'e']
print(group_by_frequency(lst))
print()

'''Problem 7: Target Sum
Write a function two_sum() that takes in a list of integers nums and an integer target as parameters. The function should return the indices of the two numbers that add up to target. You may assume that each input would have exactly one solution and you may not use the same element twice. The function can return the indices in any order.'''

def two_sum(nums, target):
	left = 0
	right = len(nums) - 1
	while left < right:
		two_sums = nums[left] + nums[right]
		if two_sums == target:
			return [left, right]
		elif two_sums < target:
			left += 1
		else:
			right -= 1

nums = [2,7,11,15]
q_1 = two_sum(nums,9)
q_2 = two_sum(nums,18)

nums2 = [3,3]
q_3 = two_sum(nums2,6)
print(q_1)
print(q_2)
print(q_3)
print()