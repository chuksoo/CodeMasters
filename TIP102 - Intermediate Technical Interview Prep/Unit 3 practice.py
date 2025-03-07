# Session 2: Stacks, Queues, and Two Pointer
# Standard Problem Set Version 1

import math
from collections import deque

'''Problem 1: Manage Performance Stage Changes
At a cultural festival, multiple performances are scheduled on a single stage. However, due to last-minute changes, 
some performances need to be rescheduled or canceled. The festival organizers use a stack to manage these changes efficiently.

You are given a list changes of strings where each string represents a change action. The actions can be:

"Schedule X": Schedule a performance with ID X on the stage.
"Cancel": Cancel the most recently scheduled performance that hasn't been canceled yet.
"Reschedule": Reschedule the most recently canceled performance to be the next on stage.
Return a list of performance IDs that remain scheduled on the stage after all changes have been applied.'''
def manage_stage_changes(changes):
    stack = []
    cancelled_stack = []
    for schedule in changes:
        if 'Schedule' in schedule:
            change, id = schedule.split()
            stack.append(id)
        elif schedule == 'Cancel':
            if stack:
                cancelled_stack.append(stack.pop())
        elif schedule == 'Reschedule':
            if cancelled_stack:
                stack.append(cancelled_stack.pop())
    return stack

'''Problem 2: Queue of Performance Requests
You are organizing a festival and want to manage the queue of requests to perform. Each request has a priority. 
Use a queue to process the performance requests in the order they arrive but ensure that requests with higher priorities are processed before those with lower priorities. 
Return the order in which performances are processed.
'''
import heapq
def process_performance_requests(requests):
    priority_queue = []

    for request_number, (priority, performance) in enumerate(requests):
        heapq.heappush(priority_queue, (-priority, request_number, performance))

    order = []
    while priority_queue:
        priority, request_number, performance = heapq.heappop(priority_queue)
        print(f'Processing {performance} with priority {-priority}')
        order.append(performance)

    return order

    


    


'''Problem 3: Collecting Points at Festival Booths
At the festival, there are various booths where visitors can collect points. Each booth has a specific number of points available. 
Use a stack to simulate the process of collecting points and return the total points collected after visiting all booths.
'''
def collect_festival_points(points):
    collecting_points = []
    for point in points:
        collecting_points.append(point)
    return sum(collecting_points)

'''Problem 4: Festival Booth Navigation
At the cultural festival, you are managing a treasure hunt where participants need to visit booths in a specific order. 
The order in which they should visit the booths is defined by a series of clues. However, some clues lead to dead ends, 
and participants must backtrack to previous booths to continue their journey.

You are given a list of clues, where each clue is either a booth number (an integer) to visit or the word "back" indicating that 
the participant should backtrack to the previous booth.

Write a function to simulate the participant's journey and return the final sequence of booths visited, in the order they were visited.'''

def booth_navigation(clues):
    clues_stack = []
    for item in clues:
        if item != 'back':
            clues_stack.append(item)
        else:
            if clues_stack:
                clues_stack.pop()
            else:
                pass
    return clues_stack

'''Problem 5: Merge Performance Schedules
You are organizing a cultural festival and have two performance schedules, schedule1 and schedule2, 
each represented by a string where each character corresponds to a performance slot. 
Merge the schedules by adding performances in alternating order, starting with schedule1. 
If one schedule is longer than the other, append the additional performances onto the end of the merged schedule.

Return the merged performance schedule.'''

def merge_schedules(schedule1, schedule2):
    schedule1, schedule2 = list(schedule1), list(schedule2)
    result = []
    ptr_one = ptr_two = 0
    while ptr_one < len(schedule1) and ptr_two < len(schedule2):
        result.append(schedule1[ptr_one])
        result.append(schedule2[ptr_two])
        ptr_one += 1
        ptr_two += 1
    if len(schedule1) > len(schedule2):
        result += schedule1[ptr_one:]
    else:
        result += schedule2[ptr_two:]
    return ''.join(result)


if __name__ == "__main__":
    print("-------- # Session 2: Stacks, Queues, and Two Pointer -------- ")
    print("------ # Standard Problem Set Version 1 ------ ")
    print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))  
    print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"])) 
    print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"])) 
    print()
    print(process_performance_requests([(3, 'Dance'), (5, 'Music'), (1, 'Drama')]))
    print(process_performance_requests([(2, 'Poetry'), (1, 'Magic Show'), (4, 'Concert'), (3, 'Stand-up Comedy')]))
    print(process_performance_requests([(1, 'Art Exhibition'), (3, 'Film Screening'), (2, 'Workshop'), (5, 'Keynote Speech'), (4, 'Panel Discussion')]))
    print()
    print(collect_festival_points([5, 8, 3, 10])) 
    print(collect_festival_points([2, 7, 4, 6])) 
    print(collect_festival_points([1, 5, 9, 2, 8])) 
    print()
    clues = [1, 2, "back", 3, 4]
    print(booth_navigation(clues)) 
    clues = [5, 3, 2, "back", "back", 7]
    print(booth_navigation(clues)) 
    clues = [1, "back", 2, "back", "back", 3]
    print(booth_navigation(clues)) 
    print()
    print(merge_schedules("abc", "pqr")) 
    print(merge_schedules("ab", "pqrs")) 
    print(merge_schedules("abcd", "pq")) 
    print()
