def initialize_adjacency_matrix(num_vertices):
    """Initializes an adjacency matrix with zeros."""
    return [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]

    flights = {
        "LAX":["JFK"],
        "JFK":["LAX", "DFW"],
        "DFW":["JFK", "ATL"],
        "ATL":["DFW"],
    }
    # print(list(flights.keys()))
    # print(list(flights.values()))
    # print(flights["JFK"])

def bidirectional_flights(flights):
    adj = [[0 for x in range(len(flights))] for y in range(len(flights))]
    
    for i, flight in enumerate(flights):
        for j, dest in enumerate(flight):
            adj[i][flights[i][j]] = 1
            
            
    for i, flight in enumerate(flights):
        for j, dest in enumerate(flight):
            if adj[i][j] != adj[j][i]:
                return False
    
    return True
flights1 = [[1, 2], [0], [0, 3], [2]]
flights2 = [[1, 2], [], [0], [2]]

# print(bidirectional_flights(flights1))
# print(bidirectional_flights(flights2))

def get_direct_flights(flights, source):
    res = []
    
    for i in range(len(flights[source])):
        if flights[source][i]:
            res.append(i)
            
    return res

flights = [
            [0, 1, 1, 0],
            [1, 0, 0, 0],
            [1, 1, 0, 1],
            [0, 0, 0, 0]]

print(get_direct_flights(flights, 2))
print(get_direct_flights(flights, 3))