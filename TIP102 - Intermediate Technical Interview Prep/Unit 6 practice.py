###################################################
# Session 1: Linked Lists II
###################################################
# Standard Problem Set Version 1
# -------------------------------------------------
'''Problem 1: Building a Playlist
The assignment statement to the top_hits_2010s variable below creates the linked list Uptown Funk -> Party Rock Anthem -> Bad Romance. 
Break apart the assignment statement into multiple lines with one call to the Node constructor per line to recreate the list.'''

from collections import defaultdict

class SongNode:
    def __init__(self, song, next=None):
        self.song = song
        self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print(current.song, end=" -> " if current.next else "")
        current = current.next
    print()

'''Problem 2: Top Artists
Given the head of a linked list playlist, return a dictionary that maps each artist in the list to its frequency.

Evaluate the time complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.'''
class SongNode_artist:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next

def get_artist_frequency(playlist):
    # create dict using default dict
    artist_count = defaultdict(int)
    current = playlist

    while current:
        # get count of current.artist in playlist:
        artist_count[current.artist] += 1
        current = current.next
    return artist_count

'''Problem 3: Glitching Out
The following code attempts to remove the first node with a given song from a singly linked list with head playlist_head but it contains a bug!

Step 1: Copy this code into Replit.

Step 2: Create your own test cases to run the code against, and use print statements and the stack trace to identify and fix the bug so that the function correctly removes a node by value from the list.

Step 3: Evaluate the time and space complexity of the fixed solution. Define your variables and provide a rationale for why you believe the solution has the stated time and space complexity.'''

# For testing
def print_linked_list_tuple(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()

# Function with a bug!
def remove_song(playlist_head, song):
    if not playlist_head:
        return None
    if playlist_head.song == song:
        return playlist_head.next

    current = playlist_head
    while current.next:
        if current.next.song == song:
            current.next = current.next.next  
            return playlist_head 
        current = current.next

    return playlist_head

'''Problem 4: On Repeat
A variation of the two-pointer technique introduced in previous units is to have a slow and a fast pointer that increment at different rates.

We would like to check whether our playlist loops or not. Given the head of a linked list playlist_head, return True if the playlist has a cycle in it and False otherwise. 
A linked list has a cycle if at some point in the list, the node’s next pointer points back to a previous node in the list.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.'''
def on_repeat(playlist_head):
    slow = fast = playlist_head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

'''Problem 5: Looped
Given the head of a linked list playlist_head that may contain a cycle, use the fast and slow pointer method to return the length of the cycle. If the list does not contain a cycle, return 0.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.'''
def loop_length(playlist_head):
    count = 0
    slow = fast = playlist_head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        count += 1
        if slow == fast:
            return count 
    return 0

'''Problem 6: Volume Control
You are working as an engineer normalizing volume levels on songs. Given the head of a singly linked list with integer values song_audio representing volume levels at different points in a song, 
return the number of critical points. A critical point is a local minima or maxima.

The head and tail nodes are not considered critical points.
A node is a local minima if both the next and previous elements are greater than the current element
A node is a local maxima if both the next and previous elements are less than the current element
Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.'''
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def count_critical_points(song_audio):
    counter = 0
    current = song_audio.next
    previous = song_audio
    
    while current.next:
        if current.value < previous.value and current.value < current.next.value:
            counter += 1
        if current.value > previous.value and current.value > current.next.value:
            counter += 1
        previous = current
        current = current.next
    return counter

# -------------------------------------------------
# Standard Problem Set Version 2
# -------------------------------------------------
'''Problem 1: Why is it Always You Three
In a single assignment statement, create the linked list Harry -> Ron -> Hermione.'''
# For testing
def print_linked_list_value(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

head = Node("Harry", Node("Ron", Node("Hermione")))

'''Problem 2: 200 Points for Gryffindor
It's almost the end of the year, and Gryffindor students want to see if they have any competition for first place. Given the head of a linked list house_points and the Gryffindor's score, 
return the frequency of score in the list.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.'''
class Node_score:
    def __init__(self, house, score, next=None):
        self.house = house
        self.value = score
        self.next = next

# For testing
def print_linked_list_score(head):
    current = head
    while current:
        print((current.house, current.value), end=" -> " if current.next else "\n")
        current = current.next

def count_element(house_points, score):
    if house_points is None:
        return 0
    
    count = 0
    current = house_points
    while current is not None:
        if current.value == score:
            count += 1
        current = current.next
    return count

'''Problem 3: Target Practice
You are practicing the accuracy of your spellwork by trying to extract the middle-most ingredient in a line of potions. Given the head of a linked list, potions, use a variation of the two-pointer 
technique to return the middle potion. If there are two middle nodes, return the potion of the second middle node.

The two-pointer variation you should use is called the 'slow and fast pointer' or 'tortoise and the hare' technique. In this variation, a slow and a fast pointer are incremented at different rates.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.'''
class Node_potion:
    def __init__(self, potion, next=None):
        self.potion = potion
        self.next = next

# For testing
def print_linked_list_potion(head):
    current = head
    while current:
        print(current.potion, end=" -> " if current.next else "\n")
        current = current.next

def find_middle_potion(potions):
    if head is None:
        return potions
    
    slow = fast = potions
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow.potion

'''Problem 4: Turn Back Time
A spell gone wrong has reversed time! Write a function reverse() that accepts the head of a singly linked list events and restores order by reversing the order of elements. Return the head of the reversed list.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.'''
def reverse(events):
    if events is None:
        return events
    
    prev = None
    current = events 
    while current is not None:
        next_temp = current.next # store current's next node
        current.next = prev  # swap nodes
        prev = current 
        current = next_temp
    return prev 

'''Problem 5: Mirror, Mirror
You think another bit of wonky spell casting may have left your enchanted mirror broken. Write a function is_mirrored() to test if your mirror successfully reflects objects back. 
The function accepts the head of a linked list and should return True if the values of the linked list read the same backwards and forwards, and False otherwise.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.'''
def is_mirrored(head):
    if head is None:
        return True
    
    # find the middle node
    slow = fast = head 
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    
    # if list has an even number, get the second middle node
    if fast is not None:
        slow = slow.next

    # reverse second half of list
    second_half = reverse(slow)

    # compare first and second half
    ptr_one = head
    ptr_two = second_half
    while ptr_two is not None:
        if ptr_one.value != ptr_two.value:
            return False 
        ptr_one = ptr_one.next
        ptr_two = ptr_two.next
    return True


'''Problem 6: Magic Loop
In a nearby enchanted forest, magical paths sometimes loop back on themselves, creating never-ending cycles. Write a function loop_start() to help you keep your way. 
The function accepts the head of a linked list path_start and returns the value of the node where the cycle starts. If the path has no cycle, return None.

A linked list has a cycle if, at some point in the list, the node’s next pointer points back to a previous node in the list.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.'''
def loop_start(path_start):  
    slow = fast = path_start
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    if fast is None or fast.next is None:
        return None

    fast = path_start
    while fast != slow:
        slow = slow.next
        fast = fast.next
    return slow.value

# -------------------------------------------------
# Advanced Problem Set Version 1
# -------------------------------------------------
'''Problem 1: Selective DNA Deletion
As a biologist, you are working on editing a long strand of DNA represented as a linked list of nucleotides. Each nucleotide in the sequence is represented as a node in the linked list, 
where each node contains a character ('A', 'T', 'C', 'G') representing the nucleotide.

Given the head of the linked list dna_strand and two integers m and n, write a function edit_dna_sequence() that simulates the selective deletion of nucleotides in a DNA sequence. 
You will: - Start at the beginning of the DNA strand. - Retain the first m nucleotides from the current position. - Remove the next n nucleotides from the sequence. - Repeat the process until the end of the DNA strand is reached.

Return the head of the modified DNA sequence after removing the mentioned nucleotides.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.'''
def edit_dna_sequence(dna_strand, m, n):
    current = dna_strand
    while current is not None:
        for i in range(1, m):
            if current is None:
                break 
            current = current.next

        if current is None:
            break 

        temp = current.next
        for j in range(n):
            if temp is None:
                break
            temp = temp.next 

        current.next = temp
        current = temp
    return dna_strand

'''Problem 2: Protein Folding Loop Detection
As a biochemist, you're studying the folding patterns of proteins, which are represented as a sequence of amino acids linked together. 
These proteins sometimes fold back on themselves, creating loops that can impact their function.

Given the head of a linked list protein where each node in the linked list represents an amino acid in the protein, return an array with the values of any cycle in the list. 
A linked list has a cycle if at some point in the list, the node’s next pointer points back to a previous node in the list.

The values may be returned in any order.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.'''
def cycle_length(protein):
    if protein is None:
        return 
    
    slow = fast = protein
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break 

    fast = protein
    while fast != slow:
        fast = fast.next
        slow = slow.next
        
    lst = []    
    while slow:
        if slow.value not in lst:
            lst.append(slow.value)
        else:
            break
        slow = slow.next 
    return lst

'''Problem 3: Segmenting Protein Chains for Analysis
As a biochemist, you are analyzing a long protein chain represented by a singly linked list, where each node is an amino acid. 
For a specific experiment, you need to split this protein chain into k consecutive segments for separate analysis. Each segment should be as equal in length as possible, 
with no two segments differing in size by more than one amino acid.

The segments should appear in the same order as the original protein chain, and segments earlier in the list should have a size greater than or equal to those occurring later. 
If the protein chain cannot be evenly divided, some segments may be an empty list.

Write a function split_protein_chain() that takes the head of the linked list protein and an integer k, and returns an array of k segments.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.'''

def split_protein_chain(protein, k):
    # Step 1: Count the total number of nodes in the protein linked list.
    total_nodes = 0
    current = protein
    while current:
        total_nodes += 1
        current = current.next

    # Step 2: Determine the size for each segment.
    # base_size is the minimum number of nodes per segment.
    base_size = total_nodes // k
    # extra is how many segments need one extra node.
    extra = total_nodes % k

    # Prepare list to hold the heads of the segments.
    segments = [None] * k

    # Reset current pointer to the head.
    current = protein

    # Step 3: For each segment i, decide how many nodes it should have and split.
    for i in range(k):
        if current:
            # This segment will have (base_size + 1) nodes if i < extra, else base_size nodes.
            seg_size = base_size + 1 if i < extra else base_size

            # The current node is the head of this segment.
            segments[i] = current

            # Advance to the last node of this segment.
            # We need to move (seg_size - 1) steps because current is already at the head.
            for j in range(seg_size - 1):
                if current:
                    current = current.next

            # Break the link if there are still nodes left.
            if current:
                temp = current.next  # Save the beginning of the next segment.
                current.next = None  # Break the current segment.
                current = temp
        else:
            # If there are no more nodes, the remaining segments are None (empty).
            segments[i] = None

    return segments

'''Problem 4: Maximum Protein Pair Stability
You are analyzing the stability of protein chains, which are represented by a singly linked list where each node contains an integer stability value. 
The chain has an even number of nodes, and for each node i (0-indexed), its "twin" is defined as node (n-1-i), where n is the length of the linked list.

Write a function max_protein_pair_stability() that accepts the head of a linked list, and determines the maximum "twin stability sum," which is the sum of the stability values of a node and its twin.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.'''
def max_protein_pair_stability(head):
    # find the middle of the linked list
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # reverse the second half
    second_half_head = reverse_linked_list(slow)

    # compute the maximum sum
    max_sum = 0
    ptr_one = head
    ptr_two = second_half_head
    while ptr_two:
        current_sum = ptr_one.value + ptr_two.value
        if current_sum > max_sum:
            max_sum = current_sum
        ptr_one = ptr_one.next
        ptr_two = ptr_two.next

    # return maximum sum
    return max_sum

def reverse_linked_list(head):
    if head is None:
        return head
    
    current = head
    prev = None
    while current is not None:
        next_temp = current.next # store current's next node
        current.next = prev      # reverse the pointer
        prev = current           # move previous forward
        current = next_temp      # move current forward
    return prev

'''Problem 5: Grouping Experiments
You have a list of experiment results for two types of experiments conducted in alternating order represented by a singly linked list. 
Each node in the list corresponds to an experiment result, and the position of the result in the 1-indexed sequence determines whether it is odd or even.

Given the head of the linked list, exp_results, reorganize the experiment results so that all results in odd positions are grouped together first, followed by all results in even positions. 
The relative order of the results within the odd group and the even group must remain the same as the original sequence. The first result in the list is considered to be odd, the second result is even, and so on. Return the head of the reorganized list.

Your solution must have O(1) space complexity and O(n) time complexity.'''
def odd_even_experiments(exp_results):
    if exp_results is None or exp_results.next is None:
        return exp_results
    
    odd = exp_results
    even = exp_results.next
    even_head = even

    while even is not None and even.next is not None:
        odd.next = even.next
        odd = odd.next

        even.next = odd.next
        even = even.next

    odd.next = even_head
    return exp_results

# -------------------------------------------------
# Advanced Problem Set Version 2
# -------------------------------------------------
'''Problem 1: Linked List Game
As the judge of the game show, you are given the head of a linked list of even length containing integers.

Each odd-indexed node contains an odd integer and each even-indexed node contains an even integer.

We call each even-indexed node and its next node a pair, e.g., the nodes with indices 0 and 1 are a pair, the nodes with indices 2 and 3 are a pair, and so on.

For every pair, we compare the values of the nodes in the pair:

If the odd-indexed node is higher, the "Odd" team gets a point.
If the even-indexed node is higher, the "Even" team gets a point.
Write a function game_result() that returns the name of the team with the higher points, if the points are equal, return "Tie".

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.'''
def game_result(head):

    odd_point = even_point = 0
    current = head
    while current is not None and current.next is not None:
        even_value = current.value
        odd_value = current.next.value

        if even_value < odd_value:
            odd_point += 1
        elif even_value > odd_value:
            even_point += 1

        current = current.next.next

    if odd_point > even_point:
        return "Odd"
    elif odd_point < even_point:
        return "Even"
    else:
        return "Tie"

'''Problem 2: Cycle Start
On your marks, get set, go! Contestants in the game show are racing along a path that contains a loop, but there's a hidden mini challenge: they aren't told where along the path the loop begins. 
Given the head of a linked list, path_start where each node represents a point in the path, return the value of the node at the start of the loop. If no loop exists in the path, return None.

A linked list has a cycle or loop if at some point in the list, the node’s next pointer points back to a previous node in the list.'''
def cycle_start(path_start):
    if path_start is None or path_start.next is None:
        return path_start
    
    slow = fast = path_start
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    fast = path_start
    while fast != slow:
        slow = slow.next
        fast = fast.next
    return slow.value

'''Problem 3: Fastest Wins!
Contestants, today's challenge is to sort a linked list of items the fastest! The catch - you have to follow a certain technique or you're disqualified from the round. 
You’ll start with an unsorted lineup, and with each step, you’ll move one item at a time into its proper position until the entire lineup is perfectly ordered.

Given the head of a linked list, sort the items using the following procedure:

Start with the first item: The sorted section initially contains just the first item. The rest of the items await their turn in the unsorted section.
Pick and Place: For each step, pick the next item from the unsorted section, find its correct spot in the sorted section, and place it there.
Repeat: Continue until all items are in the sorted section.
Return the head of the sorted linked list.

As a preview, here is a graphical example of the required technique (also known as the insertion sort algorithm). 
The partially sorted list (black) initially contains only the first element in the list. One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration.

Sorting unordered list of integers using insertion sort technique

When you have finished your sorting, receive bonus points for evaluating the time and space complexity of your solution. 
To get full points, you must define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.'''

def sort_list(head):
    if head is None or head.next is None:
        return head
    
    sorted_head = head
    unsorted_node = head.next 

    sorted_head.next = None

    while unsorted_node is not None:
        next_unsorted = unsorted_node.next 
        if unsorted_node.value < sorted_head.value:
            unsorted_node.next = sorted_head
            sorted_head = unsorted_node
        else:
            current_sorted = sorted_head
            while current_sorted.next is not None and current_sorted.next.value < unsorted_node.value:
                current_sorted = current_sorted.next
            unsorted_node.next = current_sorted.next
            current_sorted.next = unsorted_node
        unsorted_node = next_unsorted
    return sorted_head
            
'''Problem 4: Calculate Prize Money
In the game show, contestants win prize money for each of the challenges they participate in. Write a function get_total_prize() that accepts the heads of two non-empty linked lists, prize_a and prize_b, representing two non-negative integers. The digits are stored in reverse order and each node represents a single digit. The function should add the two numbers and return the sum of the prize money as a linked list.

The digits of the sum should also be stored in reverse order with each node containing a single digit.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.'''
def add_two_numbers(head_a, head_b):
    dummy_node = Node(0)
    current = dummy_node
    carry = 0

    while head_a or head_b or carry:
        val_1 = head_a.value if head_a else 0
        val_2 = head_b.value if head_b else 0

        # compute total sum
        total = val_1 + val_2 + carry

        # compute carry
        carry = total // 10

        # get remainder as new digit
        new_digit = total % 10

        # create node with compute sum
        current.next = Node(new_digit)
        current = current.next

        if head_a:
            head_a = head_a.next
        if head_b:
            head_b = head_b.next 

    return dummy_node.next

'''Problem 5: Next Contestant to Beat
You are given the head of a linked list contestant_scores with n nodes where each node represents the current score of a contestant in the game.

For each node in the list, find the value of the contestant with the next highest score. That is, for each score, find the value of the first node that is next to it and has a strictly larger value than it.

Return an integer array answer where answer[i] is the value of the next greater node of the ith node (1-indexed). If the ith node does not have a next greater node, set answer[i] = 0.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.'''   
def next_highest_scoring_contestant(contestant_scores):
    # get array from linked list
    values = []
    current = contestant_scores

    while current is not None:
        values.append(current.value)
        current = current.next

    # create result arrays filed with zeros 
    result = [0] * len(values)
    stack = []

    for i, value in enumerate(values):
        while stack and values[stack[-1]] < value:
            index = stack.pop()
            result[index] = value
        stack.append(i)
    return result

###################################################
# Session 2: Linked Lists II
###################################################
# Standard Problem Set Version 1
# -------------------------------------------------
'''Problem 1: Wild Goose Chase
You're a detective and have been given an anonymous tip on your latest case, but something about it seems fishy - you suspect the clue might be a red herring meant to send you around in circles. 
Write a function is_circular() that accepts the head of a singly linked list clues and returns True if the tail of the linked list points at the head of the linked list. Otherwise, return False.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.'''
def is_circular(clues):
    if clues is None or clues.next is None:
        return False
    
    slow = fast = clues
    while fast is not None and fast.next is not None:
        slow  = slow.next
        fast = fast.next.next
        if slow == fast:
            return True 
    return False

'''Problem 2: Breaking the Cycle
All the clues that lead us in circles are false evidence we need to purge! Given the head of a linked list evidence, clean up the evidence list by identifying any false clues. 
Write a function collect_false_evidence() that returns an array containing all values that are part of any cycle in evidence. Return the values in any order.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.'''
def collect_false_evidence(evidence):
    false_evidence = []
    
    if evidence is None or evidence.next is None:
        return false_evidence
    
    slow = fast = evidence
    is_circular = False
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            is_circular = True
            break 
    
    if is_circular == False:
        return false_evidence
    
    fast = evidence
    while fast != slow:
        slow = slow.next
        fast = fast.next
    cycle_start = fast

    current = cycle_start
    while True:
        false_evidence.append(current.value)
        current = current.next
        if current == cycle_start:
            break
    return false_evidence

'''Problem 3: Prioritizing Suspects
You've identified a list of suspect, but time is limited and you won't be able to question all of them today. Write a function partition() to help prioritize the order in which you question suspects. 
Given the head of a linked list of integers suspect_ratings, where each integer represents the suspiciousness of the a given suspect and a value threshold, 
partition the linked list such that all nodes with values greater than threshold come before nodes with values less than or equal to threshold.

Return the head of the partitioned list.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.'''
def partition(suspect_ratings, threshold):
    # create dummy nodes for low and high partitions
    low_value_node = Node(0)
    high_value_node = Node(0)

    # create pointers to build list
    low_head = low_value_node
    high_head = high_value_node

    # traverse the list
    current = suspect_ratings
    while current is not None:
        if current.value <= threshold:
            low_head.next = current
            low_head = low_head.next
        else:
            high_head.next = current
            high_head = high_head.next
        current = current.next

    # terminate low partition list
    low_head.next = None
    # combine low head after high head
    high_head.next = low_value_node.next
    return high_value_node.next

'''Problem 4: Puzzling it Out
A new witness has emerged and provided a new account of events the night of the crime. Given the heads of two sorted linked lists, known_timeline and witness_timeline, each representing a numbered sequence of events,
merge the two timelines into one sorted sequence of events. The resulting linked list should be made by splicing together the nodes of the first two timelines. Return the head of the merged timeline.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.'''
def merge_timelines(known_timeline, witness_timeline):
    if known_timeline is None and witness_timeline is not None:
        return witness_timeline
    elif known_timeline is not None and witness_timeline is None:
        return known_timeline
    
    merged_node = Node(0)
    merged = merged_node

    node_one = known_timeline
    node_two = witness_timeline
    while node_one and node_two:
        if node_one.value <= node_two.value:
            merged.next = node_one
            node_one = node_one.next
        else:
            merged.next = node_two
            node_two = node_two.next
        merged = merged.next
        
    if node_one is not None:
        merged.next = node_one
    else:
        merged.next = node_two
    return merged_node.next

'''Problem 5: A New Perspective
You're having a tough time making a break in the case, and it's time to shake things up to gain a new perspective. Given the head of a linked list of numbered pieces of evidence evidence, and a non-negative integer k, 
rotate the list to the right by k places. Return the head of the rotated list.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.'''
def rotate_right(head, k):
    if head is None:
        return head
    
    # get length of linked list
    length = 0
    current = head
    tail = None
    while current:
        tail = current
        current = current.next
        length += 1
    
    # compute effective rotation
    k = k % length
    if k == 0:
        return head
    
    # connect tail to head to form a circular list
    tail.next = head 

    # find new tail
    split_point = length - k
    current = head 
    for i in range(1, split_point):
        current = current.next
    
    new_head = current.next
    current.next = None
    return new_head

'''Problem 6: Adding Up the Evidence
You have all your evidence, and it's time to sum it to the final answer! You are given the heads of two non-empty non-empty linked lists head_a and head_b representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

The digits of the sum should also be stored in reverse order with each node containing a single digit.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.'''
def add_two_numbers(head_a, head_b):
    if head_a is None:
        return head_b
    elif head_b is None:
        return head_a
    
    dummy_node = Node(0)
    current = dummy_node
    carry = 0

    while head_a or head_b or carry:
        val1 = head_a.value if head_a else 0
        val2 = head_b.value if head_b else 0

        total = val1 + val2 + carry
        new_digit = total % 10
        carry = total // 10
        current.next = Node(new_digit)
        current = current.next

        if head_a:
            head_a = head_a.next
        if head_b:
            head_b = head_b.next
    return dummy_node.next

# -------------------------------------------------
# Standard Problem Set Version 2
# -------------------------------------------------
'''Problem 1: Measuring Loop Length
As a trail worker, you've been tasked with measuring the length of a loop trail that circles back to its starting point. 
Given the head of a linked list trailhead where each node represents a trail marker and the last marker points back to the first marker, return the length of the trail. 
Assume the length of the trail is equal to the number of markers.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.'''
def trail_length(trailhead):
    if trailhead is None:
        return 0
    if  trailhead.next is None:
        return 1
    
    current = trailhead
    temp_node = current
    count = 1

    while current:
        current = current.next
        count += 1
        if current.next == temp_node:
            break 
    return count

'''Problem 2: Clearing the Path
While maintaining a trail, you discover that some parts of the path loop back on themselves, creating confusing detours. Given the head of a linked list that may contain cycles trailhead, 
write a function that removes any loops/cycles in the trail ensuring a clear, straightforward path. Return the head of the cleared trail.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.'''
def clear_trail(trailhead):
    if trailhead is None:
        return trailhead
    
    slow = fast = trailhead
    is_cycle = False

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            is_cycle = True
            break

    if not is_cycle:
        return trailhead
    
    fast = trailhead
    while fast != slow:
        slow = slow.next
        fast = fast.next
        
    cycle_start = slow

    current = cycle_start
    while current.next != cycle_start:
        current = current.next 

    current.next = None
    return trailhead

'''Problem 3: Removing Duplicate Markers
When clearing an old trail, you notice some markers have been placed more than once, confusing hikers. Given the head of a sorted linked list of numbered trail markers, trailhead, 
write a function that removes all duplicate markers, keeping only the unique ones. Return the head of the updated trail.'''
def remove_duplicate_markers(trailhead):
    if trailhead is None:
        return trailhead
    
    dummy = Node(0)
    dummy.next = trailhead

    prev = dummy    
    current = trailhead

    while current is not None:
        if current.next and current.value == current.next.value:
            while current.next and current.value == current.next.value:
                current = current.next
            prev.next = current.next
            current = current.next
        else:
            prev = current
            current = current.next
    return dummy.next





if __name__ == "__main__":
    print("-------- # Session 1: Linked Lists II -------- ")
    print("------ # Standard Problem Set Version 1 ------ ")
    print("Problem 1: Building a Playlist")
    node_three = SongNode("Bad Romance")
    node_two = SongNode("Party Rock Anthem", node_three)
    node_one = SongNode("Uptown Funk", node_two)
    top_hits_2010s = node_one
    print_linked_list(top_hits_2010s)
    print()
    print("Problem 2: Top Artists")
    playlist = SongNode_artist("Saturn", "SZA", 
                    SongNode_artist("Who", "Jimin", 
                            SongNode_artist("Espresso", "Sabrina Carpenter", 
                                    SongNode_artist("Snooze", "SZA"))))
    print(get_artist_frequency(playlist))
    print()
    print("Problem 3: Glitching Out")
    playlist = SongNode_artist("SOS", "ABBA", 
                    SongNode_artist("Simple Twist of Fate", "Bob Dylan",
                        SongNode_artist("Dreams", "Fleetwood Mac",
                            SongNode_artist("Lovely Day", "Bill Withers"))))
    print_linked_list_tuple(remove_song(playlist, "Dreams"))
    print()
    print("Problem 4: On Repeat")
    song1 = SongNode("GO!", "Common")
    song2 = SongNode("N95", "Kendrick Lamar")
    song3 = SongNode("WIN", "Jay Rock")
    song4 = SongNode("ATM", "J. Cole")
    song1.next = song2
    song2.next = song3
    song3.next = song4
    song4.next = song2
    print(on_repeat(song1))
    print()
    print("Problem 5: Looped")
    song0 = SongNode("ioaiai", "ahufioahuf")
    song1 = SongNode("Wein", "AL SHAMI")
    song2 = SongNode("Si Ai", "Tayna")
    song3 = SongNode("Qalbi", "Yasser Abd Alwahab")
    song4 = SongNode("La", "DYSTINCT")
    song0.next = song1
    song1.next = song2
    song2.next = song3
    song3.next = song4
    song4.next = song2
    print(loop_length(song0))
    print()
    print("Problem 6: Volume Control")
    song_audio = Node(5, Node(3, Node(1, Node(2, Node(5, Node(1, Node(2)))))))
    print(count_critical_points(song_audio))
    print()
    print()
    print("------ # Standard Problem Set Version 2 ------ ")
    print("Problem 1: Why is it Always You Three")
    print_linked_list_value(head)
    print()
    print("Problem 2: 200 Points for Gryffindor")
    house_points = Node_score("Gryffindor", 600, 
                              Node_score("Ravenclaw", 300, 
                                         Node_score("Slytherin", 500, 
                                                    Node_score("Hufflepuff", 600))))
    score = 600
    print(count_element(house_points, score))
    print()
    print("Problem 3: Target Practice")
    potions1 = Node_potion("Poison Antidote", Node_potion("Shrinking Solution", Node_potion("Trollblood Tincture")))
    potions2 = Node_potion("Elixir of Life", Node_potion("Sleeping Draught", Node_potion("Babbling Beverage", Node_potion("Aging Potion"))))

    print(find_middle_potion(potions1))
    print(find_middle_potion(potions2))
    print()
    print("Problem 4: Turn Back Time")
    events = Node("Potion Brewing", 
                  Node("Spell Casting", 
                       Node("Wand Making", 
                            Node("Dragon Taming", 
                                 Node("Broomstick Flying")))))

    print_linked_list_value(reverse(events))
    print()
    print("Problem 5: Mirror, Mirror")
    list1 = Node("Phoenix", Node("Dragon", Node("Phoenix")))
    list2 = Node("Werewolf", Node("Vampire", Node("Griffin")))

    print(is_mirrored(list1))
    print(is_mirrored(list2))
    print()
    print("Problem 6: Magic Loop")
    path_start = Node("Mystic Falls")
    waypoint1 = Node("Troll's Bridge")
    waypoint2 = Node("Elven Arbor")
    waypoint3 = Node("Fairy Glade")

    path_start.next = waypoint1
    waypoint1.next = waypoint2
    waypoint2.next = waypoint3
    waypoint3.next = waypoint1

    print(loop_start(path_start))
    print()
    print("------ # Advanced Problem Set Version 1 ------ ")
    print("Problem 1: Selective DNA Deletion")
    dna_strand = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, Node(10, Node(11, Node(12, Node(13)))))))))))))
    print_linked_list_value(edit_dna_sequence(dna_strand, 2, 3))
    print()
    print("Problem 2: Protein Folding Loop Detection")
    protein_head = Node('Ala', Node('Gly', Node('Leu', Node('Val'))))
    protein_head.next.next.next.next = protein_head.next 

    print(cycle_length(protein_head))
    print()
    print("Problem 3: Segmenting Protein Chains for Analysis")
    protein1 = Node('Ala', Node('Gly', Node('Leu', Node('Val', Node('Pro', Node('Ser', Node('Thr', Node('Cys'))))))))
    protein2 = Node('Ala', Node('Gly', Node('Leu', Node('Val'))))

    parts = split_protein_chain(protein1, 3)
    for part in parts:
        print_linked_list_value(part)
    print()
    parts = split_protein_chain(protein2, 5)
    for part in parts:
        print_linked_list_value(part)
    print()
    print("Problem 4: Maximum Protein Pair Stability")
    head1 = Node(5, Node(4, Node(2, Node(1))))
    head2 = Node(4, Node(2, Node(2, Node(3))))

    print(max_protein_pair_stability(head1))
    print(max_protein_pair_stability(head2))
    print()
    print("Problem 5: Grouping Experiments")
    experiment_results1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    experiment_results2 = Node(2, Node(1, Node(3, Node(5, Node(6, Node(4, Node(7)))))))

    print_linked_list_value(odd_even_experiments(experiment_results1))
    print_linked_list_value(odd_even_experiments(experiment_results2))
    print()
    print("Problem 1: Linked List Game")
    game1 = Node(2, Node(1))
    game2 = Node(2, Node(5, Node(4, Node(7, Node(20, Node(5))))))
    game3 = Node(4, Node(5, Node(2, Node(1))))

    print(game_result(game1))
    print(game_result(game2))
    print(game_result(game3))
    print()
    print("Problem 2: Cycle Start")
    path_start = Node('Start', Node('Point 1', Node('Point 2', Node('Point 3'))))
    path_start.next.next.next.next = path_start.next
    print(cycle_start(path_start))
    print()
    print("Problem 3: Fastest Wins!")
    head1 = Node(4, Node(2, Node(1, Node(3))))
    head2 = Node(-1, Node(5, Node(3, Node(4, Node(0)))))

    print_linked_list_value(sort_list(head1))
    print_linked_list_value(sort_list(head2))
    print()
    print("Problem 4: Calculate Prize Money")
    head_a = Node(2, Node(4, Node(3))) # 342
    head_b = Node(5, Node(6, Node(4))) # 465
    print_linked_list_value(add_two_numbers(head_a, head_b))
    print()
    print("Problem 5: Next Contestant to Beat")
    contestant_scores1 = Node(2, Node(1, Node(5)))
    contestant_scores2 = Node(2, Node(7, Node(4, Node(3, Node(5)))))

    print(next_highest_scoring_contestant(contestant_scores1))
    print(next_highest_scoring_contestant(contestant_scores2))
    print()
    print("-------- # Session 2: Linked Lists II -------- ")
    print("------ # Standard Problem Set Version 1 ------ ")
    print("Problem 1: Wild Goose Chase")
    clue1 = Node("The stolen goods are at an abandoned warehouse")
    clue2 = Node("The mayor is accepting bribes")
    clue3 = Node("They dumped their disguise in the lake")
    clue1.next = clue2
    clue2.next = clue3
    clue3.next = clue1
    print(is_circular(clue1))
    print()
    print("Problem 2: Breaking the Cycle")
    clue1 = Node("Unmarked sedan seen near the crime scene")
    clue2 = Node("The stolen goods are at an abandoned warehouse")
    clue3 = Node("The mayor is accepting bribes")
    clue4 = Node("They dumped their disguise in the lake")
    clue1.next = clue2
    clue2.next = clue3
    clue3.next = clue4
    clue4.next = clue2

    clue5 = Node("A masked figure was seen fleeing the scene")
    clue6 = Node("Footprints lead to the nearby woods")
    clue7 = Node("A broken window was found at the back")
    clue5.next = clue6
    clue6.next = clue7

    print(collect_false_evidence(clue1))
    print(collect_false_evidence(clue5))
    print()
    print("Problem 3: Prioritizing Suspects")
    suspect_ratings = Node(1, Node(4, Node(3, Node(2, Node(5, Node(2))))))
    print("Before partitioning")
    print_linked_list_value(suspect_ratings)
    print("After Partitioning")
    print_linked_list_value(partition(suspect_ratings, 3))
    print()
    print("Problem 4: Puzzling it Out")
    known_timeline = Node(1, Node(2, Node(4)))
    witness_timeline = Node(1, Node(3, Node(4)))
    print_linked_list_value(merge_timelines(known_timeline, witness_timeline))
    print()
    print("Problem 5: A New Perspective")
    evidence_list1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    evidence_list2 = Node(0, Node(1, Node(2)))
    print_linked_list_value(rotate_right(evidence_list1, 2))
    print_linked_list_value(rotate_right(evidence_list2, 4))
    print()
    print("Problem 6: Adding Up the Evidence")
    head_a = Node(2, Node(4, Node(3))) # 342
    head_b = Node(5, Node(6, Node(4))) # 465
    print_linked_list_value(add_two_numbers(head_a, head_b))
    print()
    print("------ # Standard Problem Set Version 2 ------ ")
    print("Problem 1: Measuring Loop Length")
    marker1 = Node("Marker 1")
    marker2 = Node("Marker 2")
    marker3 = Node("Marker 3")
    marker1.next = marker2
    marker2.next = marker3
    marker3.next = marker1
    print(trail_length(marker1))
    print()
    print("Problem 2: Clearing the Path")
    marker1 = Node("Trailhead")
    marker2 = Node("Trail Fork")
    marker3 = Node("The Falls")
    marker4 = Node("Peak")
    marker1.next = marker2
    marker2.next = marker3
    marker3.next = marker4
    marker4.next = marker2
    print_linked_list_value(clear_trail(marker1))
    print()
    print("Problem 3: Removing Duplicate Markers")
    trailhead = Node(1, Node(2, Node(3, Node(3, Node(4)))))
    print_linked_list_value(remove_duplicate_markers(trailhead))
    print()
