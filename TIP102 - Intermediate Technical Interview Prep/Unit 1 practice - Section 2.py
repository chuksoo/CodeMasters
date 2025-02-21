# Session 2: Strings & Arrays
# Standard Problem Set Version 1

# def delete_minimum_elements(hunny_jar_sizes):
# 	result = []
# 	min_elem = min(hunny_jar_sizes)
# 	while len(hunny_jar_sizes) != 0:
# 		min_elem = min(hunny_jar_sizes)
# 		result.append(min_elem)
# 		hunny_jar_sizes.remove(min_elem)
# 	return result


# hunny_jar_sizes = [5, 3, 2, 4, 1]
# print(delete_minimum_elements(hunny_jar_sizes))
# hunny_jar_sizes = [5, 2, 1, 8, 2]
# print(delete_minimum_elements(hunny_jar_sizes))

#def sum_of_digits(num):
#     sum = 0
#     strg = str(num)
#     for val in strg:
#         sum += int(val)
#     return sum
      
# num = 423
# print(sum_of_digits(num))
# num = 4
# print(sum_of_digits(num))

def final_value_after_operations(operations):
    tigger = 1
    for strg in operations:
        if strg == "bouncy" or strg == "flouncy":
            tigger += 1
        elif strg == "trouncy" or strg == "pouncy":
            tigger -= 1
    return tigger

operations = ["trouncy", "flouncy", "flouncy"]
print(final_value_after_operations(operations))
operations = ["bouncy", "bouncy", "flouncy"]
print(final_value_after_operations(operations))
