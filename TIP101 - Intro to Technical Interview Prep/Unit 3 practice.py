# Session 1

# Problem 1: Calling Mississippi
def count_mississippi(limit):
  for num in range(1, limit):
    print( f"{num} mississippi")

# count_mississippi(6)

# Problem 2: Swap Ends
def swap_ends(my_str):
  start = my_str[0]
  end = my_str[-1]
  new_string = ""
  for i in my_str:
    if i == start:
      new_string += end
    elif i == end:
      new_string += start
    else:
      new_string += i
  return new_string

my_str = "quick"
print(swap_ends(my_str))
print()

# Problem 3: Is Pangram
def is_pangram(my_str):
  str = my_str.lower()
  new_set = ''
  for i in str:
    if i.isalpha():
      new_set += i
  my_str = set(new_set)
  return True if len(my_str) == 26 else False

my_str = "The quick brown fox jumps over the lazy dog"
print(is_pangram(my_str))

str2 = "The dog jumped"
print(is_pangram(str2))
print()

# Problem 4: Reverse String
def reverse_string(my_str):
  return my_str[::-1]

my_str = "liven"
print(reverse_string(my_str))

# Reverse list
def reverse_string2(my_lst):
  my_lst = my_lst.lower().split(" ")
  my_lst.reverse()
  return my_lst

my_lst = "The quick brown fox jumps over the lazy dog"
print(reverse_string2(my_lst))
print()

# Problem 5: First Unique
def first_unique_char(my_str):
  # use counter to get the dictionary count of items
  # loop through and check if the first occuring character occurs once
  # return the item
  
  from collections import Counter
  freq = Counter(my_str)
  for i, char in enumerate(my_str):
    if freq[char] == 1:
      return i
  return -1
    
# Example Usage:
my_str = "leetcode"
print(first_unique_char(my_str))

str2 = "loveleetcode"
print(first_unique_char(str2))

str3 = "aabb"
print(first_unique_char(str3))
print()

# Problem 6: Minimum Distance
def min_distance(words, word1, word2):
  # Understand
  # - If words list is empty return -1
  # - if one or both words not present in the list return -1
  # - duplicate occurence of word, use the minimum
  # - should word list be case sensitive, lower all words
  # Plan 
  # Brute force
  # - get word and location as index in a dictionary
  # - if word1 and word2 in words keep track of its index, check minimum
  ptr1 = ptr2 = min_dist = float('inf')
  for index, item in enumerate(words):
    if word1 == word2 or words == []:
      return -1    
    if item == word1:
      ptr1 = index
    elif item == word2:
      ptr2 = index
    min_dist = min(abs(ptr1 - ptr2), min_dist)
  return min_dist
  
# Example Usage:
words = ["the", "quick", "brown", "fox", "jumped", "the"]
dist1 = min_distance(words, "quick", "jumped")
dist2 = min_distance(words, "the", "jumped")
print(dist1)
print(dist2)

words2 = ["code", "path", "code", "contribute",  "practice"]
dist3 = min_distance(words2, "code", "practice")
print(dist3)
print()

# Problem Set Version 2
# Problem 1: Perfect Match
def match_made(dictionary):
  for key, value in dictionary.items():
    print( f"{key} and {value} are a perfect match.")

dict = {"Peanut butter":"Jelly", "Spongebob":"Patrick", "Ash":"Pikachu"}
match_made(dict)
print()

# Problem 2: Remove Char
def remove_char(s, n):
  new_string = ''
  for i, char in enumerate(s):
    if i != n:
      new_string += char
    else:
      pass
  return new_string
      
# Example Usage:
s = "typpo"
fixed_s = remove_char(s, 2)
print(fixed_s)
print()

# Problem 3: Count Vowels
def vowel_count(s):
  vowels = ['a', 'e', 'i', 'o', 'u']
  count = 0
  for item in s.lower():
    if item in vowels:
      count += 1
  return count

my_str = "hello world"
my_str2 = "aAaAaAaAAA"
my_str3 = "ths strng s mssng vwls"

count1 = vowel_count(my_str)
print(count1)
count2 = vowel_count(my_str2)
print(count2)
count3 = vowel_count(my_str3)
print(count3)
print()

# Problem 4: Reverse Sentence
def reverse_sentence(sentence):
  # Alternative
  # sentence_list = sentence.split(" ")
  # sentence_list.reverse()
  # return " ".join(sentence_list)
  return " ".join(sentence.split()[::-1])
  
# Example Input: 
sentence = "I solemnly swear I am up to no good"
print(reverse_sentence(sentence))
print()

# Problem 5: String Compression
def compress_string(my_str):
  new_str = ''
  from collections import Counter
  freq = Counter(my_str)
  for item in my_str:
    if item in freq and item not in new_str:
      new_str += item 
      new_str += str(freq[item])
  if len(new_str) > len(my_str):
    return my_str
  return new_str

# Example usage
my_str = "aaaaabbcccd"
compressed_Str = compress_string(my_str)
print(compressed_Str)

my_str2 = "abcde"
compressed_Str2 = compress_string(my_str2)
print(compressed_Str2)
print()

# Problem 6: Needle in a Haystack
def find_the_needle(haystack, needle):
  index = haystack.find(needle)
  if index == -1:
    return -1
  return index
  
# Example Usage:
haystack = "tobeornottobe"
needle = "be"
print(find_the_needle(haystack, needle))

haystack2 = "leetcode"
needle2 = "leeto"
print(find_the_needle(haystack2, needle2))
print()

# Problem Set Version 3
# Problem 2: Rotate Left
def rotate_left(s, n):
  end_string = ''
  new_string = ''
  for i, str in enumerate(s):
    if i < n:
      end_string += s[i]
      i += 1
    else:
      new_string += str
  return new_string + end_string
    
# Example Usage:
s = "rotation"
print(rotate_left(s, 2))
print()

# Problem 3: First Duplicate
def first_repeated_char(s):
  hash_set = set()
  for i in range(0, len(s)):
    if s[i] in hash_set:
      return i
    hash_set.add(s[i])
  return None

# Example Usage:
s = "hello world"
s2 = "aAbBCC"
s3 = "abcdefg"
print(first_repeated_char(s))
print(first_repeated_char(s2))
print(first_repeated_char(s3))
print()

# Problem 4: Find the Imposter
def find_difference(s1, s2):
  imposter = set(s2) - set(s1)
  for item in imposter:
    return item 
  
# Example Usage:
s1 = "abcd"
s2 = "baedc"
print(find_difference(s1, s2))
print()

# Problem 5: Longest Substring
# Write a function that takes in a string s and returns the length of the longest substring without repeating characters.

def length_of_longest_substring(s):
  hash_dict = {}
  max_val = 0
  for item in s:
    if item in hash_dict:
      hash_dict[item] += 1
    else:
      hash_dict[item] = 1
  for k, v in hash_dict.items():
    if len(hash_dict) > 1:
      max_val = max(hash_dict.values())
    return max_val
  return max_val

# Example Usage:
s = "abcdeefghhhhh"
count = length_of_longest_substring(s)
print(count) # Example Output: 5

s2 = "aaaaaaaaaaaaaaa"
count = length_of_longest_substring(s2)
print(count) # Example Output: 0
print()

# Problem 6: Roman to Integer
def roman_to_int(s):
  pass
  
# Example Usage:
s = "XL"
s2 = "LVIII"
s3 = "MCMXCIV"
print(roman_to_int(s))  # Example Output: 40
print(roman_to_int(s2)) # Example Output: 58
print(roman_to_int(s3)) # Example Output: 1994

# Problem Set Version 1
# Problem 1: Sum of Strings
def sum_of_number_strings(nums):
  # convert strings to int in a list
  # sum list
  lst = [int(i) for i in nums]
  return sum(lst)

nums = ["10", "20", "30"]
sum = sum_of_number_strings(nums)
print(sum)
print()

# Problem 2
def remove_duplicates(nums):
  # create a set of number
  # convert the set to list
  my_set = set(nums)
  return list(my_set)

nums = [1,1,1,2,3,4,4,5,6,6]
print(remove_duplicates(nums))
print()

'''
U - Understand
Share 2 questions you would ask to help understand the question:
(1) Are uppercase and lowercase letters treated differently during reversal?
(2) What should be considered as non-letter characters? Just punctuation and numbers, or also spaces and other symbols?

P - Plan
Write out in plain English what you want to do:
We want to reverse the order of only the letters in the string, keeping non-letter characters in their original positions. We'll use two pointers, one starting from the beginning and one from the end of the string, swapping letters as we move towards the middle.

Translate each sub-problem into pseudocode:
(1) Initialize two pointers and convert string to list:
    left = 0
    right = length of string - 1
    char_list = convert string to list of characters

(2) Swap letters while moving pointers:
    while left < right:
        if char at left is not a letter:
            increment left
        else if char at right is not a letter:
            decrement right
        else:
            swap chars at left and right
            increment left
            decrement right

(3) Convert list back to string and return:
    return joined char_list as string

I - Implement
Translate the pseudocode into Python and share your final answer:
'''

# Problem 3: Reverse Letters
def reverse_only_letters(s):
  new_lst = list(s)
  left = 0
  right = len(s) - 1
  while left < right:
    if not new_lst[left].isalpha():
      left += 1
    elif not new_lst[right].isalpha():
      right -= 1
    else:
      new_lst[left], new_lst[right] = new_lst[right], new_lst[left]
      left += 1
      right -= 1
  return "".join(new_lst)

# Test
s = "a-bC-dEf-ghIj"
reversed_s = reverse_only_letters(s)
print(reversed_s)

# Problem 4: Longest Uniform Substring
def longest_uniform_substring(s):
  from collections import Counter
  freq = Counter(s)
  max_val = -99999
  for v in freq.values():
    if v > max_val:
      max_val = v
  return max_val
  
# Example Usage:
s1 = "aabbbbCdAA"
l1 = longest_uniform_substring(s1)
print(l1)

s2 = "abcdef"
l2 = longest_uniform_substring(s2)
print(l2)
print()

# Problem 5: Teemo's Attack
def find_poisoned_duration(time_series, duration):
  total_duration = 0
  for i in range(len(time_series)-1):
      # Calculate the actual poisoning time between two attacks
      actual_duration = min(time_series[i+1] - time_series[i] - 1, duration)

      total_duration += actual_duration
  # Add the duration of the last attack
  total_duration += duration
  return total_duration

# Example usage
time_series = [1, 4, 9]
damage = find_poisoned_duration(time_series, 3)
print(damage)  # Output: 8
print()

# Problem 6: Sum Unique Elements
def sum_of_unique_elements(lst1, lst2):
  freq_dict = {}
  for val in lst1:
    if val in freq_dict:
      freq_dict[val] += 1
    else:
      freq_dict[val] = 1

  lst2_set = set(lst2)
  unique_sum = 0
  for element, frequency in freq_dict.items():
    if frequency == 1 and element not in lst2_set:
      unique_sum += element
  return unique_sum

# Example Usage:
lstA = [1, 2 ,3, 4] 
lstB = [3, 4, 5, 6]
lstC = [7, 7, 7, 7]
sum1 = sum_of_unique_elements(lstA, lstB)
print(sum1)

sum2 = sum_of_unique_elements(lstC, lstB)
print(sum2)
print()


# greetings = "Hello World!"
# greetings[7] = 'w'
# print(greetings)
# print()

word = "encourage"
char_count = {}
for char in word:
  if char not in char_count:
    char_count[char] = 1
  else:
    char_count[char] += 1
char_count['e'] += 2
print(char_count['e'])
print()

date = "24-06-2024"
month = date[3:5]
print(month)