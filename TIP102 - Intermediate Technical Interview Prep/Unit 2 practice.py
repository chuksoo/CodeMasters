# Session 2: Dictionaries
# Standard Problem Set Version 1
import math 

'''Problem 1: Festival Lineup
Given two lists of strings artists and set_times of length n, write a function lineup() that maps each artist to their set time.

An artist artists[i] has set time set_times[i]. Assume i <= 0 < n and len(artists) == len(set_times).'''
def lineup(artists, set_times):
    dict_map = {key: value for key, value in zip(artists, set_times)}
    return dict_map

'''Problem 2: Planning App
You are designing an app for your festival to help attendees have the best experience possible! 
As part of the application, users will be able to easily search their favorite artist and find out the day, time, and stage the artist is playing at. 
Write a function get_artist_info() that accepts a string artist and a dictionary festival_schedule mapping artist's names to dictionaries containing the day, 
time, and stage they are playing on. Return the dictionary containing the information about the given artist.

If the artist searched for does not exist in festival_schedule, return the dictionary {"message": "Artist not found"}.'''
def get_artist_info(artist, festival_schedule):
    if artist in festival_schedule:
        return festival_schedule[artist]
    else:
        return {'message': 'Artist not found'}
        
'''Problem 3: Ticket Sales
A dictionary ticket_sales is used to map ticket type to number of tickets sold. Return the total number of tickets of all types sold.'''
def total_sales(ticket_sales):
    total_sales = 0
    for val in ticket_sales.values():
        total_sales += val 
    return total_sales

'''Problem 4: Scheduling Conflict
Demand for your festival has exceeded expectations, so you're expanding the festival to span two different venues. 
Some artists will perform both venues, while others will perform at just one. To ensure that there are no scheduling conflicts, 
implement a function identify_conflicts() that accepts two dictionaries venue1_schedule and venue2_schedule each mapping the artists playing at the venue to their set times. 
Return a dictionary containing the key-value pairs that are the same in each schedule.'''
def identify_conflicts(venue1_schedule, venue2_schedule):
    conflict = {}
    for k, v in venue1_schedule.items():
        if k in venue2_schedule.keys() and venue1_schedule[k] == venue2_schedule[k]:
            conflict[k] = v
    return conflict

'''Problem 5: Best Set
As part of the festival, attendees cast votes for their favorite set. Given a dictionary votes that maps attendees id numbers to the artist they voted for, 
return the artist that had the most number of votes. If there is a tie, return any artist with the top number of votes.'''
def best_set(votes):
    from collections import Counter
    vote_count = Counter(votes.values())
    return max(vote_count, key=vote_count.get)

'''Problem 6: Performances with Maximum Audience
You are given an array audiences consisting of positive integers representing the audience size for different performances at a music festival.

Return the combined audience size of all performances in audiences with the maximum audience size.

The audience size of a performance is the number of people who attended that performance.'''
def max_audience_performances(audiences):
    max_num = -9999
    count = 0
    for num in audiences:
        if num > max_num:
            max_num = num
            count = 1
        elif num == max_num:
            count += 1
    return count * max_num

'''Problem 7: Performances with Maximum Audience II
If you used a dictionary as part of your solution to max_audience_performances() in the previous problem, 
try reimplementing the function without using a dictionary. If you implemented max_audience_performances() without using a dictionary, 
try solving the problem with a dictionary.

Once you've come up with your second solution, compare the two. Is one solution better than the other? Why or why not?'''

def max_audience_performances_dict(audiences):
    from collections import Counter
    audience_dict = Counter(audiences)
    max_key = max(audience_dict.keys())
    max_val = [val for key, val in audience_dict.items() if key == max_key]
    return max_key * max_val[0]

'''Problem 8: Popular Song Pairs
Given an array of integers popularity_scores representing the popularity scores of songs in a music festival playlist, return the number of popular song pairs.

A pair (i, j) is called popular if the songs have the same popularity score and i < j.

Hint: number of pairs = (n x n-1)/2'''
def num_popular_pairs(popularity_scores):
    popularity_pairs = 0
    for i in range(len(popularity_scores)):
        for j in range(i+1, len(popularity_scores)):
            if popularity_scores[i] == popularity_scores[j]:
                popularity_pairs += 1
    return popularity_pairs

'''Problem 9: Stage Arrangement Difference Between Two Performances
You are given two strings s and t representing the stage arrangements of performers in two different performances at a music festival, 
such that every performer occurs at most once in s and t, and t is a permutation of s.

The stage arrangement difference between s and t is defined as the sum of the absolute difference between the index of the occurrence of 
each performer in s and the index of the occurrence of the same performer in t.

Return the stage arrangement difference between s and t.

A permutation is a rearrangement of a sequence. For example, [3, 1, 2] and [2, 1 , 3] are both permutations of the list [1, 2, 3].

Hint: Absolute value function'''
def find_stage_arrangement_difference(s, t):
    """
    :type s: List[str]
    :type t: List[str]
    :rtype: int
    """
    stage_abs = 0
    stage_dict = dict()
    for i, val in enumerate(s):
        stage_dict[val] = i
    for i, new_val in enumerate(t):
        if new_val in stage_dict:
            stage_abs += abs(i - stage_dict[new_val])
    return stage_abs

'''Problem 10: VIP Passes and Guests
You're given strings vip_passes representing the types of guests that have VIP passes, and guests representing the guests you have at the music festival. 
Each character in guests is a type of guest you have. You want to know how many of the guests you have are also VIP pass holders.

Letters are case sensitive, so "a" is considered a different type of guest from "A".

Here is the pseudocode for the problem. Implement this in Python and explain your implementation step-by-step.'''
def num_VIP_guests(vip_passes, guests):
    vip_set = set()
    for char in vip_passes:
        vip_set.add(char)

    count = 0
    for ch in guests:
        if ch in vip_set:
            count += 1
    return count

'''Problem 11: Performer Schedule Pattern
Given a string pattern and a string schedule, return True if schedule follows the same pattern. Return False otherwise.

Here, "follow" means a full match, such that there is a one-to-one correspondence between a letter in pattern and a non-empty word in schedule.

You are provided with a partially implemented and buggy version of the solution. Identify and fix the bugs in the code. 
Then, perform a thorough code review and suggest improvements.'''
def schedule_pattern(pattern, schedule):
    
    genres = schedule.split()
    pattern = list(pattern)

    # if len(genres) == len(pattern):
    #     return True

    char_to_genre = {}
    genre_to_char = {}

    for char, genre in zip(pattern, genres):
        if char in char_to_genre:
            if char_to_genre[char] != genre:
                return False
        else:
            char_to_genre[char] = genre

        if genre in genre_to_char:
            if genre_to_char[genre] != char:
                return False
        else:
            genre_to_char[genre] = char
    return True

'''Problem 12: Sort the Performers
You are given an array of strings performer_names, and an array performance_times that consists of distinct positive integers 
representing the performance durations in minutes. Both arrays are of length n.

For each index i, performer_names[i] and performance_times[i] denote the name and performance duration of the ith performer.

Return performer_names sorted in descending order by the performance durations.'''
def sort_performers(performer_names, performance_times):
    """
    :type performer_names: List[str]
    :type performance_times: List[int]
    :rtype: List[str]
    """
    performance_dict = {k:v for k, v in zip(performance_times, performer_names)}
    sorted_time = sorted(performance_times, reverse=True)
    return [performance_dict[val] for val in sorted_time if val in performance_dict]

# Standard Problem Set Version 2
'''Problem 1: Space Crew
Given two lists of length n, crew and position, map the space station crew to their position on board the international space station.

Each crew member crew[i] has job position[i] on board, where 0 <= i < n and len(crew) == len(position).

Hint: Introduction to dictionaries'''
def space_crew(crew, position):
    return {k:v for k, v in zip(crew, position)}

'''Problem 2: Space Encyclopedia
Given a dictionary planets that maps planet names to a dictionary containing the planet's number of moons and orbital period, 
write a function planet_lookup() that accepts a string planet_name and returns a string in the form Planet <planet_name> has an 
orbital period of <orbital period> Earth days and has <number of moons> moons. If planet_name is not a key in planets, 
return "Sorry, I have no data on that planet.".'''
def planet_lookup(planet_name):
    planetary_info = {
    "Mercury": {
        "Moons": 0,
        "Orbital Period": 88
    },
    "Earth": {
        "Moons": 1,
        "Orbital Period": 365.25
    },
    "Mars": {
        "Moons": 2,
        "Orbital Period": 687
    },
    "Jupiter": {
        "Moons": 79,
        "Orbital Period": 10592
    }
    }

    for key in planetary_info.keys():
        if key == planet_name:
            moon = planetary_info[planet_name].get('Moons')
            period = planetary_info[planet_name].get('Orbital Period')
            return f'Planet {planet_name} has an orbital period of {period} Earth days and has {moon} moons.'
    return 'Sorry, I have no data on that planet.'
    
'''Problem 3: Breathing Room
As part of your job as an astronaut, you need to perform routine safety checks. 
You are given a dictionary oxygen_levels which maps room names to current oxygen levels and two integers min_val and max_val 
specifying the acceptable range of oxygen levels. Return a list of room names whose values are outside the range defined by min_val and max_val (inclusive).'''
def check_oxygen_levels(oxygen_levels, min_val, max_val):
    return [k for k, v in oxygen_levels.items() if v < min_val or v > max_val]  

'''Problem 4: Experiment Analysis
Write a function data_difference() that accepts two dictionaries experiment1 and experiment2 and 
returns a new dictionary that contains only key-value pairs found exclusively in experiment1 but not in experiment2.'''
def data_difference(experiment1, experiment2):
    diff_dict = {}
    for key, val in experiment1.items():
        if key not in experiment2.keys() or val not in experiment2.values():
            diff_dict[key] = val
    return diff_dict

'''Problem 5: Name the Node
NASA has asked the public to vote on a new name for one of the nodes in the International Space Station. 
Given a list of strings votes where each string in the list is a voter's suggested new name, implement a function 
get_winner() that returns the suggestion with the most number of votes.

If there is a tie, return either option.'''
def get_winner(votes):
    from collections import Counter
    nasa_votes = Counter(votes)
    max_val = -9999
    for k, v in nasa_votes.items():
        if v > max_val:
            max_val = v
            winner = k
    return winner

'''Problem 6: Check if the Transmission is Complete
Ground control has sent a transmission containing important information. A complete transmission is one where 
every letter of the English alphabet appears at least once.

Given a string transmission containing only lowercase English letters, return true if the transmission is complete, or false otherwise.'''
def check_if_complete_transmission(transmission):
    """
    :type transmission: str
    :rtype: bool
    """
    return len(set(transmission)) == 26

'''Problem 7: Signal Pairs
Ground control is analyzing signal patterns received from different probes. You are given a 0-indexed array signals consisting of distinct strings.

The string signals[i] can be paired with the string signals[j] if the string signals[i] is equal to the reversed string of signals[j]. 
0 <= i < j < len(signals). Return the maximum number of pairs that can be formed from the array signals.

Note that each string can belong in at most one pair.'''
def max_number_of_string_pairs(signals):
    count = 0
    for i in range(len(signals)):
        for j in range(i+1, len(signals)):
            if signals[i] == signals[j][::-1]:
                count += 1
    return count

'''Problem 8: Find the Difference of Two Signal Arrays
You are given two 0-indexed integer arrays signals1 and signals2, representing signal data from two different probes. Return a list answer of size 2 where:

answer[0] is a list of all distinct integers in signals1 which are not present in signals2.
answer[1] is a list of all distinct integers in signals2 which are not present in signals1.
Note that the integers in the lists may be returned in any order.

Below is the pseudocode for the problem. Implement this in Python and explain your implementation step-by-step.'''
def find_difference(signals1, signals2):
    signals1, signals2 = set(signals1), set(signals2)
    diff1 = list(signals1 - signals2)
    diff2 = list(signals2 - signals1)
    return [diff1, diff2]

# Session 2: Dictionaries & Sets
# Standard Problem Set Version 1
'''Problem 1: Most Endangered Species
Imagine you are working on a wildlife conservation database. Write a function named most_endangered() that returns the species with the highest conservation 
priority based on its population.

The function should take in a list of dictionaries named species_list as a parameter. Each dictionary represents data associated with a species, 
including its name, habitat, and wild population. The function should return the name of the species with the lowest population.

If there are multiple species with the lowest population, return the species with the lowest index.'''
def most_endangered(species_list):
    if not species_list:
        return None

    min_val = math.inf
    for dict in species_list:
        if dict['population'] < min_val:
            min_val = dict['population']
            species = dict['name']
    return species

'''Problem 2: Identifying Endangered Species
As part of conservation efforts, certain species are considered endangered and are represented by the string endangered_species. 
Each character in this string denotes a different endangered species. You also have a record of all observed species in a particular region, 
represented by the string observed_species. Each character in observed_species denotes a species observed in the region.

Your task is to determine how many instances of the observed species are also considered endangered.

Note: Species are case-sensitive, so "a" is considered a different species from "A".

Write a function to count the number of endangered species observed.'''
def count_endangered_species(endangered_species, observed_species):
    from collections import Counter
    observed_map = Counter(observed_species)

    count = 0
    for item in endangered_species:
        if item in observed_map:
            count += observed_map[item]
    return count

'''Problem 3: Navigating the Research Station
In a wildlife research station, each letter of the alphabet represents a different observation point laid out in a single row. 
Given a string station_layout of length 26 indicating the layout of these observation points (indexed from 0 to 25), 
you start your journey at the first observation point (index 0). To make observations in a specific order represented by a string observations, 
you need to move from one point to another.

The time taken to move from one observation point to another is the absolute difference between their indices, |i - j|.

Write a function that returns the total time it takes to visit all the required observation points in the given order with one movement.'''
def navigate_research_station(station_layout, observations):
    station_map = {str: i for i, str in enumerate(station_layout)}

    curr = total_time = 0
    for char in observations:
        total_time += abs(station_map[char] - curr)
        curr = station_map[char]
    return total_time

'''Problem 4: Prioritizing Endangered Species Observations
In your work with a wildlife conservation database, you have two lists: observed_species and priority_species. The elements of priority_species 
are distinct, and all elements in priority_species are also in observed_species. Write a function prioritize_observations() that sorts the elements 
of observed_species such that the relative ordering of items in observed_species matches that of priority_species. Species that do not appear in 
priority_species should be placed at the end of observed_species in ascending order.'''
def prioritize_observations(observed_species, priority_species):
    priority_map = {species: i for i, species in enumerate(priority_species)}

    priority_part = []
    non_priority_part = []
    for specie in observed_species:
        if specie in priority_map:
            priority_part.append(specie)
        else:
            non_priority_part.append(specie)

    # sort both parts
    priority_part.sort(key=lambda x: priority_map[x])  # Sort by priority
    non_priority_part.sort()  # Lexicographic order

    return priority_part + non_priority_part

'''Problem 5: Calculating Conservation Statistics
You are given a 0-indexed integer array species_populations of even length, where each element represents the population of a particular species in a wildlife reserve.

As long as species_populations is not empty, you must repetitively:
1. Find the species with the minimum population and remove it.
2. Find the species with the maximum population and remove it.
3. Calculate the average population of the two removed species.
The average of two numbers a and b is (a+b)/2.
For example, the average of 200 and 300 is (200+300)/2=250.
Return the number of distinct averages calculated using the above process.
Note that when there is a tie for a minimum or maximum population, any can be removed.'''
from collections import deque
def distinct_averages(species_populations):
    species_populations.sort()
    species_populations = deque(species_populations)
    distinct_averages = set()
    while species_populations:
        min_val = species_populations.popleft()
        max_val = species_populations.pop()
        avgs = (min_val + max_val) / 2
        distinct_averages.add(avgs)
    return len(distinct_averages)

'''Problem 6: Wildlife Reintroduction
As a conservationist, your research center has been raising multiple endangered species and is now ready to reintroduce them into their native habitats. 
You are given two 0-indexed strings raised_species and target_species. The string raised_species represents the list of species available to release into 
the wild at your center, where each character represents a different species. The string target_speciesrepresents a specific sequence of species you want 
to form and release together.

You can take some species from raised_species and rearrange them to form new sequences.

Return the maximum number of copies of target_species that can be formed by taking species from raised_species and rearranging them.'''
def max_species_copies(raised_species, target_species):
    from collections import Counter
    raised_dict = Counter(raised_species)
    min_val = math.inf
    for char in target_species:
        if char not in raised_dict:
            return 0
        if char in raised_dict.keys():
            min_val = min(min_val, raised_dict[char])
    return min_val

'''Problem 7: Count Unique Species
You are given a string ecosystem_data that consists of digits and lowercase English letters. The digits represent the observed counts of various species 
in a protected ecosystem.

You will replace every non-digit character with a space. For example, "f123de34g8hi34" will become " 123 34 8 34". Notice that you are left with some 
species counts that are separated by at least one space: "123", "34", "8", and "34".

Return the number of unique species counts after performing the replacement operations on ecosystem_data.

Two species counts are considered different if their decimal representations without any leading zeros are different.'''

def count_unique_species(ecosystem_data):
    new_ecodata = ''
    for char in ecosystem_data:
        if not char.isalpha():
            new_ecodata += char 
        else:
            new_ecodata += ' '
    result = [int(x) for x in new_ecodata.split()]
    return len(set(result)) 

'''Problem 8: Equivalent Species Pairs
In an effort to understand species diversity in different habitats, researchers are analyzing species pairs observed in various regions. 
Each pair is represented by a list [a, b] where a and b represent two species observed together.

A species pair [a, b] is considered equivalent to another pair [c, d] if and only if either (a == c and b == d) or (a == d and b == c). 
This means that the order of species in a pair does not matter.

Your task is to determine the number of equivalent species pairs in the list of observed species pairs.'''

def num_equiv_species_pairs(species_pairs):
    pair_count = {}
    total_pairs = 0

    for pair in species_pairs:
        pair.sort()
        pair = tuple(pair)

        if pair in pair_count:
            total_pairs += pair_count[pair]
            pair_count[pair] += 1
        else:
            pair_count[pair] = 1
    return total_pairs
    
# Advanced Problem Set Version 1
'''Problem 1: Balanced Art Collection
As the curator of an art gallery, you are organizing a new exhibition. You must ensure the collection of art pieces are balanced to attract the right range of buyers. 
A balanced collection is one where the difference between the maximum and minimum value of the art pieces is exactly 1.

Given an integer array art_pieces representing the value of each art piece, write a function find_balanced_subsequence() that 
returns the length of the longest balanced subsequence.

A subsequence is a sequence derived from the array by deleting some or no elements without changing the order of the remaining elements.'''

def find_balanced_subsequence(art_pieces):
    from collections import Counter
    if not art_pieces:
        return 0
    
    freq_count = Counter(art_pieces)
    max_length = 0
    for val in freq_count.values():
        if (val + 1) in freq_count:
            max_length = max(max_length, freq_count[val] + freq_count[val + 1]) 
    return max_length

'''Problem 2: Verifying Authenticity
Your art gallery has just been shipped a new collection of numbered art pieces, and you need to verify their authenticity. 
The collection is considered "authentic" if it is a permutation of an array base[n].

The base[n] array is defined as [1, 2, ..., n - 1, n, n], meaning it is an array of length n + 1 containing the integers from 1 to n - 1 exactly once, 
and the integer n twice. For example, base[1] is [1, 1] and base[3] is [1, 2, 3, 3].

Write a function is_authentic_collection that accepts an array of integers art_pieces and returns True if the given array is an authentic array, 
and otherwise returns False.

Note: A permutation of integers represents an arrangement of these numbers. For example [3, 2, 1] and [2, 1, 3] are both permutations of 
the series of numbers 1, 2, and 3.'''
def is_authentic_collection(art_pieces):
    from collections import Counter
    if not art_pieces:
        return False
    
    n = max(art_pieces)
    if len(art_pieces) != n + 1:
        return False
    
    freq_dict = Counter(art_pieces)
    for i in range(1, n - 1):
        if freq_dict[i] != 1:
            return False
    
    if freq_dict[n] != 2:
        return False 
    return True

'''Problem 3: Gallery Wall
You are tasked with organizing a collection of art prints represented by a list of strings collection. 
You need to display these prints on a single wall in a 2D array format that meets the following criteria:

The 2D array should contain only the elements of the array collection.
Each row in the 2D array should contain distinct strings.
The number of rows in the 2D array should be minimal.
Return the resulting array. If there are multiple answers, return any of them. Note that the 2D array can have a different number of elements on each row.'''
def organize_exhibition(collection):
    from collections import Counter
    collections_map = Counter(collection)
    max_rows = max(collections_map.values())
    result = [[] for _ in range(max_rows)]

    for item, count in collections_map.items():
        for i in range(count):
            result[i].append(item)
    return result

'''Problem 4: Gallery Subdomain Traffic
Your gallery has been trying to increase it's online presence by hosting several virtual galleries. 
Each virtual gallery's web traffic is tracked through domain names, where each domain may have subdomains.

A domain like "modern.artmuseum.com" consists of various subdomains. At the top level, we have "com", at the next level, we have "artmuseum.com", 
and at the lowest level, "modern.artmuseum.com". When visitors access a domain like "modern.artmuseum.com", they also implicitly visit the parent 
domains "artmuseum.com" and "com".

A count-paired domain is represented as "rep d1.d2.d3" where rep is the number of visits to the domain and d1.d2.d3 is the domain itself.

For example, "9001 modern.artmuseum.com" indicates that "modern.artmuseum.com" was visited 9001 times.
Given an array of count-paired domains cpdomains, return an array of the count-paired domains of each subdomain. The order of the output does not matter.'''
def subdomain_visits(cpdomains):
    domain_map = {}
    for item in cpdomains:
        items = item.split()
        items[0] = int(items[0])
    
        domains = items[1].split('.')
        for i in range(0, len(domains)):
            subdomains = '.'.join(domains[i:])
            if subdomains in domain_map:
                domain_map[subdomains] += items[0]
            else:
                domain_map[subdomains] = items[0]
    
    result = [(str(v) + ' ' + k) for k, v in domain_map.items()]
    return result

'''Problem 5: Beautiful Collection
Your gallery has entered a competition for the most beautiful collection. Your collection is represented by a string collection where each artist in your 
gallery is represented by a character. The beauty of a collection is defined as the difference in frequencies between the most frequent and least frequent characters.

For example, the beauty of "abaacc" is 3 - 1 = 2.
Given a string collection, write a function beauty_sum() that returns the sum of beauty of all of its substrings (subcollections), not just of the collection itself.'''
def beauty_sum(collection):
    total_beauty = 0
    for i in range(0, len(collection) - 1):
        collection_map = [0] * 26
        for j in range(i, len(collection)):
            collection_map[ord(collection[j]) - ord('a')] += 1

            max_freq = max(collection_map)
            min_freq = float('inf')

            for freq in collection_map:
                if freq > 0:
                    min_freq = min(min_freq, freq)
            beauty = max_freq - min_freq
            total_beauty += beauty 
    return total_beauty

'''Problem 6: Counting Divisible Collections in the Gallery
You have a list of integers collection_sizes representing the sizes of different art collections in your gallery and are trying to determine how to 
group them to best fit in your space. Given an integer k write a function count_divisible_collections() that returns the number of non-empty subarrays 
(contiguous parts of the array) where the sum of the sizes is divisible by k.'''
def count_divisible_collections(collection_sizes, k):
    pass


if __name__ == "__main__":
    print("-------- # Session 1: Dictionaries -------- ")
    print("------ # Standard Problem Set Version 1 ------ ")
    artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
    set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

    artists2 = []
    set_times2 = []

    print(lineup(artists1, set_times1))
    print(lineup(artists2, set_times2))
    print()
    festival_schedule = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
    }

    print(get_artist_info("Blood Orange", festival_schedule)) 
    print(get_artist_info("Taylor Swift", festival_schedule)) 
    print()
    ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}
    print(total_sales(ticket_sales))
    print()
    venue1_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "8:00 PM",
    "HARDY": "7:00 PM",
    "Bruce Springsteen": "6:00 PM"
    }

    venue2_schedule = {
        "Stromae": "9:00 PM",
        "Janelle Monáe": "10:30 PM",
        "HARDY": "7:00 PM",
        "Wizkid": "6:00 PM"
    }

    print(identify_conflicts(venue1_schedule, venue2_schedule))
    print()
    votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
    }

    votes2 = {
        1234: "SZA", 
        1235: "Yo-Yo Ma",
        1236: "Ethel Cain",
        1237: "Ethel Cain",
        1238: "SZA"
    }

    print(best_set(votes1))
    print(best_set(votes2))
    print()
    audiences1 = [100, 200, 200, 150, 100, 250]
    audiences2 = [120, 180, 220, 150, 220]

    print(max_audience_performances(audiences1))
    print(max_audience_performances(audiences2))
    print()
    audiences1 = [100, 200, 200, 150, 100, 250]
    audiences2 = [120, 180, 220, 150, 220]

    print(max_audience_performances_dict(audiences1))
    print(max_audience_performances_dict(audiences2))
    print()
    popularity_scores1 = [1, 2, 3, 1, 1, 3]
    popularity_scores2 = [1, 1, 1, 1]
    popularity_scores3 = [1, 2, 3]

    print(num_popular_pairs(popularity_scores1))
    print(num_popular_pairs(popularity_scores2))
    print(num_popular_pairs(popularity_scores3)) 
    print()
    s1 = ["Alice", "Bob", "Charlie"]
    t1 = ["Bob", "Alice", "Charlie"]
    s2 = ["Alice", "Bob", "Charlie", "David", "Eve"]
    t2 = ["Eve", "David", "Bob", "Alice", "Charlie"]

    print(find_stage_arrangement_difference(s1, t1))
    print(find_stage_arrangement_difference(s2, t2))
    print()
    vip_passes1 = "aA"
    guests1 = "aAAbbbb"

    vip_passes2 = "z"
    guests2 = "ZZ"

    print(num_VIP_guests(vip_passes1, guests1))
    print(num_VIP_guests(vip_passes2, guests2))
    print()
    pattern1 = "abba"
    schedule1 = "rock jazz jazz rock"

    pattern2 = "abba"
    schedule2 = "rock jazz jazz blues"

    pattern3 = "aaaa"
    schedule3 = "rock jazz jazz rock"

    print(schedule_pattern(pattern1, schedule1))
    print(schedule_pattern(pattern2, schedule2))
    print(schedule_pattern(pattern3, schedule3))
    print()
    performer_names1 = ["Mary", "John", "Emma"]
    performance_times1 = [180, 165, 170]

    performer_names2 = ["Alice", "Bob", "Bob"]
    performance_times2 = [155, 185, 150]

    print(sort_performers(performer_names1, performance_times1)) 
    print(sort_performers(performer_names2, performance_times2))
    print()
    print("------ # Standard Problem Set Version 2 ------ ")
    exp70_crew = ["Andreas Mogensen", "Jasmin Moghbeli", "Satoshi Furukawa", "Loral O'Hara", "Konstantin Borisov"]
    exp70_positions = ["Commander", "Flight Engineer", "Flight Engineer", " Flight Engineer", "Flight Engineer"] 

    ax3_crew = ["Michael Lopez-Alegria", "Walter Villadei", "Alper Gezeravci", "Marcus Wandt"]
    ax3_positions = ["Commander", "Mission Pilot", "Mission Specialist", "Mission Specialist"]

    print(space_crew(exp70_crew, exp70_positions))
    print(space_crew(ax3_crew, ax3_positions))
    print()
    print(planet_lookup("Jupiter"))
    print(planet_lookup("Pluto"))
    print()
    oxygen_levels = {
    "Command Module": 21,
    "Habitation Module": 20,
    "Laboratory Module": 19,
    "Airlock": 22,
    "Storage Bay": 18
    }

    min_val = 19
    max_val = 22

    print(check_oxygen_levels(oxygen_levels, min_val, max_val))
    print()
    exp1_data = {'temperature': 22, 'pressure': 101.3, 'humidity': 45}
    exp2_data = {'temperature': 18, 'pressure': 101.3, 'radiation': 0.5}

    print(data_difference(exp1_data, exp2_data))
    print()
    votes1 = ["Colbert", "Serenity", "Serenity", "Tranquility", "Colbert", "Colbert"]
    votes2 = ["Colbert", "Serenity", "Serenity", "Tranquility", "Colbert"]

    print(get_winner(votes1))
    print(get_winner(votes2))
    print()
    transmission1 = "thequickbrownfoxjumpsoverthelazydog"
    transmission2 = "spacetravel"

    print(check_if_complete_transmission(transmission1))
    print(check_if_complete_transmission(transmission2))
    print()
    signals1 = ["cd", "ac", "dc", "ca", "zz"]
    signals2 = ["ab", "ba", "cc"]
    signals3 = ["aa", "ab"]

    print(max_number_of_string_pairs(signals1))
    print(max_number_of_string_pairs(signals2))
    print(max_number_of_string_pairs(signals3))
    print()
    signals1_example1 = [1, 2, 3]
    signals2_example1 = [2, 4, 6]

    signals1_example2 = [1, 2, 3, 3]
    signals2_example2 = [1, 1, 2, 2]

    print(find_difference(signals1_example1, signals2_example1)) 
    print(find_difference(signals1_example2, signals2_example2))
    print()
    print("-------- # Session 2: Dictionaries & Sets -------- ")
    print("------ # Standard Problem Set Version 1 ------ ")
    species_list = [
    {"name": "Amur Leopard",
     "habitat": "Temperate forests",
     "population": 84
    },
    {"name": "Javan Rhino",
     "habitat": "Tropical forests",
     "population": 72
    },
    {"name": "Vaquita",
     "habitat": "Marine",
     "population": 10
    }
    ]

    print(most_endangered(species_list))
    print()
    endangered_species1 = "aA"
    observed_species1 = "aAAbbbb"

    endangered_species2 = "z"
    observed_species2 = "ZZ"

    print(count_endangered_species(endangered_species1, observed_species1)) 
    print(count_endangered_species(endangered_species2, observed_species2)) 
    print()
    station_layout1 = "pqrstuvwxyzabcdefghijklmno"
    observations1 = "wildlife"

    station_layout2 = "abcdefghijklmnopqrstuvwxyz"
    observations2 = "cba"

    print(navigate_research_station(station_layout1, observations1))  
    print(navigate_research_station(station_layout2, observations2))
    print()
    observed_species1 = ["🐯", "🦁", "🦌", "🦁", "🐯", "🐘", "🐍", "🦑", "🐻", "🐯", "🐼"]
    priority_species1 = ["🐯", "🦌", "🐘", "🦁"]  

    observed_species2 = ["bluejay", "sparrow", "cardinal", "robin", "crow"]
    priority_species2 = ["cardinal", "sparrow", "bluejay"]

    print(prioritize_observations(observed_species1, priority_species1))
    print(prioritize_observations(observed_species2, priority_species2))
    print()
    species_populations1 = [4,1,4,0,3,5]
    species_populations2 = [1,100]

    print(distinct_averages(species_populations1))
    print(distinct_averages(species_populations2)) 
    print()
    raised_species1 = "abcba"
    target_species1 = "abc"
    print(max_species_copies(raised_species1, target_species1))  # Output: 1

    raised_species2 = "aaaaabbbbcc"
    target_species2 = "abc"
    print(max_species_copies(raised_species2, target_species2)) # Output: 2
    print()
    ecosystem_data1 = "f123de34g8hi34"
    ecosystem_data2 = "species1234forest234"
    ecosystem_data3 = "x1y01z001"

    print(count_unique_species(ecosystem_data1))
    print(count_unique_species(ecosystem_data2))
    print(count_unique_species(ecosystem_data3))
    print()
    species_pairs1 = [[1,2],[2,1],[3,4],[5,6]]
    species_pairs2 = [[1,2],[1,2],[1,1],[1,2],[2,2]]

    print(num_equiv_species_pairs(species_pairs1))
    print(num_equiv_species_pairs(species_pairs2))
    print()
    print("------ # Advanced Problem Set Version 1 ------ ")
    art_pieces1 = [1,3,2,2,5,2,3,7]
    art_pieces2 = [1,2,3,4]
    art_pieces3 = [1,1,1,1]

    print(find_balanced_subsequence(art_pieces1))
    print(find_balanced_subsequence(art_pieces2))
    print(find_balanced_subsequence(art_pieces3))
    print()
    collection1 = [2, 1, 3]
    collection2 = [1, 3, 3, 2]
    collection3 = [1, 1]

    print(is_authentic_collection(collection1))
    print(is_authentic_collection(collection2))
    print(is_authentic_collection(collection3))
    print()
    collection1 = ["O'Keefe", "Kahlo", "Picasso", "O'Keefe", "Warhol", 
              "Kahlo", "O'Keefe"]
    collection2 = ["Kusama", "Monet", "Ofili", "Banksy"]

    print(organize_exhibition(collection1))
    print(organize_exhibition(collection2))
    print()
    cpdomains1 = ["9001 modern.artmuseum.com"]
    cpdomains2 = ["900 abstract.gallery.com", "50 impressionism.com", 
                "1 contemporary.gallery.com", "5 medieval.org"]

    print(subdomain_visits(cpdomains1))
    print(subdomain_visits(cpdomains2))
    print()
    print(beauty_sum("aabcb")) 
    print(beauty_sum("aabcbaa"))
    print()
    nums1 = [4, 5, 0, -2, -3, 1]
    k1 = 5
    nums2 = [5]
    k2 = 9

    print(count_divisible_collections(nums1, k1))  
    print(count_divisible_collections(nums2, k2))  
    print()

