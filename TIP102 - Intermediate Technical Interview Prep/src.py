# '''
# You are grafting different varieties of apple onto the same root tree can produce many different varieties of apples! Given the following TreeNode class, create the binary tree depicted below. The text representing each node should should be used as the value.

# The root, or topmost node in the tree TreeNode("Trunk") has been provided for you.
# '''
# from collections import deque 

# Tree Node class
# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def print_tree(root):
#     if not root:
#         return "Empty"
#     result = []
#     queue = deque([root])
#     while queue:
#         node = queue.popleft()
#         if node:
#             result.append(node.val)
#             queue.append(node.left)
#             queue.append(node.right)
#         else:
#             result.append(None)
#     while result and result[-1] is None:
#         result.pop()
#     print(result)

# root = TreeNode("Trunk")
# root.left = TreeNode('Mcintosh')
# root.right = TreeNode('Granny Smith')
# root.left.left = TreeNode('Fuji')
# root.left.right = TreeNode('Opal')
# root.right.left = TreeNode('Crab')
# root.right.right = TreeNode('Gala')

# print_tree(root)

#----------------------------
#problem 2
#plan - use four if conditions to see which operation we're using
#depending on the operation, + - * / the nodes.
# def calculate_yield(root):

#     if root.val == "+":
#         return root.left.val + root.right.val
#     elif root.val == "-":
#         return root.left.val - root.right.val
#     elif root.val == "*":
#         return root.left.val * root.right.val
#     else:
#         return root.left.val / root.right.val

# apple_tree = TreeNode("+", TreeNode(7), TreeNode(5))
# print(calculate_yield(apple_tree))
#-------------------------------------
#problem 3

#PLAN
#empty list to store nodes
#start at root
#keep returning the right nodes

# def right_vine(root):
#     # if not root:
#     #   return None
  
#     # rightNodes.append(root.val)
#     # right_vine(root.right, rightNodes)
#     # return rightNodes
#     rightNodes = []
    
#     while root:
#         rightNodes.append(root.val)
#         root = root.right
#     return rightNodes
    

# ivy1 = TreeNode("Root", 
#                 TreeNode("Node1", TreeNode("Leaf1")),
#                 TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

# ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))



# # print(right_vine(ivy1))
# print(right_vine(ivy2))
#--------------------------
#problem 5
#PLAN
#if no root, return 0
# if root.left then go left
# if root.right then go right
# """
#         Root
#       /      \
#     Node1    Node2
#   /         /    \
# Leaf1    Leaf2  Leaf3
# """

# def count_leaves(root):
#     #if root is none
#     if not root:
#         return 0
    
#     if not root.left and not root.right:
#         return 1 
    
#     return count_leaves(root.left) + count_leaves(root.right)

# oak1 = TreeNode("Root", 
#                 TreeNode("Node1", TreeNode("Leaf1")),
#                 TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

# oak2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))
# oak3 = None


# print(count_leaves(oak1))
# print(count_leaves(oak2))
#---------------------------------

#PLAN
#IF not root return none
#pass a list
#appending left subtree
#append right subtree
#return list


# def survey_tree(root, lst=[]):
#     if not root:
#         return None

#     survey_tree(root.left)
#     survey_tree(root.right)
#     lst.append(root.val)
    
#     return lst


# """
#         Root
#       /      \
#     Node1    Node2
#   /         /    \
# Leaf1    Leaf2  Leaf3
# """

# magnolia = TreeNode("Root", 
#                 TreeNode("Node1", TreeNode("Leaf1")),
#                 TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

# print(survey_tree(magnolia))
#-----------------------------
#problem 7

#PLAN
# IF current node is none, return 0

# def harvest_berries(root, threshold):
#     if not root:
#         return 0
    
#     cur = 0
#     if root.val > threshold:
#         cur = root.val
#     else:
#         cur = 0

#     return harvest_berries(root.left, threshold) + cur + harvest_berries(root.right, threshold)
    

# """
#        4
#      /   \
#    10     6
#   /  \     \
#  5    8    20
# """
# bush = TreeNode(4, TreeNode(10, TreeNode(5), TreeNode(8)), TreeNode(6, None, TreeNode(20)))

# print(harvest_berries(bush, 6))
# print(harvest_berries(bush, 30))




from collections import deque 

# Tree Node class
class TreeNode:
  def __init__(self, value, key=None, left=None, right=None):
      self.key = key
      self.val = value
      self.left = left
      self.right = right

def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root





def count_odd_splits(root):
    if not root:
        return 0
    
    if root.val % 2 != 0:
        return 1 + count_odd_splits(root.left) + count_odd_splits(root.right)
    else:
        return count_odd_splits(root.left) + count_odd_splits(root.right)
    



values = [2, 3, 5, 6, 7, None, 12]
monstera = build_tree(values)

# print(count_odd_splits(monstera))
# print(count_odd_splits(None))

def find_flower(inventory, name):
    if not inventory:
        return False
    
    if name == inventory.val:
        return True
    
    if inventory.val[0] > name[0]:
        return find_flower(inventory.left, name)
    else:
        return find_flower(inventory.right, name)



def non_bst_find_flower(root, name):
    if root is None:
        return False
    
    if root.val == name:
        return True

    return non_bst_find_flower(root.left, name) or non_bst_find_flower(root.right, name)
    




"""
          Rose
         /    \
      Lilac  Tulip
      /  \       \
   Daisy Lily   Violet
"""

# using build_tree() function at top of page
# values = ["Rose", "Lilac", "Tulip", "Daisy", "Lily", None, "Violet"]
# garden = build_tree(values)

# print(find_flower(garden, "Lilac"))  
# print(find_flower(garden, "Sunflower")) 


values = ["Rose", "Lily", "Tulip", "Daisy", "Lilac", None, "Violet"]
garden = build_tree(values)

# print(non_bst_find_flower(garden, "Lilac"))  
# print(non_bst_find_flower(garden, "Sunflower"))



def add_plant(collection, name):
    if not collection.left and name[0] < collection.val[0]:
        collection.left = TreeNode(name)
        return collection
    elif not collection.right and name[0] > collection.val[0]:
        collection.right = TreeNode(name)
        return collection
    
    if name[0] < collection.val[0]:
        return add_plant(collection.left, name)
    else:
        return add_plant(collection.right, name)
        

"""

            Money Tree
        /              \
Fiddle Leaf Fig    Snake Plant
    /
aloe     
"""

# Using build_tree() function at the top of page
values = ["Money Tree", "Fiddle Leaf Fig", "Snake Plant"]
collection = build_tree(values)

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)

# Using print_tree() function at the top of page
print_tree(add_plant(collection, "Aloe"))
print_tree(add_plant(collection, "Zebra"))