# Binary Tree
class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def addNode(root, val):
    if root == None:
        return TreeNode(val)
    else:
        if root.val < val:
            root.right = addNode(root.right, val)
        else:
            root.left = addNode(root.left, val)
    return root

def deleteNode(root, val):
    if root == None:
        return root
    if val < root.val:
        root.left = deleteNode(root.left, val)
    elif val > root.val:
        root.right = deleteNode(root.right, val)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        temp = minValueNode(root.right)
        root.val = temp.val
        root.right = deleteNode(root.right, temp.val)
    return root
    
def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

root = TreeNode(10)        # root node
root.left = TreeNode(5)    # left child of the root
root.right = TreeNode(15)  # right child of the root

addNode(root, 23)
addNode(root, 11)
deleteNode(root, 15)
print()

"""Problem Set Version 1
Problem 1: Build a Binary Tree I
Given the following TreeNode class, create the binary tree depicted in the image below."""
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def print_binary_tree(root):
    from collections import deque
    if not root:
        print("Empty tree")
        return

    queue = deque([(root, 0)])
    current_level = 0
    level_nodes = []

    while queue:
        node, level = queue.popleft()

        if level > current_level:
            print(" ".join(str(n.val) for n in level_nodes))
            level_nodes = []
            current_level = level

        level_nodes.append(node)

        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))

    print(" ".join(str(n.val) for n in level_nodes))


root = TreeNode(10)
node_two = TreeNode(4)
node_three = TreeNode(6)

root.left = node_two    # Node two is the left child of node one
root.right = node_three # Node three is the right child of node one
print_binary_tree(root)
print()


"""Problem 2: 3-Node Sum I
Given the root of a binary tree that has exactly 3 nodes: the root, its left child, and its right child, return True if the value of the root is equal to the sum of the values of its two children. Return False otherwise.

Evaluate the time complexity of your function."""
class TreeNode:
   def __init__(self, val, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def check_tree(root):
  if root is None or root.left is None or root.right is None:
      return False

  return root.val == root.left.val + root.right.val

root = TreeNode(12)
root.left = TreeNode(4)
root.right = TreeNode(8)
print(check_tree(root))  # Should print True
print()

"""Problem 3: 3-Node Sum II
Given the root of a binary tree that has at most 3 nodes: the root, its left child, and its right child, return True if the value of the root is equal to the sum of the values of its two children. Return False otherwise.

Evaluate the time complexity of your function."""
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def check_tree(root):
    if root is None:
        return False

    if root.left is None and root.right is None:
        return True

    if root.left is None:
        return root.val == root.right.val

    if root.right is None:
        return root.val == root.left.val

    return root.val == root.left.val + root.right.val

# Test cases
# Case 1
root = TreeNode(10) 
root.left = TreeNode(10)
print(check_tree(root)) # Expected Output: True

# Case 2
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(2)
print(check_tree(root)) # Expected Output: True

# Case 3
root = TreeNode(5)
root.right = TreeNode(2)
print(check_tree(root)) # Expected Output: False

# Case 4
root = None
print(check_tree(root)) # Expected Output: False
print()

"""Problem 4: Find Leftmost Node I
Given the root of a binary tree, write a function that finds the value of the left most node in the tree.

Evaluate the time complexity of your function."""
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def left_most(root):
    if root is None:
        return None

    # traverse the tree
    while root.left:
        root = root.left
    return root.val

# Case 1
root =TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)

result = left_most(root)
print(result)  # Expected output: 1

# Case 2
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
print(left_most(root)) # Expected Output: 1

# Case 3
root = None
print(left_most(root)) # Expected output: None
print()

"""Problem 5: Find Leftmost Node II
If you implemented the previous left_most() function iteratively, implement it recursively. If you implemented it recursively, implement it recursively.

Evaluate the time complexity of the function."""

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def left_most(root):
    if root is None:
        return None

    if root.left is None:
        return root.val
        
    return left_most(root.left)

# Case 1
root =TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)

result = left_most(root)
print(result)  # Expected output: 1

# Case 2
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
print(left_most(root)) # Expected Output: 1

# Case 3
root = None
print(left_most(root)) # Expected output: None
print()

"""Problem 6: In-order Traversal
Given the root of a binary tree, return a list representing the inorder traversal of its nodes' values. In an inorder traversal we traverse the left subtree, then the current node, then the right subtree."""

class TreeNode():
     def __init__(self, val, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def inorder_traversal(root):
    inorder_dfs = []

    if root:
        inorder_dfs = inorder_dfs + inorder_traversal(root.left)  # traverse the left subtree
        inorder_dfs.append(root.val)                              # visit the root node
        inorder_dfs = inorder_dfs + inorder_traversal(root.right) # traverse the right subtree
    return inorder_dfs

# Case 1
print("In-order traversal of binary tree")
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
print(inorder_traversal(root)) # Expected Output: [1,3,2]

# Case 2
root = None
print(inorder_traversal(root)) # Expected Output: []

# Case 3
root = TreeNode(1)
print(inorder_traversal(root)) # Expected Output: [1]
print()

"""Pre-order Traversal of Binary Tree
Given the root of a binary tree, return a list representing the pre-order traversal of its nodes' values. In a pre-order traversal we visit the root node first, then recursively do a pre-order traversal of the left subtree, followed by recursive pre-order of the right subtree.
"""
class TreeNode():
     def __init__(self, val, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def preorder_traversal(root):
    pre_order_dfs = []

    if root:
        pre_order_dfs.append(root.val)                                 # visit the root node
        pre_order_dfs = pre_order_dfs + preorder_traversal(root.left)  # traverse the left subtree
        pre_order_dfs = pre_order_dfs + preorder_traversal(root.right) # traverse the right subtree
    return pre_order_dfs 
    
# Case 1
print("Pre-order traversal of binary tree")
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
print(preorder_traversal(root)) # Expected Output: [1,3,2]

# Case 2
root = None
print(preorder_traversal(root)) # Expected Output: []

# Case 3
root = TreeNode(1)
print(preorder_traversal(root)) # Expected Output: [1]
print()

"""Problem 7: Binary Tree Size
Given the root of a binary tree, write a function size() that returns the number of nodes in the binary tree.

Evaluate the time complexity of your function."""

class TreeNode():
     def __init__(self, val, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def size(root):
    if root is None:
        return 0
    return 1 + size(root.left) + size(root.right)

# Case 1
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
print(size(root)) # Expected Output: 5

# Case 2
root = None
print(size(root)) # Expected Output: 0
print()

"""Problem 8: Binary Tree Find
Given a value and the root of a tree, write a function find() that returns True if there is a node with the given value in the tree. Assume the tree is balanced.

Evaluate the time complexity of your solution."""

class TreeNode():
     def __init__(self, val, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def find(root, value):
    if root is None:
       return False

    if root.val == value:
        return True
    return find(root.left, value) or find(root.right, value) 
         
# Case 1
value = 5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(4)
root.left.right = TreeNode(3)
print(find(root, value)) # Expected Output: True

# Case 2
value = 10
print(find(root, value)) # Expected Output: False
print()

"""Problem 9: Binary Search Tree Find
Given a value and the root of a binary search tree, write a function find_bst() that returns True if there is a node with the given value in the tree. Assume the tree is balanced."""

class TreeNode():
     def __init__(self, val, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def find_bst(root, value):
    if root is None:
        return False

    if root.val == value:
        return True

    if value < root.val:
        return find_bst(root.left, value)
    else:
        return find_bst(root.right, value)

# Case 1
value = 5
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
print(find_bst(root, value)) # Expected Output: True

# Case 2
value = 10
print(find_bst(root, value)) # Expected Output: False
print()

"""Problem 10: BST Descending Leaves
Given the root of a binary search tree, write a function descending_leaves() that returns a list of the values of all leaves in the BST in descending order. Assume the tree is balanced."""

class TreeNode():
     def __init__(self, val, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def descending_leaves(root):
    # if node is null, return empty list
    if root is None:
        return []

    # if node is leaf node, append its data
    if root.right is None and root.left is None:
        return [root.val]

    # get all right leaf recursively
    right_leaves = descending_leaves(root.right) 

    # get all left leaf recursively
    left_leaves = descending_leaves(root.left)
    return right_leaves + left_leaves

# Case 1
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
print(descending_leaves(root)) # Expected Output: [5, 3, 1]

# Case 2
root = TreeNode(4)
root.right = TreeNode(10)
print(descending_leaves(root)) # Expected Output: [10]
print()

"""Sum of Left Leaves
Given the root of a binary tree, return the sum of all left leaves.
A leaf is a node with no children. A left leaf is a leaf that is the left child of another node."""
class TreeNode():
     def __init__(self, val, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def sumOfLeftLeaves(self, root):
        if root is None:
            return 0

        total = 0
        if root.left is not None and root.left.left is None and root.left.right is None:
            total += root.left.val

        # recursively sum the left leaves from both left and right subtrees
        total += self.sumOfLeftLeaves(root.left)
        total += self.sumOfLeftLeaves(root.right)
        return total 
        
# Case 1
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

solution = Solution()
print(solution.sumOfLeftLeaves(root)) # Expected Output: 24 since 9 + 15 = 24
print()

"""Problem Set Version 2
Problem 1: Build A Binary Tree II
Given the following TreeNode class, create the binary tree that has a root with value 5. The root should have a left child with value 10, and a right child with value 20."""

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

root = TreeNode(5)
root.left = TreeNode(10)
root.right = TreeNode(20)
print_binary_tree(root)
print()

"""Problem 2: 3-Node Product I
Given the root of a binary tree that has exactly 3 nodes: the root, its left child, and its right child, return True if the value of the root is equal to the product of the values of its two children. Return False otherwise.

Evaluate the time complexity of your function."""
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def check_tree(root):
    if root is None:
        return False

    left_val = root.left.val if root.left is not None else 0
    right_val = root.right.val if root.right is not None else 0
    return root.val == left_val * right_val
    
# Case 1
root = TreeNode(10)
root.left = TreeNode(2)
root.right = TreeNode(5)
print(check_tree(root)) # Expected Output: True

# Case 2
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(1)
print(check_tree(root)) # Expected Output: False
print()

"""Problem 3: 3-Node Product II
Given the root of a binary tree that has at most 3 nodes: the root, its left child, and its right child, return True if the value of the root is equal to the product of the values of its two children. Return False otherwise. If the root has only one child, return False.

Evaluate the time complexity of your function."""
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def check_tree(root):
    if root is None:
        return False

    if root.left is None and root.right is None:
        return False
        
    if root.left is None:
        return root.val == root.right.val

    if root.right is None:
        return root.val == root.left.val

    return root.val == root.left.val * root.right.val
    
# Test cases
# Case 1
root = TreeNode(10) 
root.left = TreeNode(10)
print(check_tree(root)) # Expected Output: True

# Case 2
root = TreeNode(6)
root.left = TreeNode(3)
root.right = TreeNode(2)
print(check_tree(root)) # Expected Output: True

# Case 3
root = TreeNode(5)
root.right = TreeNode(2)
print(check_tree(root)) # Expected Output: False

# Case 4
root = None
print(check_tree(root)) # Expected Output: False
print()

"""Problem 4: Find Rightmost Node I
Given the root of a binary tree, write a function that finds the value of the right most node in the tree.

Evaluate the time complexity of your function."""
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def right_most(root):
    # base case: if node is null, return None
    if root is None:
        return None
    # traverse thru with while loop and return value of right root
    while root.right:
        root = root.right
    return root.val
    
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(4)
root.left.right = TreeNode(3)
print(right_most(root)) # Expected Output: 5

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
print(right_most(root)) # Expected Output: 2

# Case 3
root = None
print(right_most(root)) # Expected Output: None
print()

"""Problem 5: Find Rightmost Node II
If you implemented the previous right_most() function iteratively, implement it recursively. If you implemented it recursively, implement it recursively.

Evaluate the time complexity of the function."""
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def right_most(root):
    # base case: if node is null, return None
    if root is None:
        return None
    # recursively traverse the loop and return right val
    if root.right is None:
        return root.val
    return right_most(root.right)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(4)
root.left.right = TreeNode(3)
print(right_most(root)) # Expected Output: 5

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
print(right_most(root)) # Expected Output: 2

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
root.right.right = TreeNode(3)
print(right_most(root)) # Expected Output: 3

# Case 3
root = None
print(right_most(root)) # Expected Output: None
print()

"""Problem 6: Post-order Traversal
Given the root of a binary tree, return a list representing the postorder traversal of its nodes' values. In an postorder traversal we traverse the left subtree, then the right subtree, then the current node.

Evaluate the time complexity of your function."""
class TreeNode():
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def postorder_traversal(root):
    post_order_dfs = []

    if root:
        post_order_dfs = post_order_dfs + postorder_traversal(root.left)  # traverse the left subtree
        post_order_dfs = post_order_dfs + postorder_traversal(root.right) # traverse the right subtree
        post_order_dfs.append(root.val)                                   # visit the root
    return post_order_dfs 

# Case 1
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
print("Post-order traversal of binary tree")
print(postorder_traversal(root)) # Expected Output: [4, 5, 2, 6, 3, 1]

# Case 2
root = None
print(postorder_traversal(root)) # Expected Output: []

# Case 3
root = TreeNode(1)
print(postorder_traversal(root)) # Expected Output: [1]
print()

"""Problem 7: Binary Tree Product
Given the root of a binary tree, write a function that returns the product of all nodes’ values in a binary tree. If the tree is empty, return 1.

Evaluate the time complexity of your function."""
class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right

def product_tree(root):
    product = 1
    if root:
        product *= root.val
        product = product * product_tree(root.left)
        product = product * product_tree(root.right)
    return product
    
# Case 1
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
print("Product of all nodes in binary tree")
print(product_tree(root)) # Expected Output: 120

# Case 2
root = None
print(product_tree(root)) # Expected Output: 1
print()

"""Problem 8: Binary Tree Is Leaf
Given a value and the root of a binary search tree, write a function is_leaf_bst() that returns True if a node with the given value is a leaf node and False otherwise. Assume the tree is balanced.

Evaluate the time complexity of your solution.
"""
class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right

def is_leaf(root, value):
    # Base case: If the tree is empty, return False
    if root is None:
        return False

    # Check if the current node is a leaf node
    if root.left is None and root.right is None:
        return root.val == value

    # Recursively check in the left and right subtrees
    return is_leaf(root.left, value) or is_leaf(root.right, value)
    
# Case 1
value = 5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(4)
root.left.right = TreeNode(3)
print(is_leaf(root, value)) # Expected Output: True

# Case 2
value = 2
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(4)
print(is_leaf(root, value)) # Expected Output: False
print()

"""Problem 9: BST Is Leaf
Given a value and the root of a binary search tree, write a function is_leaf_bst() that returns True if a node with the given value is a leaf node and False otherwise. Assume the tree is balanced.

Evaluate the time complexity of your solution."""
class TreeNode():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_leaf_bst(root, value):
    # Base case: if node is null, return False
    if root is None:
        return False

    # Check if value of the node is equal to the given value
    if root.val == value:
        return True
        
    # recursively check left and right subtree and return true if given value is leaf node else false
    return is_leaf_bst(root.left, value) or is_leaf_bst(root.right, value)

# Case 1
value = 5
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
print(is_leaf_bst(root, value)) # Expected Output: True

# Case 2
value = 10
print(is_leaf_bst(root, value)) # Expected Output: False
print()

"""Problem 10: BST Is Full
Given the root of a binary search tree, write a function is_full_tree() that returns True if the tree is full and False otherwise. A binary tree is full if every node has either zero or two children."""
class TreeNode():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_full_tree(root):
    if root is None:
        return False
        
    if root.left is None and root.right is None:
        return True
        
    if root.left and root.right:
        return is_full_tree(root.left) and is_full_tree(root.right)
    return False
    
# Case 1
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
print(is_full_tree(root)) # Expected Output: True

# Case 2
root = TreeNode(10)
root.left = TreeNode(2)
root.right = TreeNode(1)
root.left.right = TreeNode(3)
print(is_full_tree(root)) # Expected Output: False
print()

"""Problem Set Version 3
Problem 1: Build A Binary Tree III
Given the following TreeNode class, create the binary tree depicted below."""
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

root = TreeNode("a")
root.left = TreeNode("b")
root.right = TreeNode("c")
root.right.right = TreeNode("d")
print_binary_tree(root)
print()

"""Problem 2: 3-Node Booleans
You are given the root of a binary tree that has exactly 3 nodes: the root, its left child, and its right child. The left and right child have a boolean value of either True or False.

The root has a string value of either AND or OR. Apply the boolean operation of the root to its two children. Return True if the result of the expression is truth and False otherwise.

Evaluate the time complexity of your function."""
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def tree_expression(root):
    if root is None:
        return False
    # extract the boolean value
    left_value = root.left.val
    right_value = root.right.val

    # check the root value
    if root.val == "AND":
        return left_value and right_value
    elif root.val == "OR":
        return left_value or right_value
    return False
    
# Case 1
root = TreeNode("OR")
root.left = TreeNode(True)
root.right = TreeNode(False)
print(tree_expression(root)) # Expected Output: True

# Case 2
root = TreeNode("AND")
root.left = TreeNode(True)
root.right = TreeNode(False)
print(tree_expression(root)) # Expected Output: False
print()

"""Problem 3: 3-Node Equality
You are given the root of a binary tree that has at most 3 nodes: the root, its left child, and its right child.

Return True if the root’s children have equal value and False otherwise.

Evaluate the time complexity of your function."""
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def equality(root):
    if root is None:
        return False

    if root.left is None or root.right is None:
        return root.left == root.right # True if both are None, False if only one is None
    return root.left.val == root.right.val 

# Case 1
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
print(equality(root)) # Expected Output: True

# Case 2
root = TreeNode(1)
root.left = TreeNode(2)
print(equality(root)) # Expected Output: False
print()

"""Problem 4: Find Leftmost Path I
Given the root of a binary tree, write a function that finds that returns a list of the left most path of the tree.

Evaluate the time complexity of your function."""
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def left_path(root):
    path_lst = []
    if root is None:
        return path_lst

    if root:
        path_lst.append(root.val)
        path_lst = path_lst + left_path(root.left)
    return path_lst
    
# Case 1
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(4)
root.left.right = TreeNode(3)
print(left_path(root)) # Expected Output: [1, 2, 4]

# Case 2
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
print(left_path(root)) # Expected Output: [1]

# Case 3
root = None
print(left_path(root)) # Expected Output: []
print()

"""Problem 5: Find Leftmost Path II
If you implemented the previous left_most() function iteratively, implement it recursively. If you implemented it recursively, implement it recursively.

Evaluate the time complexity of your implementation."""
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def left_path(root):
    path_lst_iter = []
    if root:
        path_lst_iter.append(root.val)

        while root.left:
            root = root.left
            path_lst_iter.append(root.val)
    return path_lst_iter
    
# Case 1
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(4)
root.left.right = TreeNode(3)
print(left_path(root)) # Expected Output: [1, 2, 4]

# Case 2
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
print(left_path(root)) # Expected Output: [1]

# Case 3
root = None
print(left_path(root)) # Expected Output: []
print()

"""Problem 6: Pre-order Traversal
Given the root of a binary tree, return a list representing the preorder traversal of its nodes' values. In an preorder traversal we traverse the current node, then the left subtree, then the right subtree."""
class TreeNode():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorder_traversal(root):
    preorder_dfs = []
    # base case: if node is null, return empty list
    if root is None:
        return preorder_dfs
        
    if root:
        # visit the root node
        preorder_dfs.append(root.val)
        # traverse the left subtree and add the left nodes to list
        preorder_dfs = preorder_dfs + preorder_traversal(root.left)
        # traverse the right subtree and add the right nodes to list
        preorder_dfs = preorder_dfs + preorder_traversal(root.right)
    return preorder_dfs
    
# Case 1
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(4)
root.left.right = TreeNode(3)
print("Pre-order traversal of binary tree")
print(preorder_traversal(root)) # Expected Output: [1, 2, 4, 3, 5]

# Case 2
root = None
print(preorder_traversal(root)) # Expected Output: []

# Case 3
root = TreeNode(1)
print(preorder_traversal(root)) # Expected Output: [1]

# Case 4
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
print(preorder_traversal(root)) # Expected Output: [1, 2, 3]
print()

"""Problem 7: Binary Tree All Lesser
Given the root of a binary tree and a value val, write a function is_lesser() that returns True if all the nodes in the tree have a value less than val and False otherwise. If the tree is empty, return False.

Evaluate the time complexity of your function."""
class TreeNode():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def is_lesser(root, val):
    if root is None:
        return True
        
    if root.value >= val:
        return False
    return is_lesser(root.left, val) and is_lesser(root.right, val)
    

# Case 1
val = 5
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
print(is_lesser(root, val)) # Expected Output: False

# Case 2
val = 6
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
print(is_lesser(root, val)) # Expected Output: True
print()

"""Problem 8: Binary Tree Any Greater
Given a value and the root of a binary tree, write a function contains_greater() which returns True if any nodes greater than value exist in the tree. If no node greater than value exist, return False. Assume the tree is balanced.

Evaluate the time complexity of your solution."""
class TreeNode():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def contains_greater(root, val):
    if root is None:
        return False

    if root.value > val:
        return True
    return contains_greater(root.left, val) or contains_greater(root.right, val)
    
# Case 1
val = 3
root = TreeNode(1)
root.left = TreeNode(5)
root.right = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(3)
print(contains_greater(root, val)) # Expected Output: True

# Case 2
val = 10
root = TreeNode(1)
root.left = TreeNode(5)
root.right = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(3)
print(contains_greater(root, val)) # Expected Output: False
print()

"""Problem 9: BST Any Greater
Given a value and the root of a binary search tree, write a function contains_greater_bst() which returns True if any nodes greater than value exist in the tree. If no node greater than value exists, return False. Assume the tree is balanced.

Evaluate the time complexity of your solution."""





"""
Session 2: Binary Trees
Problem Set Version 1
Problem 1: Is Uni-valued
A binary tree is uni-valued if every node in the tree has the same value. Given the root of a binary tree, return True if the given tree is uni-valued and False otherwise.

Evaluate the time complexity of your solution.
"""
class TreeNode():
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def is_univalued(root):
    # base case: empty tree is considered univalued by default
    if root is None:
        return True

    if root.left is not None and root.left.val != root.val:
        return False

    if root.right is not None and root.right.val != root.val:
        return False
    return is_univalued(root.left) and is_univalued(root.right)      

# Case 1
root =  TreeNode(1)
root.left = TreeNode(1)
root.right = TreeNode(1)
root.left.left = TreeNode(1)
root.left.right = TreeNode(1)
root.right.right = TreeNode(1)
print(is_univalued(root)) # Expected Output: True

# Case 2
root =  TreeNode(1)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.left.left = TreeNode(1)
root.left.right = TreeNode(1)
root.right.right = TreeNode(1)
print(is_univalued(root)) # Expected Output: False
print()

"""Problem 2: Binary Tree Height
Given the root of a binary tree, write a function height() that returns the height of a binary tree.

Evaluate the time complexity of your function."""

class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right

def height(root):
    if root is None:
        return 0
        
    left_tree_height = height(root.left)
    right_tree_height = height(root.right)
    return 1 + max(left_tree_height, right_tree_height)

# Case 1
root =  TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
print (height(root)) # Expected Output: 3

# Case 2
root =  TreeNode(4)
print (height(root)) # Expected Output: 1
print()

"""Problem 3: BST Insert
Given the root of a binary search tree, insert a new node with a given key and value into the tree. Return the root of the modified tree. The tree is sorted by key. If a node with the given key already exists, update the the existing key’s value. You do not need to maintain a balanced tree.

Evaluate the time complexity of your function."""

class TreeNode():
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.val = value
        self.left = left
        self.right = right

def insert(root, key, value):
    if root is None:
        return TreeNode(key, value)

    if key < root.key:
        root.left = insert(root.left, key, value)
    elif key > root.key:
        root.right = insert(root.right, key, value)
    else:
        root.value = value
    return root

# Helper function to print the tree (in-order traversal)
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(f"({root.key}: {root.val})", end=" ")
        inorder_traversal(root.right)

# Example usage
if __name__ == "__main__":
    # Example 1
    root = TreeNode(10, "Root")
    root.left = TreeNode(8, "Eight")
    root.right = TreeNode(15, "Fifteen")
    root.left.left = TreeNode(1, "One")
    root.left.right = TreeNode(6, "Six")

    print("Original tree:")
    inorder_traversal(root)
    print("\n")

    root = insert(root, 9, "Naruto")
    print("After inserting (9, 'Naruto'):")
    inorder_traversal(root)
    print("\n")

    # Example 2
    root2 = None
    root2 = insert(root2, 4, "Sailor Moon")
    print("After inserting into empty tree:")
    inorder_traversal(root2)
    print("\n")

"""Problem 4: BST Remove I
    Use the provided pseudocode to solve the problem below. Given a key and the root of a binary search tree, remove the node with the given key. Return the root of the modified tree.

    The tree is sorted by key. If multiple nodes with the given key exist, remove the first node you find. If you need to remove a node with two children, use the in-order successor of that node, which is the smallest value in its right subtree. You do not need to maintain a balanced tree."""

class TreeNode():
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.val = value
        self.left = left
        self.right = right

def remove_bst(root, key):
    if root is None:
        return None
        
    # Locate the node to be removed
    if key < root.key:
        root.left = remove_bst(root.left, key)
    elif key > root.key:
        root.right = remove_bst(root.right, key)
    else:
    # If the node is a leaf node:
        # Remove the node by redirecting the appropriate child reference of its parent to None
        if root.left is  None and root.right is None:
            return None
    # If the node has one parent:
        # Replace the node with its child, updating its parent's nodes child reference appropriately
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
    # If the node has two children:
        # Find the node's inorder successor (smallest node in right subtree)
        # Swap the value of the node and its inorder successor
        # Recursively remove the successor (which now has the current node's value)
        successor = find_min(root.right)
        root.key = successor.key
        root.val = successor.val
        root.right = remove_bst(root.right, successor.key)

    # Return the root of the updated tree
    return root

def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current
    
# Helper function to perform inorder traversal
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(f"({root.key}: {root.val})", end=" ")
        inorder_traversal(root.right)

# Test cases
def test_remove_bst():
    # Test case 1
    root1 = TreeNode(10, "Ten")
    root1.left = TreeNode(5, "Five")
    root1.right = TreeNode(15, "Fifteen")
    root1.left.left = TreeNode(1, "One")
    root1.left.right = TreeNode(8, "Eight")
    root1.right.left = TreeNode(13, "Thirteen")
    root1.right.right = TreeNode(16, "Sixteen")

    print("Original tree:")
    inorder_traversal(root1)
    print("\n")

    root1 = remove_bst(root1, 10)
    print("After removing 10:")
    inorder_traversal(root1)
    print("\n")

    # Test case 2
    root2 = TreeNode(10, "Ten")
    root2.left = TreeNode(5, "Five")
    root2.right = TreeNode(15, "Fifteen")
    root2.left.left = TreeNode(1, "One")
    root2.left.right = TreeNode(8, "Eight")
    root2.right.left = TreeNode(13, "Thirteen")
    root2.right.right = TreeNode(16, "Sixteen")
    root2.left.right.right = TreeNode(9, "Nine")

    print("Original tree:")
    inorder_traversal(root2)
    print("\n")

    root2 = remove_bst(root2, 8)
    print("After removing 8:")
    inorder_traversal(root2)
    print("\n")

    # Test case 3
    root3 = TreeNode(10, "Ten")
    root3.left = TreeNode(5, "Five")
    root3.right = TreeNode(15, "Fifteen")
    root3.left.left = TreeNode(1, "One")
    root3.left.right = TreeNode(8, "Eight")
    root3.right.left = TreeNode(13, "Thirteen")
    root3.right.right = TreeNode(16, "Sixteen")
    root3.left.right.right = TreeNode(9, "Nine")

    print("Original tree:")
    inorder_traversal(root3)
    print("\n")

    root3 = remove_bst(root3, 9)
    print("After removing 9:")
    inorder_traversal(root3)
    print("\n")

if __name__ == "__main__":
    test_remove_bst()

"""Problem 5: BST In-order Successor
In the remove_bst() problem, we summarized the in-order successor of a given node as the smallest node in the given node’s right subtree. This is true if the given node has a right subtree.

More generally, the in-order successor is the node with the smallest key greater than the key of the given node. Given the root of a binary search tree, and a TreeNode current, write a function that returns the in-order successor of the current node. Assume the tree is balanced.

Evaluate the time complexity of your solution."""
class TreeNode:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.val = value
        self.left = left
        self.right = right

def inorder_successor(root, current):
    successor = None

    # Case 1: If the current node has a right subtree
    if current.right:
        return find_minimum(current.right)

    # Case 2: If the current node doesn't have a right subtree
    while root:
        if current.key < root.key:
            successor = root
            root = root.left
        elif current.key > root.key:
            root = root.right
        else:
            break

    return successor

def find_minimum(node):
    while node.left:
        node = node.left
    return node

# Helper function to find a node with a given key
def find_node(root, key):
    if not root or root.key == key:
        return root
    if key < root.key:
        return find_node(root.left, key)
    return find_node(root.right, key)

# Test cases
def test_inorder_successor():
    # Construct the tree for both examples
    root = TreeNode(10, "Ten")
    root.left = TreeNode(5, "Five")
    root.right = TreeNode(15, "Fifteen")
    root.left.left = TreeNode(1, "One")
    root.left.right = TreeNode(8, "Eight")
    root.left.right.left = TreeNode(6, "Six")
    root.left.right.right = TreeNode(9, "Nine")

    # Test case 1
    current = find_node(root, 5)
    successor = inorder_successor(root, current)
    print("Test case 1:")
    print(f"Current: {current.key}")
    print(f"Successor: {successor.key if successor else None}")
    print()

    # Test case 2
    current = find_node(root, 6)
    successor = inorder_successor(root, current)
    print("Test case 2:")
    print(f"Current: {current.key}")
    print(f"Successor: {successor.key if successor else None}")
    print()

    # Additional test cases
    # Test case 3: Successor of the largest node
    current = find_node(root, 15)
    successor = inorder_successor(root, current)
    print("Test case 3 (largest node):")
    print(f"Current: {current.key}")
    print(f"Successor: {successor.key if successor else None}")
    print()

    # Test case 4: Successor of a node with right child
    current = find_node(root, 5)
    successor = inorder_successor(root, current)
    print("Test case 4 (node with right child):")
    print(f"Current: {current.key}")
    print(f"Successor: {successor.key if successor else None}")
    print()

if __name__ == "__main__":
    test_inorder_successor()
 
"""Problem 6: Merge Binary Trees
You are given two binary trees with roots root1 and root2. Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.

Return the merged tree."""
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right
        
def merge_trees(root1, root2):
    if root1 is None:
        return root2

    if root2 is None:
        return root1

    root1.val += root2.val 
    root1.left = merge_trees(root1.left, root2.left)
    root1.right = merge_trees(root1.right, root2.right)
    return root1


root1 = TreeNode(1)
root1.left = TreeNode(3)
root1.right = TreeNode(2)
root1.left.left = TreeNode(5)

root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.right = TreeNode(3)
root2.left.right = TreeNode(4)
root2.right.right = TreeNode(7)
merged_tree = merge_trees(root1, root2)
print(preorder_traversal(merged_tree))




    
# """
# # Assignment Questions
# 5. Insert Node into a Binary Search Tree
# Given the root of a binary search tree, insert a node with the value val into the tree. Return the root
# """
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def insert_node(root, val):
#     # Write your code here
#     if not root:
#         return TreeNode(val)

#     if val < root.val:
#         root.left = insert_node(root.left, val)
#     else:
#         root.right = insert_node(root.right, val)

#     return root

# """
# 6. Sum the Nodes
# Given the root of a binary tree, return the sum of all its node. You may assume all values are integers
# """
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def sum_tree(root):
#     # Write your code here
#     if not root:
#         return 0

#     return root.val + sum_tree(root.left) + sum_tree(root.right)

# """
# 7. Remove Node from a Binary Search Tree
# Given the root of a binary search tree, remove the node with the value val into the tree. All nodes in the tree are guaranteed to be unique. Return the root. If you need to replace a parent node with two children, use the in-order successor of that node, such that replacement.val is the smallest value greater than removed.val"""
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def remove_node(root, value):
#     if not root:
#         return None

#     if value < root.val:
#         root.left = remove_node(root.left, value)
#     elif value > root.val:
#         root.right = remove_node(root.right, value)
#     else:
#         # Node to delete found

#         # Case 1: Leaf node
#         if not root.left and not root.right:
#             return None

#         # Case 2: Only one child
#         if not root.left:
#             return root.right
#         if not root.right:
#             return root.left

#         # Case 3: Two children
#         # Find in-order successor (minimum value in the right subtree)
#         successor = find_min(root.right)
#         root.val = successor.val
#         root.right = remove_node(root.right, successor.val)

#     return root

# def find_min(node):
#     current = node
#     while current.left:
#         current = current.left
#     return current