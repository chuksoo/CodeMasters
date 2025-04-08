

''''''
def find_cruise_length(cruise_lengths, vacation_length):
    # if list is empty, return False
    if not cruise_lengths:
        return False

    # define two pointer low and high
    low, high = 0, len(cruise_lengths) - 1
    # while loop
    while low <= high:
        # get middle of the list
        mid_point = (low + high) // 2
        if cruise_lengths[mid_point] == vacation_length:
            return True
        # perform binary search
        elif cruise_lengths[mid_point] > vacation_length:
            high = mid_point - 1
        else:
            low = mid_point + 1
    return False

print(find_cruise_length([9, 10, 11, 12, 13, 14, 15], 13))
print(find_cruise_length([8, 9, 12, 13, 13, 14, 15], 11))
print()

def find_cabin_index(cabins, preferred_deck):
    # if list is empty, return 0
    if not cabins:
         return 0
    
    n = len(cabins)
    return recursive_binary_search(cabins, 0, n, preferred_deck)
    
def recursive_binary_search(arr, low, high, target):
    if high > low:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return recursive_binary_search(arr, low, mid - 1, target)
        else:
            return recursive_binary_search(arr, mid + 1, high, target)
    elif high == low:
        return low
 
print(find_cabin_index([1, 3, 5, 6], 5)) # 2  low=0, high = 4 mid = 2 
print(find_cabin_index([1, 3, 5, 6], 2)) # 1  low=0, high = 4 mid = 2  call2:low=0, high =1 mid =0 call3: low=1, high =1 mid =1 call4:l=1,h=0
print(find_cabin_index([1, 3, 5, 6], 7)) # 4
print()

def count_checked_in_passengers(rooms):
    low, high = 0, len(rooms) - 1
    # calculate mid point
    while low <= high:
        mid = (low + high) // 2
        # if element at mid point is a 1
        if rooms[mid] == 0:
            # update low
            low = mid + 1
        else:
            high = mid - 1
       
    return len(rooms) - low

rooms1 = [0, 0, 0, 1, 1, 1, 1]
rooms2 = [0, 0, 0, 0, 0, 1]
rooms3 = [0, 0, 0, 0, 0, 0]

print(count_checked_in_passengers(rooms1))  # 4
print(count_checked_in_passengers(rooms2))  # 1
print(count_checked_in_passengers(rooms3))  # 0


def is_profitable(excursion_counts):
    pass

print(is_profitable([3, 5, 6, 8, 9, 12])) # 6 excursions
print(is_profitable([0, 0]))
print(0 // 2)