# # Problem1
# from collections import deque
# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def print_tree(root):
#     if not root:
#         return []

#     queue = deque([root])
#     output = []

#     while queue:
#         curr = queue.popleft()
#         output.append(curr.val)

#         if curr.left:
#             queue.append(curr.left)
#         if curr.right:
#             queue.append(curr.right)
    
#     return output

# root = TreeNode("Trunk")
# root.left = TreeNode("Mcintosh")
# root.right = TreeNode("Granny Smith")

# root.left.left = TreeNode("Fuji")
# root.left.right = TreeNode("Opal")

# root.right.left = TreeNode("Crab")
# root.right.right = TreeNode("Gala")

# # Using print_tree() included at the top of this page
# print(print_tree(root))

# Problem2
# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def calculate_yield(root):
#     if root.val == "+":
#         return root.left.val + root.right.val
#     elif root.val == "-":
#         return root.left.val - root.right.val
#     elif root.val == "*":
#         return root.left.val * root.right.val
#     elif root.val == "/":
#         return root.left.val / root.right.val
#     else: 
#         return None

# apple_tree = TreeNode("+", TreeNode(7), TreeNode(5))

# print(calculate_yield(apple_tree))

#Probme 3
# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def right_vine(root):
#     if root is None:
#         return []
    
#     if root.left is None and root.right is None:
#         return [root.val]
    
#     result = [root.val]
#     while root.right is not None:
#         result.append(root.right.val)
#         root = root.right
#     return result

# """
#         Root
#       /      \
#     Node1    Node2
#   /         /    \
# Leaf1    Leaf2  Leaf3
# """

# ivy1 = TreeNode("Root", 
#                 TreeNode("Node1", TreeNode("Leaf1")),
#                 TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

# ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

# print(right_vine(ivy1))
# print(right_vine(ivy2))

# # Problem 4
# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def right_vine(root):
#     if root is None:
#         return []
    
#     root.left = None
#     right_val = right_vine(root.right)

#     return [root.val] + right_val

# """
#         Root
#       /      \
#     Node1    Node2
#   /         /    \
# Leaf1    Leaf2  Leaf3
# """
# ivy1 = TreeNode("Root", 
#                 TreeNode("Node1", TreeNode("Leaf1")),
#                 TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

# """
#       Root
#       /  
#     Node1
#     /
#   Leaf1  
# """
# ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

# print(right_vine(ivy1))
# print(right_vine(ivy2))

# Problem 5
# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def count_leaves(root):
#     if root is None:
#         return 0
#     if root.left is None and root.right is None:
#         return 1
#     return count_leaves(root.left) + count_leaves(root.right)

# """
#         Root
#       /      \
#     Node1    Node2
#   /         /    \
# Leaf1    Leaf2  Leaf3
# """

# oak1 = TreeNode("Root", 
#                 TreeNode("Node1", TreeNode("Leaf1")),
#                 TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

# """
#       Root
#       /  
#     Node1
#     /
#   Leaf1  
# """
# oak2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))


# print(count_leaves(oak1))
# print(count_leaves(oak2))

# Problem 6
# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def survey_tree(root):
#     postorder_dfs = []

#     if root:
#         postorder_dfs = postorder_dfs + survey_tree(root.left)
#         postorder_dfs = postorder_dfs + survey_tree(root.right)
#         postorder_dfs.append(root.val)
#     return postorder_dfs


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

# Problem 7
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def harvest_berries(root, threshold):
    if root is None:
        return 0

    total = 0

    if root.val > threshold:
        total += root.val
    
    total += harvest_berries(root.right, threshold)
    total += harvest_berries(root.left, threshold)

    return total


"""
       4
     /   \
   10     6
  /  \     \
 5    8    20
"""
bush = TreeNode(4, TreeNode(10, TreeNode(5), TreeNode(8)), TreeNode(6, None, TreeNode(20)))

print(harvest_berries(bush, 6))
print(harvest_berries(bush, 30))