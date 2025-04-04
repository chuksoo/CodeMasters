# Session 1: Stacks, Queues, and Two Pointer
# Standard Problem Set Version 1
'''Problem 1: Post Format Validator
You are managing a social media platform and need to ensure that posts are properly formatted. 
Each post must have balanced and correctly nested tags, such as () for mentions, [] for hashtags, and {} for links. 
You are given a string representing a post's content, and your task is to determine if the tags in the post are correctly formatted.

A post is considered valid if:

 - Every opening tag has a corresponding closing tag of the same type.
 - Tags are closed in the correct order.'''
def is_valid_post_format(posts):
    stack = []
    for tag in posts:
        if tag == '(' or tag == '{' or tag == '[':
            stack.append(tag)
        if len(stack) != 0:
            if tag == ')' and stack[-1] == '(':
                stack.pop()
            elif tag == '}'  and stack[-1] == '{':
                stack.pop()
            elif tag == ']' and stack[-1] == '[':
                stack.pop()

    if len(stack) == 0:
        return True
    return False
    
'''Problem 2: Reverse User Comments Queue
On your platform, comments on posts are displayed in the order they are received. However, for a special feature, you need to reverse the order of comments before displaying them. 
Given a queue of comments represented as a list of strings, reverse the order using a stack.
'''
def reverse_comments_queue(comments):
    comment_stack = []
    reversed_lst = []
    for comment in comments:
        comment_stack.append(comment)

    while comment_stack:
        reversed_lst.append(comment_stack.pop())
    return reversed_lst

'''Problem 3: Check Symmetry in Post Titles
As part of a new feature on your social media platform, you want to highlight post titles that are symmetrical, 
meaning they read the same forwards and backwards when ignoring spaces, punctuation, and case. Given a post title as a string, 
use a new algorithmic technique the two-pointer method to determine if the title is symmetrical.'''
def is_symmetrical_title(title):
    title = ''.join(title.lower().split())
    left, right = 0, len(title) - 1
    while left < right:
        if title[left] != title[right]:
            return False
        else:
            left += 1
            right -= 1
    return True

'''Problem 4: Engagement Boost
You track your daily engagement rates as a list of integers, sorted in non-decreasing order. To analyze the impact of certain strategies, 
you decide to square each engagement rate and then sort the results in non-decreasing order.

Given an integer array engagements sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Your Task:

Read through the existing solution and add comments so that everyone in your pod understands how it works.
Modify the solution below to use the two-pointer technique.'''
# def engagement_boost(engagements):
#     squared_engagements = []
    
#     # get squared of each engagement and store in a list
#     for i in range(len(engagements)):
#         squared_engagement = engagements[i] * engagements[i]
#         squared_engagements.append((squared_engagement, i))
    
#     # sort the list in reverse
#     squared_engagements.sort(reverse=True)
  
#     result = [0] * len(engagements)
#     position = len(engagements) - 1
    
#     # 
#     for square, original_index in squared_engagements:
#         result[position] = square
#         position -= 1
    
#     return result

def engagement_boost(engagements):
    squared_engagement = [0] * len(engagements)
    left, right = 0, len(engagements) - 1
    position = len(engagements) - 1

    while left < right:
        left_square, right_square = engagements[left]**2, engagements[right]**2
        if left_square > right_square:
            squared_engagement[position] = left_square
            left += 1
        else:
            squared_engagement[position] = right_square
            right -= 1
        position -= 1
    return squared_engagement

'''Problem 5: Content Cleaner
You want to make sure your posts are clean and professional. Given a string post of lowercase and uppercase English letters, 
you want to remove any pairs of adjacent characters where one is the lowercase version of a letter and the other is the uppercase version 
of the same letter. Keep removing such pairs until the post is clean.

A clean post does not have two adjacent characters post[i] and post[i + 1] where:

post[i] is a lowercase letter and post[i + 1] is the same letter in uppercase or vice-versa.
Return the clean post.

Note that an empty string is also considered clean.'''
def clean_post(post):
    if post == '':
        return post
    
    clean_stack = []
    for char in post:
        if clean_stack and (char.lower() == clean_stack[-1].lower()) and (char.isupper() != clean_stack[-1].isupper()):
            clean_stack.pop()
        else:
            clean_stack.append(char)

    return ''.join(clean_stack)
        
'''Problem 6: Post Editor
You want to add a creative twist to your posts by reversing the order of characters in each word within your post while still 
preserving whitespace and the initial word order. Given a string post, use a queue to reverse the order of characters in each word within the sentence.
'''
from collections import deque, Counter

def edit_post(post):
    result = ""
    queue = deque() 

    for char in post:
        if char != ' ':
            queue.append(char)
        else:
            # process word when we hit a space
            current_word = ""
            while queue:
                current_word = queue.popleft() + current_word
            result += current_word + " "

    # process the last word 
    if queue:
        current_word = ""
        while queue:
            current_word = queue.popleft() + current_word
        result += current_word
    return result

'''Problem 7: Post Compare
You often draft your posts and edit them before publishing. Given two draft strings draft1 and draft2, return true 
if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will remain empty.'''
def post_compare(draft1, draft2):
    def process_draft(draft):
        draft_stack = []
        for char in draft:
            if char != "#":
                draft_stack.append(char)
            else:
                draft_stack.pop()
        return draft_stack
    return process_draft(draft1) == process_draft(draft2)

# Standard Problem Set Version 2
'''Problem 1: Time Needed to Stream Movies
There are 'n' users in a queue waiting to stream their favorite movies, where the 0th user is at the front of the queue and the (n - 1)th user is at the back of the queue.

You are given a 0-indexed integer array movies of length n where the number of movies that the ith user would like to stream is movies[i].

Each user takes exactly 1 second to stream a movie. A user can only stream 1 movie at a time and has to go back to the end of the queue (which happens instantaneously) 
in order to stream more movies. If a user does not have any movies left to stream, they will leave the queue.

Return the time taken for the user at position k (0-indexed) to finish streaming all their movies.'''

def time_required_to_stream(movies, k):
    current_time = 0
    queue = deque()
    for i in range(len(movies)):
        if movies[i] > 0:
            queue.append((i, movies[i]))
    
    while queue:
        user_index, movies_left = queue.popleft()
        current_time += 1
        movies_left -= 1

        if user_index == k and movies_left == 0:
            return current_time
        
        if movies_left > 0:
            queue.append((user_index, movies_left))
    return -1
          
'''Leetcode: Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.'''
def topKFrequent(nums, k):
    import heapq
    from collections import Counter

    heap = []
    num_freq = Counter(nums)

    for num, freq in num_freq.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)

    result = [num for freq, num in heap]
    return result

'''Problem 2: Reverse Watchlist
You are given a list watchlist representing a list of shows sorted by popularity for a particular user. 
The user wants to discover new shows they haven't heard of before by reversing the list to show the least popular shows first.

Using the two-pointer approach, implement a function reverse_watchlist() that reverses the order of the watchlist in-place. 
This means that the first show in the given list should become the last, the second show should become the second to last, and so on. Return the reversed list.

Do not use list slicing (e.g., watchlist[::-1]) to achieve this.'''
def reverse_watchlist(watchlist):
    left, right = 0, len(watchlist) - 1
    while left < right:
        watchlist[left], watchlist[right] = watchlist[right], watchlist[left]
        left += 1
        right -= 1
    return watchlist

'''Problem 3: Remove All Adjacent Duplicate Shows
You are given a string schedule representing the lineup of shows on a streaming platform, where each character in the string represents a different show. 
A duplicate removal consists of choosing two adjacent and equal shows and removing them from the schedule.

We repeatedly make duplicate removals on schedule until no further removals can be made.

Return the final schedule after all such duplicate removals have been made. The answer is guaranteed to be unique.'''
def remove_duplicate_shows(schedule):
    stack = []
    for char in schedule:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)

'''Problem 4: Minimum Average of Smallest and Largest View Counts
You manage a collection of view counts for different shows on a streaming platform. You are given an array view_counts of n integers, where n is even.

You repeat the following procedure n / 2 times:

Remove the show with the smallest view count, min_view_count, and the show with the largest view count, max_view_count, from view_counts.
Add (min_view_count + max_view_count) / 2 to the list of average view counts average_views.
Return the minimum element in average_views.'''
def minimum_average_view_count(view_counts):
    import heapq

    min_heap = [] # heap
    max_heap = []
    average_views = []
    procedure_count = len(view_counts) // 2

    for num in view_counts:
        heapq.heappush(min_heap, num)
        heapq.heappush(max_heap, -num)

    for i in range(procedure_count):
        min_view_count = heapq.heappop(min_heap)
        max_view_count = -heapq.heappop(max_heap)
        average_val = (min_view_count + max_view_count) / 2
        heapq.heappush(average_views, average_val)
    return heapq.heappop(average_views)

'''Problem 5: Minimum Remaining Watchlist After Removing Movies
You have a watchlist consisting only of uppercase English letters representing movies. Each movie is represented by a unique letter.

You can apply some operations to this watchlist where, in one operation, you can remove any occurrence of one of the movie pairs "AB" or "CD" from the watchlist.

Return the minimum possible length of the modified watchlist that you can obtain.

Note that the watchlist concatenates after removing the movie pair and could produce new "AB" or "CD" pairs.'''
def min_remaining_watchlist(watchlist):
    modified_watch_list = []
    for char in watchlist:
        if modified_watch_list and modified_watch_list[-1] == 'A' and char == 'B':
            modified_watch_list.pop()
        elif modified_watch_list and modified_watch_list[-1] == 'C' and char == 'D':
            modified_watch_list.pop()
        else:
            modified_watch_list.append(char)
    return len(modified_watch_list)
    
'''Problem 6: Apply Operations to Show Ratings
You are given a 0-indexed array ratings of size n consisting of non-negative integers. Each integer represents the rating of a show in a streaming service.

You need to apply n - 1 operations to this array where, in the ith operation (0-indexed), you will apply the following on the ith element of ratings:

If ratings[i] == ratings[i + 1], then multiply ratings[i] by 2 and set ratings[i + 1] to 0. Otherwise, you skip this operation.
After performing all the operations, shift all the 0's to the end of the array.

For example, the array [1,0,2,0,0,1] after shifting all its 0's to the end, is [1,2,1,0,0,0].

Return the resulting array of ratings.'''
def apply_rating_operations(ratings):
    for i in range(len(ratings) - 1):
        if ratings[i] == ratings[i + 1]:
            ratings[i] = ratings[i] * 2
            ratings[i + 1] = 0
    return zero_shift(ratings)

def zero_shift(nums):
    left, right = 0 , len(nums) - 1
    while left < right:
        if nums[left] != 0 and nums[right] == 0:
            left += 1
            right -= 1
        elif nums[left] == 0 and nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        else:
            right -= 1
    return nums

'''Problem 7: Lexicographically Smallest Watchlist
You are managing a watchlist for a streaming service, represented by a string watchlist consisting of lowercase English letters, where each letter represents a different show.
You are allowed to perform operations on this watchlist. In one operation, you can replace a show in watchlist with another show (i.e., another lowercase English letter).
Your task is to make the watchlist a palindrome with the minimum number of operations possible. If there are multiple palindromes that can be made using the minimum number of operations, 
make the lexicographically smallest one.

A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, 
string a has a letter that appears earlier in the alphabet than the corresponding letter in b.

Return the resulting watchlist string.
Implement the following pseudocode:'''
def make_smallest_watchlist(watchlist):
    watchlist = list(watchlist)
    left, right = 0, len(watchlist) - 1
    while left < right:
        if watchlist[left] != watchlist[right] and watchlist[left] > watchlist[right]:
            watchlist[left] = watchlist[right]
        elif watchlist[left] != watchlist[right] and watchlist[left] < watchlist[right]:
            watchlist[right] = watchlist[left]
        left += 1
        right -= 1
    return ''.join(watchlist)

# Advanced Problem Set Version 1
'''Problem 1: Arrange Guest Arrival Order
You are organizing a prestigious event, and you must arrange the order in which guests arrive based on their status. 
The sequence is dictated by a 0-indexed string arrival_pattern of length n, consisting of the characters 'I' meaning 
the next guest should have a higher status than the previous one, and 'D' meaning the next guest should have a lower status than the previous one.

You need to create a 0-indexed string guest_order of length n + 1 that satisfies the following conditions:

guest_order consists of the digits '1' to '9', where each digit represents the guest's status and is used at most once.
If arrival_pattern[i] == 'I', then guest_order[i] < guest_order[i + 1].
If arrival_pattern[i] == 'D', then guest_order[i] > guest_order[i + 1].
Return the lexicographically smallest possible string guest_order that meets the conditions.'''
def arrange_guest_arrival_order(arrival_pattern):
    n = len(arrival_pattern)
    pattern = [] 
    result_lst = []

    for i in range(len(arrival_pattern) + 1):
        pattern.append(i+1)
        if i == n or arrival_pattern[i] == 'I':
            while pattern:
                top_element = pattern.pop()
                result_lst.append(str(top_element))
    return ''.join(result_lst)
    



    

# Session 2: Stacks, Queues, and Two Pointer
# Standard Problem Set Version 1

# import math
# from collections import deque

# '''Problem 1: Manage Performance Stage Changes
# At a cultural festival, multiple performances are scheduled on a single stage. However, due to last-minute changes, 
# some performances need to be rescheduled or canceled. The festival organizers use a stack to manage these changes efficiently.

# You are given a list changes of strings where each string represents a change action. The actions can be:

# "Schedule X": Schedule a performance with ID X on the stage.
# "Cancel": Cancel the most recently scheduled performance that hasn't been canceled yet.
# "Reschedule": Reschedule the most recently canceled performance to be the next on stage.
# Return a list of performance IDs that remain scheduled on the stage after all changes have been applied.'''
# def manage_stage_changes(changes):
#     stack = []
#     cancelled_stack = []
#     for schedule in changes:
#         if 'Schedule' in schedule:
#             change, id = schedule.split()
#             stack.append(id)
#         elif schedule == 'Cancel':
#             if stack:
#                 cancelled_stack.append(stack.pop())
#         elif schedule == 'Reschedule':
#             if cancelled_stack:
#                 stack.append(cancelled_stack.pop())
#     return stack

# '''Problem 2: Queue of Performance Requests
# You are organizing a festival and want to manage the queue of requests to perform. Each request has a priority. 
# Use a queue to process the performance requests in the order they arrive but ensure that requests with higher priorities are processed before those with lower priorities. 
# Return the order in which performances are processed.
# '''
# import heapq
# def process_performance_requests(requests):
#     priority_queue = []

#     for request_number, (priority, performance) in enumerate(requests):
#         heapq.heappush(priority_queue, (-priority, request_number, performance))

#     order = []
#     while priority_queue:
#         priority, request_number, performance = heapq.heappop(priority_queue)
#         print(f'Processing {performance} with priority {-priority}')
#         order.append(performance)

#     return order

# '''Problem 3: Collecting Points at Festival Booths
# At the festival, there are various booths where visitors can collect points. Each booth has a specific number of points available. 
# Use a stack to simulate the process of collecting points and return the total points collected after visiting all booths.
# '''
# def collect_festival_points(points):
#     collecting_points = []
#     for point in points:
#         collecting_points.append(point)
#     return sum(collecting_points)

# '''Problem 4: Festival Booth Navigation
# At the cultural festival, you are managing a treasure hunt where participants need to visit booths in a specific order. 
# The order in which they should visit the booths is defined by a series of clues. However, some clues lead to dead ends, 
# and participants must backtrack to previous booths to continue their journey.

# You are given a list of clues, where each clue is either a booth number (an integer) to visit or the word "back" indicating that 
# the participant should backtrack to the previous booth.

# Write a function to simulate the participant's journey and return the final sequence of booths visited, in the order they were visited.'''

# def booth_navigation(clues):
#     clues_stack = []
#     for item in clues:
#         if item != 'back':
#             clues_stack.append(item)
#         else:
#             if clues_stack:
#                 clues_stack.pop()
#             else:
#                 pass
#     return clues_stack

# '''Problem 5: Merge Performance Schedules
# You are organizing a cultural festival and have two performance schedules, schedule1 and schedule2, 
# each represented by a string where each character corresponds to a performance slot. 
# Merge the schedules by adding performances in alternating order, starting with schedule1. 
# If one schedule is longer than the other, append the additional performances onto the end of the merged schedule.

# Return the merged performance schedule.'''

# def merge_schedules(schedule1, schedule2):
#     schedule1, schedule2 = list(schedule1), list(schedule2)
#     result = []
#     ptr_one = ptr_two = 0
#     while ptr_one < len(schedule1) and ptr_two < len(schedule2):
#         result.append(schedule1[ptr_one])
#         result.append(schedule2[ptr_two])
#         ptr_one += 1
#         ptr_two += 1
#     if len(schedule1) > len(schedule2):
#         result += schedule1[ptr_one:]
#     else:
#         result += schedule2[ptr_two:]
#     return ''.join(result)




if __name__ == "__main__":
    print("-------- # Session 1: Stacks, Queues, and Two Pointer -------- ")
    print("------ # Standard Problem Set Version 1 ------ ")
    print(is_valid_post_format("()"))
    print(is_valid_post_format("()[]{}")) 
    print(is_valid_post_format("(]"))
    print()
    print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))
    print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))
    print()
    print(is_symmetrical_title("A Santa at NASA"))
    print(is_symmetrical_title("Social Media")) 
    print()
    print(engagement_boost([-4, -1, 0, 3, 10]))
    print(engagement_boost([-7, -3, 2, 3, 11]))
    print()
    print(clean_post("poOost")) 
    print(clean_post("abBAcC")) 
    print(clean_post("s")) 
    print()
    print(edit_post("Boost your engagement with these tips")) 
    print(edit_post("Check out my latest vlog")) 
    print()
    print(post_compare("ab#c", "ad#c"))
    print(post_compare("ab##", "c#d#")) 
    print(post_compare("a#c", "b")) 
    print()
    print("------ # Standard Problem Set Version 1 ------ ")
    print(time_required_to_stream([2, 3, 2], 2)) 
    print(time_required_to_stream([5, 1, 1, 1], 0)) 
    print()
    print(topKFrequent([1,1,1,2,2,3], 2)) # Output: [1,2]
    print(topKFrequent([1], 1)) # Output: [1]
    print() 
    watchlist = ["Breaking Bad", "Stranger Things", "The Crown", "The Witcher"]
    print(reverse_watchlist(watchlist))  
    print()
    print(remove_duplicate_shows("abbaca")) 
    print(remove_duplicate_shows("azxxzy")) 
    print()
    print(minimum_average_view_count([7, 8, 3, 4, 15, 13, 4, 1])) 
    print(minimum_average_view_count([1, 9, 8, 3, 10, 5])) 
    print(minimum_average_view_count([1, 2, 3, 7, 8, 9])) 
    print()
    print(min_remaining_watchlist("ABFCACDB")) 
    print(min_remaining_watchlist("ACBBD")) 
    print()
    print(apply_rating_operations([1, 2, 2, 1, 1, 0])) 
    print(apply_rating_operations([0, 1])) 
    print()
    print(make_smallest_watchlist("egcfe")) 
    print(make_smallest_watchlist("abcd")) 
    print(make_smallest_watchlist("seven")) 
    print()
    print("------ # Advanced Problem Set Version 1 ------ ")
    print(arrange_guest_arrival_order("IIIDIDDD"))  
    print(arrange_guest_arrival_order("DDD"))  
    



    # print("-------- # Session 2: Stacks, Queues, and Two Pointer -------- ")
    # print("------ # Standard Problem Set Version 1 ------ ")
    # print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))  
    # print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"])) 
    # print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"])) 
    # print()
    # print(process_performance_requests([(3, 'Dance'), (5, 'Music'), (1, 'Drama')]))
    # print(process_performance_requests([(2, 'Poetry'), (1, 'Magic Show'), (4, 'Concert'), (3, 'Stand-up Comedy')]))
    # print(process_performance_requests([(1, 'Art Exhibition'), (3, 'Film Screening'), (2, 'Workshop'), (5, 'Keynote Speech'), (4, 'Panel Discussion')]))
    # print()
    # print(collect_festival_points([5, 8, 3, 10])) 
    # print(collect_festival_points([2, 7, 4, 6])) 
    # print(collect_festival_points([1, 5, 9, 2, 8])) 
    # print()
    # clues = [1, 2, "back", 3, 4]
    # print(booth_navigation(clues)) 
    # clues = [5, 3, 2, "back", "back", 7]
    # print(booth_navigation(clues)) 
    # clues = [1, "back", 2, "back", "back", 3]
    # print(booth_navigation(clues)) 
    # print()
    # print(merge_schedules("abc", "pqr")) 
    # print(merge_schedules("ab", "pqrs")) 
    # print(merge_schedules("abcd", "pq")) 
    # print()
