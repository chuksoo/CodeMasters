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

    
