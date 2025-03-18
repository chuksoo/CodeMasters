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
    # sort the clues list
    clues.sort()
    # iniialize missing range
    missing_range = []
    # handle gap befoe fist clue
    if lower < clues[0]:
        missing_range.append([lower, clues[0] - 1])
    # check gaps between clues
    for i in range(len(clues) - 1):
        if clues[i] + 1 < clues[i + 1]:
            missing_range.append([clues[i] + 1, clues[i + 1] - 1])
    # handle gap after last clue
    if upper > clues[-1]:
        missing_range.append([clues[-1] + 1, upper])
    return missing_range

'''Problem 6: Vegetable Harvest
Rabbit is collecting carrots from his garden to make a feast for Pooh and friends. 
Write a function harvest() that accepts a 2D n x m matrix vegetable_patch and returns the number of of carrots that are ready to harvest in the vegetable patch. 
A carrot is ready to harvest if vegetable_patch[i][j] has value 'c'.

Assume n = len(vegetable_patch) and m = len(vegetable_patch[0]). 0 <= i < n and 0 <= j < m.'''
def harvest(vegetable_patch):
    count = 0
    for lst in vegetable_patch:
        for item in lst:
            if 'c' in item:
                count += 1
    return count

'''Problem 7: Eeyore's House
Eeyore has collected two piles of sticks to rebuild his house and needs to choose pairs of sticks whose lengths are the right proportion. 
Write a function good_pairs() that accepts two integer arrays pile1 and pile2 where each integer represents the length of a stick. 
The function also accepts a positive integer k. The function should return the number of good pairs.

A pair (i, j) is called good if pile1[i] is divisible by pile2[j] * k. Assume 0 <= i <= len(pile1) - 1 and 0 <= j <= len(pile2) - 1.'''

def good_pairs(pile1, pile2, k):
    count = 0
    for num1 in pile1:
        for num2 in pile2:
            if num1 % (num2 * k) == 0:
                count += 1
    return count

'''Problem 8: Local Maximums
Write a function local_maximums() that accepts an n x n integer matrix grid and returns an integer matrix local_maxes of size (n - 2) x (n - 2) such that:

local_maxes[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1.
In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.'''

def local_maximums(grid):
    n = len(grid)
    local_maxes = [[0] * (n - 2) for _ in range(n - 2)]

    for i in range(n - 2):
        for j in range(n - 2):
            # extract 3x3 submatrix and ind maximum value
            max_value = max(
                grid[i][j], grid[i][j+1], grid[i][j+2],
                grid[i+1][j], grid[i+1][j+1], grid[i+1][j+2],
                grid[i+2][j], grid[i+2][j+1], grid[i+2][j+2]
                )
            # store max value
            local_maxes[i][j] = max_value

    return local_maxes

# Advanced Problem Set Version 2
'''Problem 1: Words Containing Character
Write a function words_with_char() that accepts a list of strings words and a character x. 
Return a list of indices representing the words that contain the character x. The returned list may be in any order.
'''
def words_with_char(words, x):
    result = []
    for i, word in enumerate(words):
        if x in word:
            result.append(i)
    return result

'''Problem 2: HulkSmash
Write a function hulk_smash() that accepts an integer n and returns a 1-indexed string array answer where:

answer[i] == "HulkSmash" if i is divisible by 3 and 5.
answer[i] == "Hulk" if i is divisible by 3.
answer[i] == "Smash" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.'''
def hulk_smash(n):
    answer = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            answer.append("HulkSmash")
        elif i % 3 == 0:
            answer.append("Hulk")
        elif i % 5 == 0:
            answer.append("Smash") 
        else:
            answer.append(str(i))
    return answer

'''Problem 3: Encode
The Riddler is planning to leave a coded message to lead Batman into a trap. 
Write a function shuffle() that takes in a string, the Riddler's message, and encodes it using an integer array indices. 
The message will be shuffled such that the character at the ith position in message moves to index indices[i] in the shuffled string. 
You may assume len(message) is equal to the len(indices).'''

def shuffle_encode(message, indices):
    message_map = {}
    indices = indices
    for i, val in enumerate(message):
        message_map[i] = val
    
    result = ''
    for num in indices:
        result += message_map[num]
    return result

'''Problem 4: Good Samaritan
Superman is doing yet another good deed, using his power of flight to distribute meals for the Metropolis Food Bank. 
He wants to distribute meals in the least number of trips possible.

Metropolis Food Bank currently stores meals in n packs where the ith pack contains meals[i] meals. 
There are also m empty boxes which can contain up to capacity[i] meals.

Given an array meals of length n and capacity of size m, write a function minimum_boxes() that returns the minimum number of boxes 
needed to redistribute the n packs of meals into boxes.

Note that meals from the same pack can be distributed into different boxes.'''
def minimum_boxes(meals, capacity):
    total_meals = sum(meals)
    capacity.sort(reverse=True)

    box_used = 0
    meals_distributed = 0

    for box_capacity in capacity:
        if meals_distributed >= total_meals:
            break

        meals_distributed += box_capacity
        box_used += 1
    return box_used

'''Problem 5: Heist
The legendary outlaw Robin Hood is looking for the target of his next heist. 
Write a function wealthiest_customer() that accepts an m x n 2D integer matrix accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. 
Return a list [i, w] where i is the 0-based index of the wealthiest customer and w is the total wealth of the wealthiest customer.

If multiple customers have the highest wealth, return the index of any customer.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.'''
def wealthiest_customer(accounts):
    max_wealth = 0
    wealthiest_customer = 0
    for i, val in enumerate(accounts):
        sum_account = sum(val)
        if sum_account >= max_wealth:
            max_wealth = sum_account
            wealthiest_customer = i
    return [wealthiest_customer, max_wealth]
    
'''Problem 6: Smaller Than
Write a function smaller_than_current that accepts a list of integers nums and, for each element in the list nums[i], 
determines the number of other elements in the array that are smaller than it. More formally, for each nums[i] count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer as a list.'''
def smaller_than_current(nums):
    result = []
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if nums[j] < nums[i]:
                count += 1
        result.append(count)
    return result

'''Problem 7: Diagonal
Write a function diagonal_sum() that accepts a 2D n x n matrix grid and returns the sum of the matrix diagonals. 
Only include the sum of all the elements on the primary diagonal and all the elements in the secondary diagonal that are not part of the primary diagonal.

The primary diagonal is all cells in the matrix along a line drawn from the top-left cell in the matrix to the bottom-right cell. 
The secondary diagonal is all cells in the matrix along a line drawn from the top-right cell in the matrix to the bottom-left cell.'''
def diagonal_sum(grid):
    n = len(grid)
    diag_sum = 0

    for i in range(len(grid)):
        diag_sum += grid[i][i]
        diag_sum += grid[i][n - i - 1]
    if n % 2 != 0:
        diag_sum -= grid[n // 2][n // 2]
    return diag_sum
    
'''Problem 8: Defuse the Bomb
Batman has a bomb to defuse, and his time is running out! His butler, Alfred, is on the phone providing him with a circular array code of length n and key k.

To decrypt the code, Batman must replace every number. All the numbers are replaced simultaneously.

If k > 0, replace the ith number with the sum of the next k numbers.
If k < 0, replace the ith number with the sum of the previous k numbers.
If k == 0, replace the ith number with 0.
As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].

Given the circular array code and an integer key k, write a function decrypt() that returns the decrypted code to defuse the bomb!'''
def defuse(code, k):
    n = len(code)
    # base case: k == 0, return an array of zeros of length n
    if k == 0:
        return [0] * n
    # create extended code i.e [5, 7, 1, 4] + [5, 7, 1, 4] = [5, 7, 1, 4, 5, 7, 1, 4]
    extended_code = code + code
    # initialize result array of length n filled with zeros
    result = [0] * n
    for i in range(0, n):
    # if k > 0, use sliding window sum to compute sum of next k elements
        if k > 0:
            result[i] = sum(extended_code[i+1: i+1+k])
    # else, compute sum of previous k element
        else:
            result[i] = sum(extended_code[i+n+k: i+n])
    # return result
    return result

# Session 1: Strings & Arrays
# Standard Problem Set Version 1
'''Problem 1: Reverse Sentence
Write a function reverse_sentence() that takes in a string sentence and returns the sentence with the order of the words reversed. 
The sentence will contain only alphabetic characters and spaces to separate the words. If there is only one word in the sentence, 
the function should return the original string.'''
def reverse_sentence(sentence):
    # sentence_lst = sentence.split()
    # sentence_lst = sentence_lst[::-1]
    # return ' '.join(sentence_lst)
    return ' '.join(sentence.split()[::-1])

'''Problem 2: Goldilocks Number
In the extended universe of fictional bears, Goldilocks finds an enticing list of numbers in the Three Bears' house. 
She doesn't want to take a number that's too high or too low - she wants a number that's juuust right. 
Write a function goldilocks_approved() that takes in the list of distinct positive integers nums and returns any number from the list 
that is neither the minimum nor the maximum value in the array, or -1 if there is no such number.

Return the selected integer.'''
def goldilocks_approved(nums):
    min_val, max_val = min(nums), max(nums)
    for num in nums:
        if num != min_val and num != max_val:
            return num
    return -1

'''Problem 3: Delete Minimum
Pooh is eating all of his hunny jars in order of smallest to largest. Given a list of integers hunny_jar_sizes, 
write a function delete_minimum_elements() that continuously removes the minimum element until the list is empty. 
Return a new list of the elements of hunny_jar_sizes in the order in which they were removed.'''
def delete_minimum_elements(hunny_jar_sizes):
    result = []
    min_val = min(hunny_jar_sizes)
    while len(hunny_jar_sizes) != 0:
        min_val = min(hunny_jar_sizes)
        result.append(min_val)
        hunny_jar_sizes.remove(min_val)   
    return result

'''Problem 4: Sum of Digits
Write a function sum_of_digits() that accepts an integer num and returns the sum of num's digits.'''
def sum_of_digits(num):
    digit_sum = 0
    while num > 0:
        digit_sum += num % 10
        num //= 10
    return digit_sum
    
'''Problem 5: Bouncy, Flouncy, Trouncy, Pouncy
Tigger has developed a new programming language Tiger with only four operations and one variable tigger.

bouncy and flouncy both increment the value of the variable tigger by 1.
trouncy and pouncy both decrement the value of the variable tigger by 1.
Initially, the value of tigger is 1 because he's the only tigger around! 
Given a list of strings operations containing a list of operations, return the final value of tigger after performing all the operations.'''
def final_value_after_operations(operations):
    tigger = 1
    for item in operations:
        if item == 'bouncy' or item == 'flouncy':
            tigger += 1
        else:
            tigger -= 1
    return tigger

'''Problem 6: Acronym
Given an array of strings words and a string s, implement a function is_acronym() that returns True if s is an acronym of words and returns False otherwise.

The string s is considered an acronym of words if it can be formed by concatenating the first character of each string in words in order. 
For example, "pb" can be formed from ["pooh"", "bear"], but it can't be formed from ["bear", "pooh"].'''
def is_acronym(words, s):
    acronym = ''
    for word in words:
        acronym += word[0]
    return acronym == s

'''
Problem 7: Good Things Come in Threes
Write a function make_divisible_by_3() that accepts an integer array nums. In one operation, you can add or subtract 1 from any element of nums. 
Return the minimum number of operations to make all elements of nums divisible by 3.
'''
def make_divisible_by_3(nums):
    count = 0
    for num in nums:
        if num % 3 != 0:
            count += 1
    return count

'''Problem 8: Exclusive Elements
Given two lists lst1 and lst2, write a function exclusive_elemts() that returns a new list that contains the elements
which are in lst1 but not in lst2 and the elements that are in lst2 but not in lst1.'''
def exclusive_elemts(lst1, lst2):
    # Time: O(N+M), Space: O(N*M)
    # intersect = list(set(lst1).intersection(set(lst2)))
    # first_exclusive = [x for x in lst1 if x not in intersect]
    # second_exclusive = [x for x in lst2 if x not in intersect]
    # return first_exclusive + second_exclusive

    # Time: O(N+M), Space: O(N+M)
    set1, set2 = set(lst1), set(lst2)
    return list(set1 - set2) + list(set2 - set1)

'''Problem 9: Merge Strings Alternately
Write a function merge_alternately() that accepts two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. 
If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.'''
def merge_alternately(word1, word2):
    merged = []
    min_length = min(len(word1), len(word2))
    for i in range(min_length):
        merged.append(word1[i])
        merged.append(word2[i])

    if len(word1) > len(word2):
        merged.append(word1[min_length:])
    elif len(word2) > len(word1):
        merged.append(word2[min_length:])
    return ''.join(merged)

'''Problem 10: Eeyore's House
Eeyore has collected two piles of sticks to rebuild his house and needs to choose pairs of sticks whose lengths are the right proportion. 
Write a function good_pairs() that accepts two integer arrays pile1 and pile2 where each integer represents the length of a stick. 
The function also accepts a positive integer k. The function should return the number of good pairs.

A pair (i, j) is called good if pile1[i] is divisible by pile2[j] * k. Assume 0 <= i <= len(pile1) - 1 and 0 <= j <= len(pile2) - 1'''
def good_pairs(pile1, pile2, k):
    count = 0
    for i in range(len(pile1)):
        for j in range(len(pile2)):
            if pile2[j] != 0 and pile1[i] % (pile2[j] * k) == 0:
                count += 1
    return count

# Standard Problem Set Version 2

'''Problem 1: String Array Equivalency
Given two string arrays word1 and word2, return True if the two arrays represent the same string, and False otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.'''
def are_equivalent(word1, word2):
    word1_str = ''.join(x for x in word1)
    word2_str = ''.join(x for x in word2)
    return len(word1_str) == len(word2_str)

'''Problem 2: Count Even Strings
Implement a function count_evens() that accepts a list of strings lst as a parameter. 
The function should return the number of strings with an even length in the list.
'''
def count_evens(lst):
    count = 0
    for item in lst:
        if len(item) % 2 == 0:
            count += 1
    return count
    
'''Problem 3: Secret Identity
Write a function remove_name() to keep Batman's secret identity hidden. 
The function accepts a list of names people and a string secret_identity and should return the list with any instances of secret_identity removed. 
The list must be modified in place; you may not create any new lists as part of your solution. Relative order of the remaining elements must be maintained.'''
def remove_name(people, secret_identity):
    # for num in people:
    #     if num == secret_identity:
    #         people.remove(num)
    # return people
    write = 0
    for read in range(len(people)):
        if people[read] != secret_identity:
            people[write] = people[read]
            write += 1
    del people[write:]
    return people
	
'''Problem 4: Count Digits
Given a non-negative integer n, write a function count_digits() that returns the number of digits in n. You may not cast n to a string.'''
def count_digits(n):
    if n == 0:
        return 1
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count
    
'''Problem 5: Move Zeroes
Write a function move_zeroes that accepts an integer array nums and returns a new list with all 0s moved to the end of list. 
The relative order of the non-zero elements in the original list should be maintained.'''
def move_zeroes(lst):
    left = 0
    for right in range(len(lst)):
        if lst[right] != 0:
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
    return lst

'''Problem 6: Reverse Vowels of a String
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases and more than once.'''
def reverse_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    s = list(s)
    start, end = 0, len(s) - 1
    while start < end:
        if s[start] in vowels and s[end] in vowels:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        elif s[start] in vowels and s[end] not in vowels:
            end -= 1
        else:
            start += 1
    return ''.join(s)

'''Problem 7: Vantage Point
Batman is going on a scouting trip, surveying an area where he thinks Harley Quinn might commit her next crime spree. 
The area has many hills with different heights and Batman wants to find the tallest one to get the best vantage point. 
His scout trip consists of n + 1 points at different altitudes. Batman starts his trip at point 0 with altitude 0.

Write a function highest_altitude() that accepts an integer array gain of length n where gain[i] is the net gain in altitude 
between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.'''
def highest_altitude(gain):
    max_alt = 0
    current_alt = 0
    for num in gain:
        current_alt += num
        max_alt = max(max_alt, current_alt)
    return max_alt

'''Problem 8: Left and Right Sum Differences
Given a 0-indexed integer array nums, write a function left_right_difference that returns a 0-indexed integer array answer where:

len(answer) == len(nums)
answer[i] = left_sum[i] - right_sum[i]
Where:

left_sum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, left_sum[i] = 0
right_sum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, right_sum[i] = 0'''
def left_right_difference(nums):
    answer = [0] * len(nums)
    for i in range(len(nums)):
        if i == 0:
            left_sum = 0
            right_sum = sum(nums[i+1:])
        else:
            left_sum, right_sum = sum(nums[:i]), sum(nums[i+1:])
        answer[i] = left_sum - right_sum
    return answer

'''Problem 9: Common Cause
Write a function common_elements() that takes in two lists lst1 and lst2 and returns a list of the elements that are common to both lists.'''

def common_elements(lst1, lst2):
    return [x for x in lst1 if x in lst2]

'''Problem 10: Exposing Superman
Metropolis has a population n, with each citizen assigned an integer id from 1 to n. There's a rumor that Superman is an ordinary citizen among this group.

If Superman is an ordinary citizen, then:

Superman trusts nobody.
Everybody (except for Superman) trusts Superman.
There is exactly one citizen that satisfies properties 1 and 2.
Write a function expose_superman() that accepts a 2D array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. 
If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

Return the label of Superman if he is hiding amongst the population and can be identified, or return -1 otherwise.'''
def expose_superman(trust, n):
    if n == 1 and not trust:
        return 1
    
    # initialize trust_someone and trusted_by array of size n+1 with zeros
    trust_someone = [0] * (n+1)
    trusted_by = [0] * (n+1)

    for (a, b) in trust:
        trust_someone[a] += 1 # a trusts someone
        trusted_by[b] += 1 # b is trusted by someone
    
    # find persons who has:
    # 1. Trusts nobody -> trust_someone[i] == 0
    # 2. Trusted by everyone else -> trusted_by[i] == n - 1
    for i in range(1, n+1):
        if  trust_someone[i] == 0 and trusted_by[i] == n - 1:
            return i
    return -1 # No Superman found  
            
# Advanced Problem Set Version 1
'''Problem 1: Transpose Matrix
Write a function transpose() that accepts a 2D integer array matrix and returns the transpose of matrix. 
The transpose of a matrix is the matrix flipped over its main diagonal, swapping the rows and columns.'''
def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
    return transposed

'''Problem 2: Two-Pointer Reverse List
Write a function reverse_list() that takes in a list lst and returns elements of the list in reverse order. 
The list should be reversed in-place without using list slicing (e.g. lst[::-1]).

Instead, use the two-pointer approach, which is a common technique in which we initialize two variables (also called a pointer in this context) 
to track different indices or places in a list or string, then moves the pointers to point at new indices based on certain conditions. 
In the most common variation of the two-pointer approach, we initialize one variable to point at the beginning of a list and a second variable/pointer 
to point at the end of list. We then shift the pointers to move inwards through the list towards each other, until our problem is solved or the pointers 
reach the opposite ends of the list.
'''
def reverse_list(lst):
    left, right = 0, len(lst) - 1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    return lst

'''Problem 3: Remove Duplicates
Write a function remove_dupes() that accepts a sorted array items, and removes the duplicates in-place such that each element appears only once. 
Return the length of the modified array. You may not create another array; your implementation must modify the original input array items.'''
def remove_dupes(items):
    left = 0
    for right in range(1, len(items)):
        if items[left] != items[right]:
            left += 1
            items[left] = items[right]
    return left + 1

'''Problem 4: Sort Array by Parity
Given an integer array nums, write a function sort_by_parity() that moves all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.'''
def sort_by_parity(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        if nums[left] % 2 != 0 and nums[right] % 2 == 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        elif nums[left] % 2 == 0:
            left += 1
        else:
            right -= 1
    return nums

'''Problem 5: Container with Most Honey
Christopher Robin is helping Pooh construct the biggest hunny jar possible. Help his write a function that accepts an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most honey.

Return the maximum amount of honey a container can store.

Notice that you may not slant the container.'''
def most_honey(height):
    left, right = 0, len(height) - 1
    max_area = 0
    while left < right:
        width = right - left
        container_height = min(height[left], height[right])
        area = width * container_height
        max_area = max(max_area, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area

'''Problem 6: Merge Intervals
Write a function merge_intervals() that accepts an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.
'''
def merge_intervals(intervals):
    result_lst = [intervals[0]]
    if not intervals:
        return result_lst
    
    intervals = sorted(intervals)

    for i in range(1, len(intervals)):
        if intervals[i][0] <= result_lst[-1][1]:
            result_lst[-1][1] = max(result_lst[-1][1], intervals[i][1])
        else:
            result_lst.append(intervals[i])

    return result_lst
    

    
if __name__ == "__main__":
    print("-------- # Session 1: Strings & Arrays -------- ")
    print("------ # Standard Problem Set Version 1 ------ ")
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
    print("------ # Standard Problem Set Version 2 ------ ")
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
    print('------ # Advanced Problem Set Version 1 ------ ')
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
    vegetable_patch = [
    ['x', 'c', 'x'],
    ['x', 'x', 'x'],
    ['x', 'c', 'c'],
    ['c', 'c', 'c']
    ]
    print(harvest(vegetable_patch))
    print()
    pile1 = [1, 3, 4]
    pile2 = [1, 3, 4]
    k = 1
    print(good_pairs(pile1, pile2, k))
    pile1 = [1, 2, 4, 12]
    pile2 = [2, 4]
    k = 3
    print(good_pairs(pile1, pile2, k))
    print()
    grid = [
    [9, 9, 8, 1],
    [5, 6, 2, 6],
    [8, 2, 6, 4],
    [6, 2, 2, 2]
    ]
    print(local_maximums(grid))

    grid = [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 2, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1]
    ]
    print(local_maximums(grid))
    print()
    print('------ # Advanced Problem Set Version 2 ------ ')
    words = ["batman", "superman"]
    x = "a"
    print(words_with_char(words, x))
    words = ["black panther", "hulk", "black widow", "thor"]
    x = "a"
    print(words_with_char(words, x))
    words = ["star-lord", "gamora", "groot", "rocket"]
    x = "z"
    print(words_with_char(words, x))
    print()
    n = 3
    print(hulk_smash(n))
    n = 5
    print(hulk_smash(n))
    n = 15
    print(hulk_smash(n))
    print()
    message = "evil"
    indices = [3, 1, 2, 0]
    print(shuffle_encode(message, indices))
    message = "findme"
    indices = [0, 1, 2, 3, 4, 5]
    print(shuffle_encode(message, indices))
    print()
    meals = [1, 3, 2]
    capacity = [4, 3, 1, 5, 2]
    print(minimum_boxes(meals, capacity))
    meals = [5, 5, 5]
    capacity = [2, 4, 2, 7]
    print(minimum_boxes(meals, capacity))
    print()
    accounts = [
        [1, 2, 3],
        [3, 2, 1]
    ]
    print(wealthiest_customer(accounts))

    accounts = [
        [1, 5],
        [7, 3],
        [3, 5]
    ]
    print(wealthiest_customer(accounts))

    accounts = [
        [2, 8, 7],
        [7, 1, 3],
        [1, 9, 5]
    ]
    print(wealthiest_customer(accounts))
    print()
    nums = [8, 1, 2, 2, 3]
    print(smaller_than_current(nums))
    nums = [6, 5, 4, 8]
    print(smaller_than_current(nums))
    nums = [7, 7, 7, 7]
    print(smaller_than_current(nums))
    print()
    grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]
    print(diagonal_sum(grid))
    grid = [
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]
    ]
    print(diagonal_sum(grid))
    grid = [
        [5]
    ]
    print(diagonal_sum(grid))
    print()
    code = [5, 7, 1, 4]
    k = 3
    print(defuse(code, k))

    code = [1, 2, 3, 4]
    k = 0
    print(defuse(code, k))

    code = [2, 4, 9, 3]
    k = -2
    print(defuse(code, k))
    print()
    print("-------- # Session 2: Strings & Arrays -------- ")
    print("------ # Standard Problem Set Version 1 ------ ")
    sentence = "tubby little cubby all stuffed with fluff"
    print(reverse_sentence(sentence))
    sentence = "Pooh"
    print(reverse_sentence(sentence))
    print()
    nums = [3, 2, 1, 4]
    print(goldilocks_approved(nums))
    nums = [1, 2]
    print(goldilocks_approved(nums))
    nums = [2, 1, 3]
    print(goldilocks_approved(nums))
    print()
    hunny_jar_sizes = [5, 3, 2, 4, 1]
    print(delete_minimum_elements(hunny_jar_sizes))
    hunny_jar_sizes = [5, 2, 1, 8, 2]
    print(delete_minimum_elements(hunny_jar_sizes))
    print()
    num = 423
    print(sum_of_digits(num))
    num = 4
    print(sum_of_digits(num))
    print()
    operations = ["trouncy", "flouncy", "flouncy"]
    print(final_value_after_operations(operations))
    operations = ["bouncy", "bouncy", "flouncy"]
    print(final_value_after_operations(operations))
    print()
    words = ["christopher", "robin", "milne"]
    s = "crm"
    print(is_acronym(words, s))
    words = ["christopher", "toronto", "russia"]
    s = "cpr"
    print(is_acronym(words, s))
    words = []
    s = "cpr"
    print(is_acronym(words, s))
    print()
    nums = [1, 2, 3, 4]
    print(make_divisible_by_3(nums))
    nums = [3, 6, 9]
    print(make_divisible_by_3(nums))
    print()
    lst1 = ["pooh", "roo", "piglet"]
    lst2 = ["piglet", "eeyore", "owl"]
    print(exclusive_elemts(lst1, lst2))
    lst1 = ["pooh", "roo"]
    lst2 = ["piglet", "eeyore", "owl", "kanga"]
    print(exclusive_elemts(lst1, lst2))
    lst1 = ["pooh", "roo", "piglet"]
    lst2 = ["pooh", "roo", "piglet"]
    print(exclusive_elemts(lst1, lst2))
    print()
    word1 = "wol"
    word2 = "oze"
    print(merge_alternately(word1, word2))
    word1 = "hfa"
    word2 = "eflump"
    print(merge_alternately(word1, word2))
    word1 = "eyre"
    word2 = "eo"
    print(merge_alternately(word1, word2))
    print()
    pile1 = [1, 3, 4]
    pile2 = [1, 3, 4]
    k = 1
    print(good_pairs(pile1, pile2, k))
    pile1 = [1, 2, 4, 12]
    pile2 = [2, 4]
    k = 3
    print(good_pairs(pile1, pile2, k))
    print()
    print("------ # Standard Problem Set Version 2 ------ ")
    word1 = ["bat", "man"]
    word2 = ["b", "atman"]
    print(are_equivalent(word1, word2))
    word1 = ["alfred", "pennyworth"]
    word2 = ["alfredpenny", "word"]
    print(are_equivalent(word1, word2))
    word1  = ["cat", "wom", "an"]
    word2 = ["catwoman"]
    print(are_equivalent(word1, word2))
    print()
    lst = ["na", "nana", "nanana", "batman", "!"]
    print(count_evens(lst))
    lst = ["the", "joker", "robin"]
    print(count_evens(lst))
    lst = ["you", "either", "die", "a", "hero", "or", "you", "live", "long", "enough", "to", "see", "yourself", "become", "the", "villain"]
    print(count_evens(lst))
    print()
    people = ['Batman', 'Superman', 'Bruce Wayne', 'The Riddler', 'Bruce Wayne']
    secret_identity = 'Bruce Wayne'
    print(remove_name(people, secret_identity))
    print()
    n = 964
    print(count_digits(n))
    n = 0
    print(count_digits(n))
    print()
    lst = [1, 0, 2, 0, 3, 0]
    print(move_zeroes(lst))
    print()
    s = "robin"
    print(reverse_vowels(s))
    s = "BATgirl"
    print(reverse_vowels(s))
    s = "batman"
    print(reverse_vowels(s))
    print()
    gain = [-5, 1, 5, 0, -7]
    print(highest_altitude(gain))
    gain = [-4, -3, -2, -1, 4, 3, 2]
    print(highest_altitude(gain))
    print()
    nums = [10, 4, 8, 3]
    print(left_right_difference(nums))
    nums = [1]
    print(left_right_difference(nums))
    print()
    lst1 = ["super strength", "super speed", "x-ray vision"]
    lst2 = ["super speed", "time travel", "dimensional travel"]
    print(common_elements(lst1, lst2))
    lst1 = ["super strength", "super speed", "x-ray vision"]
    lst2 = ["martial arts", "stealth", "master detective"]
    print(common_elements(lst1, lst2))
    print()
    n = 2
    trust = [[1, 2]]
    print(expose_superman(trust, n))
    n = 3
    trust = [[1, 3], [2, 3]]
    print(expose_superman(trust, n))
    n = 3
    trust = [[1, 3], [2, 3], [3, 1]]
    print(expose_superman(trust, n))
    print()
    print('------ # Advanced Problem Set Version 1 ------ ')
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(transpose(matrix))
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    print(transpose(matrix))
    print()
    lst = ["pooh", "christopher robin", "piglet", "roo", "eeyore"]
    print(reverse_list(lst))
    print()
    items = ["extract of malt", "haycorns", "honey", "thistle", "thistle"]
    print(remove_dupes(items))
    items = ["extract of malt", "haycorns", "honey", "thistle"]
    print(remove_dupes(items))
    print()
    nums = [3, 1, 2, 4]
    print(sort_by_parity(nums))
    nums = [0]
    print(sort_by_parity(nums))
    print()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(most_honey(height))
    height = [1, 1]
    print(most_honey(height))
    print()
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(merge_intervals(intervals))
    intervals = [[1, 4], [4, 5]]
    print(merge_intervals(intervals))
    print()

