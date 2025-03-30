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
    previous = head
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


    
