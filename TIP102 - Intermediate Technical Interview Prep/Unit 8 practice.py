###################################################
# Session 1: Binary Trees
###################################################
# Standard Problem Set Version 1
# -------------------------------------------------

'''Problem 1: Grafting Apples
You are grafting different varieties of apple onto the same root tree can produce many different varieties of apples! 
Given the following TreeNode class, create the binary tree depicted below. The text representing each node should should be used as the value.

The root, or topmost node in the tree TreeNode("Trunk") has been provided for you.

             Trunk
          /         \
      Mcintosh   Granny Smith
      /     \       /     \
    Fuji   Opal   Crab   Gala
'''
from collections import deque
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def print_tree(root):
    if not root:
        return []

    queue = deque([root])
    output = []

    while queue:
        curr = queue.popleft()
        output.append(curr.val)

        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
    
    return output

root = TreeNode("Trunk")
root.left = TreeNode("Mcintosh")
root.right = TreeNode("Granny Smith")

root.left.left = TreeNode("Fuji")
root.left.right = TreeNode("Opal")

root.right.left = TreeNode("Crab")
root.right.right = TreeNode("Gala")

'''Problem 2: Calculating Yield
You have a fruit tree represented as a binary tree with exactly three nodes: the root and its two children. 
Given the root of the tree, evaluate the amount of fruit your tree will yield this year. The tree has the following form:
    +
  /   \
 7     5

Leaf nodes have an integer value.
The root has a string value of either "+", "-", "*", or "-".
The yield of a the tree is calculated by applying the mathematical operation to the two children.

Return the result of evaluating the root node.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.'''
def calculate_yield(root):
    if root.val == "+":
        return root.left.val + root.right.val
    elif root.val == "-":
        return root.left.val - root.right.val
    elif root.val == "*":
        return root.left.val * root.right.val
    elif root.val == "/":
        return root.left.val / root.right.val
    else: 
        return None

'''Problem 3: Ivy Cutting
You have a trailing ivy plant represented by a binary tree. You want to take a cutting to start a new plant using the rightmost vine in the plant. 
Given the root of the plant, return a list with the value of each node in the path from the root node to the rightmost leaf node.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. 
Assume the input tree is balanced when calculating time complexity.'''
def right_vine_iterative(root):
    if root is None:
        return []
    
    if root.left is None and root.right is None:
        return [root.val]
    
    result = [root.val]
    while root.right is not None:
        result.append(root.right.val)
        root = root.right
    return result

'''Problem 4: Ivy Cutting II
If you implemented right_vine() iteratively in the previous problem, implement it recursively. 
If you implemented it recursively, implement it iteratively.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. 
Assume the input tree is balanced when calculating time complexity.'''
def right_vine_recursive(root):
    if root is None:
        return []
    
    root.left = None
    right_val = right_vine_recursive(root.right)

    return [root.val] + right_val

'''Problem 5: Count the Tree Leaves
You've grown an oak tree from a tiny little acorn and it's finally sprouting leaves! Given the root of a binary tree representing your oak tree, 
count the number of leaf nodes in the tree. A leaf node is a node that does not have any children.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. 
Assume the input tree is balanced when calculating time complexity.'''
def count_leaves(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return count_leaves(root.left) + count_leaves(root.right)

'''Problem 6: Pruning Plans
You have a large overgrown Magnolia tree that's in desperate need of some pruning. Before you can prune the tree, 
you need to do a full survey of the tree to evaluate which sections need to be pruned.

Given the root of a binary tree representing the magnolia, return a list of the values of each node using a postorder traversal. 
In a postorder traversal, you explore the left subtree first, then the right subtree, and finally the root. Postorder traversals are 
often used when deleting nodes from a tree.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. 
Assume the input tree is balanced when calculating time complexity.'''
def survey_tree(root):
    postorder_dfs = []

    if root:
        postorder_dfs += survey_tree(root.left)
        postorder_dfs += survey_tree(root.right)
        postorder_dfs.append(root.val)
    return postorder_dfs

'''Problem 7: Foraging Berries
You've found a wild blueberry bush and want to do some foraging. However, you want to be conscious of the local ecosystem and leave some behind for 
local wildlife and regeneration. To do so, you plan to only harvest from branches where the number of berries is greater than threshold.

Given the root of a binary tree representing a berry bush where each node represents the number of berries on a branch of the bush, 
write a function harvest_berries(), that finds the number of berries you can harvest by returning the sum of all nodes with value greater than threshold.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. 
Assume the input tree is balanced when calculating time complexity.'''
def harvest_berries(root, threshold):
    if root is None:
        return 0

    total = 0

    if root.val > threshold:
        total += root.val
    
    total += harvest_berries(root.right, threshold)
    total += harvest_berries(root.left, threshold)

    return total

'''Problem 8: Flower Fields
You're looking for the perfect bloom to add to your bouquet of flowers. Given the root of a binary tree representing flower options, and a target flower flower, 
return True if the bloom you are looking for each exists in the tree and False otherwise.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. 
Assume the input tree is balanced when calculating time complexity.'''
def find_flower(root, flower):
    # breadth first search (bfs) or level-order traversal
    if root is None:
        return False
    
    queue = deque()
    queue.append(root)

    while queue:
        popped_node = queue.popleft()
        if popped_node.val == flower:
            return True
        if popped_node.left:
            queue.append(popped_node.left)
        if popped_node.right:
            queue.append(popped_node.right)

    return False

    




if __name__ == "__main__":
    print("-------- # Session 1: Binary Trees -------- ")
    print("------ # Standard Problem Set Version 1 ------ ")
    print("Problem 1: Grafting Apples")
    print(print_tree(root)) # Expected Output: ['Trunk', 'Mcintosh', 'Granny Smith', 'Fuji', 'Opal', 'Crab', 'Gala']
    print()
    print("Problem 2: Calculating Yield")
    apple_tree = TreeNode("+", TreeNode(7), TreeNode(5))
    print(calculate_yield(apple_tree))
    print()
    print("Problem 3: Ivy Cutting")
    """
            Root
        /      \
        Node1    Node2
    /         /    \
    Leaf1    Leaf2  Leaf3
    """
    ivy1 = TreeNode("Root", 
                    TreeNode("Node1", TreeNode("Leaf1")),
                    TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

    """
        Root
        /  
        Node1
        /
    Leaf1  
    """
    ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))
    print(right_vine_iterative(ivy1))
    print(right_vine_iterative(ivy2))
    print()
    print("Problem 4: Ivy Cutting II")
    print(right_vine_recursive(ivy1))
    print(right_vine_recursive(ivy2))
    print()
    print("Problem 5: Count the Tree Leaves")
    """
            Root
          /      \
        Node1    Node2
      /         /    \
    Leaf1    Leaf2  Leaf3
    """

    oak1 = TreeNode("Root", 
                    TreeNode("Node1", TreeNode("Leaf1")),
                    TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))
    """
          Root
          /  
        Node1
        /
      Leaf1  
    """
    oak2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))
    print(count_leaves(oak1))
    print(count_leaves(oak2))
    print()
    print("Problem 6: Pruning Plans")
    """
          Root
        /      \
      Node1    Node2
     /         /    \
    Leaf1    Leaf2  Leaf3
    """

    magnolia = TreeNode("Root", 
                    TreeNode("Node1", TreeNode("Leaf1")),
                    TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))
    print(survey_tree(magnolia))
    print()
    print("Problem 7: Foraging Berries")
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
    print()
    print("Problem 8: Flower Fields")
    """
            Rose
            /    \
        /      \
        Lily     Daisy
        /    \        \
    Orchid  Lilac    Dahlia
    """

    flower_field = TreeNode("Rose", 
                            TreeNode("Lily", TreeNode("Orchid"), TreeNode("Lilac")),
                                    TreeNode("Daisy", None, TreeNode("Dahlia")))
    print(find_flower(flower_field, "Lilac"))
    print(find_flower(flower_field, "Hibiscus"))    