from collections import defaultdict

class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print(current.song, end=" -> " if current.next else "")
        current = current.next
    print()
        
# node_three = SongNode("Bad Romance")
# node_two = SongNode("Party Rock Anthem", node_three)
# node_one = SongNode("Uptown Funk", node_two)

#top_hits_2010s = node_one

# print_linked_list(top_hits_2010s)

def get_artist_frequency(playlist):
    # create dict
    artist_count = defaultdict(int)
    current = playlist
    # loop threw playlist 
    while current:
        #if current.artist in artist_count:
        artist_count[current.artist] += 1
        current = current.next
    
    return artist_count
    # checking if current is in dict 
    # if yes add one 
    # else create new key in dict 

playlist = SongNode("Saturn", "SZA", 
                SongNode("Who", "Jimin", 
                        SongNode("Espresso", "Sabrina Carpenter", 
                                SongNode("Snooze", "SZA"))))

# print(get_artist_frequency(playlist))

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

playlist = SongNode("SOS", "ABBA", 
                SongNode("Simple Twist of Fate", "Bob Dylan",
                    SongNode("Dreams", "Fleetwood Mac",
                        SongNode("Lovely Day", "Bill Withers"))))

# print_linked_list(remove_song(playlist, "Dreams"))

def on_repeat(playlist_head):
    slow = fast = playlist_head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

song1 = SongNode("GO!", "Common")
song2 = SongNode("N95", "Kendrick Lamar")
song3 = SongNode("WIN", "Jay Rock")
song4 = SongNode("ATM", "J. Cole")
song1.next = song2
song2.next = song3
song3.next = song4
# song4.next = song2

# print(on_repeat(song1))

# def loop_length(playlist_head):
#     count = 0
#     slow = fast = playlist_head
#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next
#         count += 1
#         if slow == fast:
#             return count 
#     return 0


# song0 = SongNode("ioaiai", "ahufioahuf")
# song1 = SongNode("Wein", "AL SHAMI")
# song2 = SongNode("Si Ai", "Tayna")
# song3 = SongNode("Qalbi", "Yasser Abd Alwahab")
# song4 = SongNode("La", "DYSTINCT")
# song0.next = song1
# song1.next = song2
# song2.next = song3
# song3.next = song4
# song4.next = song2

# print(loop_length(song0))

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


song_audio = Node(5, Node(3, Node(1, Node(2, Node(5, Node(1, Node(2)))))))

print(count_critical_points(song_audio))