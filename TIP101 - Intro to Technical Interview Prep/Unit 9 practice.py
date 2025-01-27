"""
Unit 9: Advanced Binary Trees
Session 1: Binary Trees
"""
# BST search code:
class TreeNode:
    def __init__(self, key, left = None, right = None):
        self.left = left
        self.right = right
        self.val = key

def search(root, target):
  if root:
    print(f"Checking node with value: {root.val}")
  else:
    print("Reached a None node")

  if root is None or root.val == target:
    if root:
      print(f"Found node with value: {root.val}")
    else:
      print(f"Value {target} not found in the tree.")
    return root

  if target < root.val:
    print(f"Going left from node with value: {root.val}")
    return search(root.left, target)

  print(f"Going right from node with value: {root.val}")
  return search(root.right, target)

root = TreeNode(50)
root.left = TreeNode(30)
root.right = TreeNode(70)
root.left.left = TreeNode(20)
root.left.right = TreeNode(40)
root.right.left = TreeNode(60)
root.right.right = TreeNode(80)

target = 40
found_node = search(root, target)
print(found_node.val)
print()

# traversal code:
def inorderTraversal(root):
  result = []

  if root:
    print(f"Traversing left subtree of node with value {root.val}")
    result = inorderTraversal(root.left)

    print(f"Visiting node with value {root.val}")
    result.append(root.val)

    print(f"Traversing right subtree of node with value {root.val}")
    result = result + inorderTraversal(root.right)

  return result

def preorderTraversal(root):
  result = []

  if root:
    print(f"Visiting node with value {root.val}")
    result.append(root.val)

    print(f"Traversing left subtree of node with value {root.val}")
    result = result + preorderTraversal(root.left)

    print(f"Traversing right subtree of node with value {root.val}")
    result = result + preorderTraversal(root.right)

  return result

"""Problem Set Version 1
Problem 1: Is Symmetric Tree
Given the root of a binary tree, return True if the tree’s left and right subtrees are mirrors of each other (i.e., tree is symmetric around its center). Return False otherwise.

Evaluate the time complexity of your function."""
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def is_symmetric(root):
  if not root: 
    return True
  return helper(root.left, root.right)

def helper(left, right):
  if not left and not right:
    return True
  if not left or not right:
    return False
  if left.val != right.val:
     return False
  return helper(left.left, right.right) and helper(left.right, right.left)

# Case 1
head = TreeNode(1)
head.left = TreeNode(2)
head.right = TreeNode(2)
head.left.left = TreeNode(3)
head.left.right = TreeNode(4)
head.right.left = TreeNode(4)
head.right.right = TreeNode(3)
print(is_symmetric(head))

# Case 2
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.right = TreeNode(3)
root.right.right = TreeNode(3)
print(is_symmetric(root))
print()

"""Problem 2: Root-to-Leaf Paths
Given the root of a binary tree, return a list of all root-to-leaf paths in any order.
A leaf is a node with no children. Evaluate the time complexity of your function."""

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def binary_tree_paths(root):
    if root is None:
        return []
        
    if not root.left and not root.right:
        return [str(root.val)]

    paths = []
    if root.left:
        for path in binary_tree_paths(root.left):
            paths.append(f"{root.val}->{path}")
    if root.right:
        for path in binary_tree_paths(root.right):
            paths.append(f"{root.val}->{path}")
    return paths

# Case 1
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
print(binary_tree_paths(root)) # Expected Output: ["1->2->5", "1->3"]

# Case 2
root = TreeNode(1)
print(binary_tree_paths(root)) # Expected Output: ["1"]
print()
    
"""Problem 3: Minimum Difference in BST
Given the root of a binary search tree, return the minimum difference between the values of any two different nodes in the tree.

Evaluate the time complexity of your function."""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def helper(node, prev_val, min_distance):
    if not node:
        return min_distance

    min_distance = helper(node.left, prev_val, min_distance)
    if prev_val:
        min_distance = min(min_distance, node.val - prev_val)
    prev_val = node.val
    min_distance = helper(node.right, prev_val, min_distance)
    return min_distance
    
def min_diff_in_bst(root):
    return helper(root, float('-inf'), float('inf'))

# Case 1:
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
print(min_diff_in_bst(root)) # Expected Output: 1, The smallest difference between any two nodes is 1 (2 - 1 = 1, 3 - 2 = 1)

# Case 2 
root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(48)
root.right.left = TreeNode(12)
root.right.right = TreeNode(49)
print(min_diff_in_bst(root)) # Expected Output: 1, The smallest difference between any two nodes is 1 (1 - 0 = 1)
print()

"""Problem 4: Increasing Order Search Tree
Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node of the tree is now the root of tree and every node has no left child and only one right child.

Return the root of the modified tree. Evaluate the time complexity of your function."""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def increasing_bst(root):
    def inorder_traversal(node):
        nonlocal current
        if node is None:
            return

        # traverse left subtree
        inorder_traversal(node.left)

        # process current node
        node.left = None
        current.right = node 
        current = node

        # traverse right subtree
        inorder_traversal(node.right)
        
    # initialize a dummy node to build new tree
    dummy = TreeNode(0)
    # keep track of current node in new tree
    current = dummy

    # start the inorder traversal
    inorder_traversal(root)

    # return the root of the new tree
    return dummy.right
    
# Helper function to print the tree in-order
def print_tree(root):
    if not root:
        return
    print(root.val, end=" ")
    print_tree(root.left)
    print_tree(root.right)

# Case 1
root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(7)
print("Original tree:")
print_tree(root)
print()

new_root = increasing_bst(root)
print("Modified tree:")
print_tree(new_root)
print()

# Case 2
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(8)
root.left.left.left = TreeNode(1)
root.right.right.left = TreeNode(7)
root.right.right.right = TreeNode(9)
print()
print("Original tree:")
print_tree(root)
print()

new_root = increasing_bst(root)
print("Modified tree:")
print_tree(new_root)
print()

"""Problem 5: Equal Tree Split
Given the root of a binary tree, return True if removing an edge between two nodes can split the tree into two trees with an equal number of nodes. Return False otherwise.

Evaluate the time complexity of the function."""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def can_split(root):
    if not root:
        return False

    # Function to calculate total number of nodes in the tree
    def calculate_total_nodes(node):
        if not node:
            return 0
        return 1 + calculate_total_nodes(node.left) + calculate_total_nodes(node.right)

    total_nodes = calculate_total_nodes(root)

    # If total number of nodes is odd, can't split into equal halves
    if total_nodes % 2 != 0:
        return False

    target = total_nodes // 2
    result = [False]  # Use a list to capture result in the inner function

    # Post-order traversal to find the size of each subtree
    def post_order(node):
        if not node:
            return 0

        left_size = post_order(node.left)
        right_size = post_order(node.right)

        # Current subtree size
        subtree_size = left_size + right_size + 1

        # Check if the current subtree can form one half
        if subtree_size == target:
            result[0] = True

        return subtree_size

    post_order(root)
    return result[0]

# Case 1
print()
print("Equal Tree Split")
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(7)
print(can_split(root)) # Expected Output: True

# Case 2
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
print(can_split(root)) # Expected Output: False
print()

print("********* Session 2: Binary Trees Essentials **********")
"""
Problem Set Version 1

Problem 1: Level Order Traversal of Binary Tree
Given the following pseudocode and the root of a binary tree, return a list of the level order traversal of it’s nodes’ values (i.e., from left to right, level by level).

Evaluate the time complexity of your solution. Define your variables and give a rationale as to why you believe your solution has the stated time complexity.
"""
from collections import deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def level_order(root):
    # If the tree is empty, return an empty list
    if not root:
        return []

    # Create an empty queue using deque
    queue = deque() 
    # Create an empty list to store the explored nodes
    level_order = []
    # Add the root to the queue
    queue.append(root)
    
    # While the queue is not empty:
    while queue:
        # Pop the next node off the queue (pop from the left side!)
        node = queue.popleft()
        # Add the popped node to the list of explored nodes
        level_order.append(node.val)
        # Add each of the popped node's children to the end of the queue
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    # Return the list of visited nodes
    return level_order

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
print("Level Order Traversal of Binary Tree")
print(level_order(root)) # Expected Output: [4, 2, 6, 1, 3]
print()

"""Problem 2: Find Minimum Depth of Binary Tree
Given the root of a binary tree, return its minimum depth. The minimum depth is the number of nodes along the shortest path from the root down to the nearest leaf node.

Evaluate the time complexity of your solution. Define your variables and give a rationale as to why you believe your solution has the stated time complexity."""

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def min_depth(root):
    """
    # Using BFS
    # Understand
        - what should be the return value if node is none
        - can we implement it using inordal traversal
    # Plan
        - find minimum in left node
        - repeat for right node
        - get the node with lowest depth
    # Implement

    # if node is null, return 0
    if root is None:
        return 0

    # if there is no left or right subtree, return 1
    if root.left is None and root.right is None:
        return 1

    # if left node is none, return 1 plus recursive call to right node
    if root.left is None:
        return 1 + min_depth(root.right)

    # if right node is none, return 1 plus recursive call to left node
    elif root.right is None:
        return 1 + min_depth(root.left)
    # return 1 plus min(recursive call to left node, recursive call to right node)
    return 1 + min(min_depth(root.left), min_depth(root.right))
    """
    # Using DFS
    # if node is null, return 0
    if root is None:
        return 0

    # create empty queue
    queue = deque()

    # enqueueing the root node with a depth of 1
    queue.append((root, 1))

    # while the queue is not empty, dequeue a node and its depth.
    while queue:
        node, depth = queue.popleft()
        # If node is a leaf (has no children), we've found the minimum depth, so we return it.
        if node.left is None and node.right is None:
            return depth
        # Otherwise, we enqueue its left and right children (if they exist) with an incremented depth.
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))
    # Continue this process until we find the first leaf node, which will be at the minimum depth.
    # if we exit the while loop without finding a leaf (which shouldn't happen in a valid binary tree), we return -1 to indicate an error.
    return -1

def max_depth(root):
    if root is None:
        return 0

    queue = deque()
    queue.append((root, 1))
    max_depth = 0

    while queue:
        node, depth = queue.popleft()
        
        if node.left is None and node.right is None:
            max_depth = max(max_depth, depth)
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))
    return max_depth
    
# Case 1
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print("Minimum depth:", min_depth(root)) # Expected Output: 2
print("Maximum depth:", max_depth(root)) # Expected Output: 3

# Case 2
root = TreeNode(2)
root.right = TreeNode(3)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(5)
root.right.right.right.right = TreeNode(6)
print("Minimum depth:", min_depth(root)) # Expected Output: 5
print("Maximum depth:", max_depth(root)) # Expected Output: 5
# Expected Output: 5
# Shortest path from root node to a leaf node is 2 -> 3 -> 4 -> 5 -> 6. Number of nodes in path is 5.

# Case 3
root = None
print("Minimum depth:", min_depth(root)) # Expected Output: 0
print("Maximum depth:", max_depth(root)) # Expected Output: 0

# Case 4
root = TreeNode(2)
print("Minimum depth:", min_depth(root)) # Expected Output: 1
print("Maximum depth:", max_depth(root)) # Expected Output: 1
print()

"""Problem 3: Odd-Even Level Sum Difference in Binary Tree
Given the root of a binary tree, return the difference between the sum of all node values in odd levels and sum of all node values in even levels.

Evaluate the time complexity of your solution. Define your variables and give a rationale as to why you believe your solution has the stated time complexity."""

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def level_difference(root):
    if not root:
        return 0

    queue = deque([root])
    level = 1
    odd_sum = 0
    even_sum = 0

    while queue:
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()

            if level % 2 == 1:
                odd_sum += node.val
            else:
                even_sum += node.val

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        level += 1

    return odd_sum - even_sum

# Case 1
root = TreeNode(6)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(5)
root.right.left = TreeNode(4)
root.right.right = TreeNode(2)
root.right.left.left = TreeNode(1)
root.right.left.right = TreeNode(7)
root.right.right.right = TreeNode(3)
print(level_difference(root)) # Expected Output: -5
# Odd level sum: 6 + 5 + 4 + 2 = 17
# Even level sum: 3 + 8 + 1 + 7 + 3 = 22
# Odd level sum - even level sum: 17 - 22 = -5
print()

"""Problem 4: Level Order Traversal of Binary Tree with Nested Lists
Given the root of a binary tree, write a function level_order() that returns the level order traversal of its nodes’ values (i.e., from left to right, level by level). level_order() should return a list of lists, where each inner list contains the node values of a single level in the tree.

Evaluate the time complexity of your solution. Define your variables and give a rationale as to why you believe your solution has the stated time complexity."""

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def level_order(root):
    if not root:
        return []
        
    order_lst = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
    
            if node.left:
                queue.append(node.left)
    
            if node.right:
                queue.append(node.right)
        order_lst.append(current_level)

    return order_lst

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(level_order(root)) # Expected Output: [ [3], [9, 20], [15, 7]]
print()

"""Problem 5: Sum of Binary Tree Node Tilts
Given the root of a binary tree, return the sum of every tree node’s tilt. The tilt of a tree node is the absolute difference between the sum of all left subtree node values and all right subtree node values. If a node does not have a left child, then the sum of the left subtree node values is treated as 0. The rule is similar if the node does not have a right child.

Evaluate the time complexity of your solution. Define your variables and give a rationale as to why you believe your solution has the stated time complexity."""

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def find_tilt(root):
    total_tilt = 0

    def dfs(node):
        nonlocal total_tilt
        if node is None:
            return 0

        left_sum = dfs(node.left)
        right_sum = dfs(node.right)
                       
        node_tilt = abs(left_sum - right_sum)
        total_tilt += node_tilt
        
        return left_sum + right_sum + node.val

    dfs(root)
    return total_tilt

# Case 1
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print(find_tilt(root)) # Expected Output: 1

# Case 2
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(9)
root.left.left = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(7)
print(find_tilt(root)) # Expected Output: 15
print()

"""
Height of a Binary Tree
"""
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def height(root):
    if root is None:
        return 0
    else:
        left_height = height(root.left)
        right_height = height(root.right)
        if left_height > right_height:
            return 1 + left_height
        else:
            return 1 + right_height

root = TreeNode(2)
root.right = TreeNode(3)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(5)
root.right.right.right.right = TreeNode(6)
print("Binary Tree Height:", height(root)) # Expected Output: 5
print()

"""5. Sum of All Left Leaves in Binary Tree
Given the root of a binary tree, return the sum of all left leaves. A leaf is a node with no children. A left leaf is a leaf that is the left child of another node. As such, a tree with only one node has no left leaves."""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sum_left_leaves(root):
    # Write your code here
    left_sum = 0

    if root is None:
        return left_sum

    # Check if the left child is a leaf
    if root.left and not root.left.left and not root.left.right:
        left_sum += root.left.val

    # Recur for left and right subtrees
    left_sum += sum_left_leaves(root.left)
    left_sum += sum_left_leaves(root.right)

    return left_sum

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(sum_left_leaves(root))
print()

"""6. Two Sum increasing_bst
Given the root of a binary search tree and an integer k, return True if there exist two nodes in the BST such that the sum of their values is equal to k, and False otherwise."""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_target(root, k):
    # Write your code here
    def inorder(node, seen):
        if not node:
            return False

        if inorder(node.left, seen):
            return True

        if k - node.val in seen:
            return True
        seen.add(node.val)
        return inorder(node.right, seen)

    seen = set()
    return inorder(root, seen)
    
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)
print(find_target(root, 9))
print(find_target(root, 28))
print()

"""7. Check if Binary Tree is Perfect
Given the root of a binary tree, return True if the binary tree is perfect and False otherwise. A binary tree is perfect if all internal (non-leaf) nodes have two children and all leaves are on the same level."""

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_perfect(root):
    # Write your code here
    if not root:
        return True

    queue = deque([(root, 0)])
    level_of_leaf = None
    while queue:
        node, level = queue.popleft()
        if node.left and node.right:
            queue.append((node.left, level+1))
            queue.append((node.right, level+1))
        elif not node.left and not node.right:
            if level_of_leaf is None:
                level_of_leaf = level
            elif level != level_of_leaf:
                return False
        else:
            return False
    return True

# Case 1
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(8)
print(is_perfect(root))

# Case 2
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
print(is_perfect(root))
print()