def find_task_pair(task_times, available_time):
    task_times = sorted(task_times)
    left, right = 0, len(task_times) - 1
    while left < right:
        current_time = task_times[left] + task_times[right]
        if current_time == available_time:
            return True
        elif current_time < available_time:
            left += 1
        else:
            right -= 1
    return False


task_times = [30, 45, 60, 90, 120]
available_time = 105
print(find_task_pair(task_times, available_time))

task_times_2 = [15, 25, 35, 45, 55]
available_time = 100
print(find_task_pair(task_times_2, available_time))

task_times_3 = [20, 30, 50, 70]
available_time = 60
print(find_task_pair(task_times_3, available_time))