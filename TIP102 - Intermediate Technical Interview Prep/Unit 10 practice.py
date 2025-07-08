###################################################
# Session 1: Graphs
###################################################
# Standard Problem Set Version 1
# -------------------------------------------------
from collections import deque

'''Problem 1: Graphing Flights
The following graph represents the different flights offered by CodePath Airlines. Each node or vertex represents an airport (JFK - New York City, LAX - Los Angeles, DFW - Dallas Fort Worth, and ATL - Atlanta), 
and an edge between two vertices indicates that CodePath airlines offers flights between those two airports.

Create a variable flights that represents the undirected graph below as an adjacency dictionary, where each node's value is represented by a string with the airport's name (ex. "JFK").'''
# list nodes
airports = ['JFK', 'LAX', 'DFW', 'ATL']

# initialize an empty adjacent dict
flights = {airport: [] for airport in airports}

# get undirected edges
edge = [
    ('JFK', 'LAX'),
    ('JFK', 'DFW'),
    ('DFW', 'ATL')
]
for a, b in edge:
    flights[a].append(b)
    flights[b].append(a)

'''Problem 2: There and Back
As a flight coordinator for CodePath airlines, you have a 0-indexed adjacency list flights with n nodes where each node represents the ID of a different destination and flights[i] is an integer array 
indicating that there is a flight from destination i to each destination in flights[i]. Write a function bidirectional_flights() that returns True if for any flight from a destination i to a destination j 
there also exists a flight from destination j to destination i. Return False otherwise.'''
def bidirectional_flights(flights):
    # adj = [[0 for x in range(len(flights))] for y in range(len(flights))]
    # convert neighbor-list to set
    adjacency = [set(neigh) for neigh in flights]

    # for every directed edge i -> j, check that j -> i exists
    for i, neigh in enumerate(adjacency):
        for j in neigh:
            if j < 0 or j >= len(adjacency) or i not in adjacency[j]:
                return False
            
    # if no one way flight, return True
    return True

'''Problem 3: Finding Direct Flights
Given an adjacency matrix flights of size n x n where each of the n nodes in the graph represent a distinct destination and n[i][j] = 1 indicates that there exists a flight from destination i to destination j 
and n[i][j] = 0 indicates that no such flight exists. Given flights and an integer source representing the destination a customer is flying out of, return a list of all destinations the customer can reach 
from source on a direct flight. You may return the destinations in any order.

A customer can reach a destination on a direct flight if that destination is a neighbor of source.'''
def get_direct_flights(flights, source):
    destination = []

    for i in range(len(flights[source])):
        if flights[source][i] == 1:
            destination.append(i)
    return destination

'''Problem 4: Converting Flight Representations
Given a list of edges flights where flights[i] = [a, b] denotes that there exists a bidirectional flight (incoming and outgoing flight) from city a to city b, return an adjacency dictionary adj_dict 
representing the same flights graph where adj_dict[a] is an array denoting there is a flight from city a to each city in adj_dict[a].'''
def get_adj_dict(flights):
    # create empty map
    adj_dict = {}

    # iterate over each edge
    for [a, b] in flights:
        # ensure both cities are in the dictionary
        if a not in adj_dict:
            adj_dict[a] = []
        if b not in adj_dict:
            adj_dict[b] = []

        # get bidirectional connection - add each to the other's list
        adj_dict[a].append(b)
        adj_dict[b].append(a)
    return adj_dict

'''Problem 5: Find Center of Airport
You are a pilot navigating a new airport and have a map of the airport represented as an undirected star graph with n nodes where each node represents a terminal in the airport labeled from 1 to n. 
You want to find the center terminal in the airport where the pilots' lounge is located.

Given a 2D integer array terminals where each terminal[i] = [u, v] indicates that there is a path (edge) between terminal u and v, return the center of the given airport.

A star graph is a graph where there is one center node and exactly n-1 edges connecting the center node ot every other node.'''
def find_center(terminals):
    star_dict = {}
    for a, b in terminals:
        if a not in star_dict:
            star_dict[a] = 0
        if b not in star_dict:
            star_dict[b] = 0
        star_dict[a] += 1
        star_dict[b] += 1

    target_degree = len(terminals)
    for edge, count in star_dict.items():
        if count == target_degree:
            return edge
    return None

'''Problem 6: Finding All Reachable Destinations
You are a travel coordinator for CodePath Airlines, and you're helping a customer find all possible destinations they can reach from a starting airport. 
The flight connections between airports are represented as an adjacency dictionary flights, where each key is a destination, and the corresponding value 
is a list of other destinations that are reachable through a direct flight.

Given a starting location start, return a list of all destinations reachable from the start location either through a direct flight or connecting flights with layovers. 
The list should be provided in ascending order by number of layovers required.'''
def get_all_destinations_bfs(flights, start):
    # initialize BFS structure
    visited = set([start])
    queue = deque([start])
    result = []

    # perform BFS
    while queue:
        # get the current airport
        popped_node = queue.popleft()
        result.append(popped_node)

        # visit all connected airports
        for nbr in flights.get(popped_node, []):
            if nbr not in visited:
                visited.add(nbr)
                queue.append(nbr)
    return result

'''Problem 7: Finding All Reachable Destinations II
You are a travel coordinator for CodePath Airlines, and you're helping a customer find all possible destinations they can reach from a starting airport. 
The flight connections between airports are represented as an adjacency dictionary flights, where each key is a destination, and the corresponding value 
is a list of other destinations that are reachable through a direct flight.

Given a starting location start, write a function get_all_destinations() that uses Depth First Search (DFS) to return a list of all destinations that can 
be reached from start. The list should include both direct and connecting flights and should be ordered based on the order in which airports are visited in DFS.'''
def get_all_destinations_dfs(flights, start):
    # initialize DFS structure
    visited = set()
    result = []

    # recursive DFS
    def dfs(airport):
        # mark current node as visited
        visited.add(airport)
        result.append(airport)
        # explore neightbors
        for nbr in flights.get(airport, []):
            if nbr not in visited:
                dfs(nbr)
        
    dfs(start)
    return result

'''Problem 8: Find Itinerary
You are a traveler about to embark on a multi-leg journey with multiple flights to arrive at your final travel destination. You have all your boarding passes, 
but their order has gotten all messed up! You want to organize your boarding passes in the order you will use them, from your first flight all the way to your 
last flight that will bring you to your final destination.

Given a list of edges boarding_passes where each element boarding_passes[i] = (departure_airport, arrival_airport) represents a flight from departure_airport 
to arrival_airport, return an array with the itinerary listing out the airports you will pass through in the order you will visit them. Assume that departure 
is scheduled from every airport except the final destination, and each airport is visited only once (i.e., there are no cycles in the route).'''
def find_itinerary(boarding_passes):
    graph = {}
    for dept, arr in boarding_passes:
        graph[dept] = arr

    for dept in graph.keys():
        if dept not in graph.values():
            starting_point = dept

    itinery = [starting_point]
    while starting_point in graph:
        stop = graph[starting_point]
        itinery.append(stop)
        starting_point = stop                
    return itinery




if __name__ == "__main__":
    print("-------- # Session 1: Graphs -------- ")
    print("------ # Standard Problem Set Version 1 ------ ")
    print("Problem 1: Graphing Flights")
    print(list(flights.keys()))
    print(list(flights.values()))
    print(flights["JFK"])
    print()
    print("Problem 2: There and Back")
    flights1 = [[1, 2], [0], [0, 3], [2]]
    flights2 = [[1, 2], [], [0], [2]]
    print(bidirectional_flights(flights1))
    print(bidirectional_flights(flights2))
    print()
    print("Problem 3: Finding Direct Flights")
    flights = [
            [0, 1, 1, 0],
            [1, 0, 0, 0],
            [1, 1, 0, 1],
            [0, 0, 0, 0]]
    print(get_direct_flights(flights, 2))
    print(get_direct_flights(flights, 3))
    print()
    print('Problem 4: Converting Flight Representations')
    flights = [['Cape Town', 'Addis Ababa'], ['Cairo', 'Lagos'], ['Lagos', 'Addis Ababa'], 
            ['Nairobi', 'Cairo'], ['Cairo', 'Cape Town']]
    print(get_adj_dict(flights))
    print()
    print('Problem 5: Find Center of Airport')
    terminals1 = [[1,2],[2,3],[4,2]]
    terminals2 = [[1,2],[5,1],[1,3],[1,4]]
    print(find_center(terminals1))
    print(find_center(terminals2))
    print()
    print('Problem 6: Finding All Reachable Destinations')
    flights = {
    "Tokyo": ["Sydney"],
    "Sydney": ["Tokyo", "Beijing"],
    "Beijing": ["Mexico City", "Helsinki"],
    "Helsinki": ["Cairo", "New York"],
    "Cairo": ["Helsinki", "Reykjavik"],
    "Reykjavik": ["Cairo", "New York"],
    "Mexico City": ["Sydney"]   
    }
    print(get_all_destinations_bfs(flights, "Beijing"))
    print(get_all_destinations_bfs(flights, "Helsinki"))
    print()
    print('Problem 7: Finding All Reachable Destinations II')
    flights = {
        "Tokyo": ["Sydney"],
        "Sydney": ["Tokyo", "Beijing"],
        "Beijing": ["Mexico City", "Helsinki"],
        "Helsinki": ["Cairo", "New York"],
        "Cairo": ["Helsinki", "Reykjavik"],
        "Reykjavik": ["Cairo", "New York"],
        "Mexico City": ["Sydney"]   
    }
    print(get_all_destinations_dfs(flights, "Beijing"))
    print(get_all_destinations_dfs(flights, "Helsinki"))
    print()
    print('Problem 8: Find Itinerary')
    boarding_passes_1 = [
                        ("JFK", "ATL"),
                        ("SFO", "JFK"),
                        ("ATL", "ORD"),
                        ("LAX", "SFO")]

    boarding_passes_2 = [
                        ("LAX", "DXB"),
                        ("DFW", "JFK"),
                        ("LHR", "DFW"),
                        ("JFK", "LAX")]
    print(find_itinerary(boarding_passes_1))
    print(find_itinerary(boarding_passes_2))
    print()


