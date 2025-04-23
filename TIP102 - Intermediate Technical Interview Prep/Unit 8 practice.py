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
    """
    traverse the current node's left subtree
    traverse the current node's right subtree
    visit the current node
    """
    # depth first serach (dfs) - postorder traversal
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

# -------------------------------------------------
# Standard Problem Set Version 2
# -------------------------------------------------
'''Problem 1: Building an Underwater Kingdom
Given the following TreeNode class, create the binary tree depicted below. The text representing each node should should be used as the value.

The root, or topmost node in the tree TreeNode("Poseidon") has been provided for you.'''
root = TreeNode("Poseidon")
root.left = TreeNode("Atlantis")
root.left.left = TreeNode("Coral")
root.left.right = TreeNode("Pearl")

root.right = TreeNode("Oceania")
root.right.left = TreeNode("Kelp")
root.right.right = TreeNode("Reef")
    
'''Problem 2: Are Twins?
Given the root of a binary tree that has at most three nodes: the root, its left child, and its right child.

Return True if the root's children are twins (have equal value) and False otherwise. If the root has no children, return False.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.'''
def mertwins(root):
    if root.left is None and root.right is None:
        return False
    
    if root.left is None:
        return False
    elif root.right is None:
        return False
    
    if root.left.val == root.right.val:
        return True
    return False 

'''Problem 3: Poseidon's Decision
Poseidon has received advice on an important matter from his council of advisors. Help him evaluate the advice from his council to make a final decision. 
You are given the advice as the root of a binary tree representing a boolean expression that has at most three nodes. The root may have exactly 0 or 2 children.

Leaf nodes have a boolean value of either True or False.
Non-leaf nodes have a string value of either AND or OR.
The evaluation of a node is as follows:

If the node is a leaf node, the evaluation is the value of the node, i.e. True or False.
Otherwise evaluate the node's two children and apply the boolean operation of its value with the children's evaluations.
Return the boolean result of evaluating the root node.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.'''
def get_decision(root):
    if root.left is None and root.right is None:
        return root.val
    if root.val == "OR":
        return root.left.val or root.right.val
    elif root.val == "AND":
        return root.left.val and root.right.val

'''Problem 4: Escaping the Sea Caves
You are given the root of a binary tree representing possible route through a system of sea caves. You recall that so long as you take the leftmost branch at every fork in the route, 
you'll find your way back home. Write a function leftmost_path() that returns an array with the value of each node in the leftmost path.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. 
Assume the input tree is balanced when calculating time complexity.'''
def leftmost_path_iterative(root):
    if root is None:
        return []
    
    if root.left is None and root.right is None:
        return [root.val]
    
    leftmost_node = [root.val]
    while root.left is not None:
        leftmost_node.append(root.left.val)
        root = root.left
    return leftmost_node


'''Problem 5: Escaping the Sea Caves II
If you implemented leftmost_path() iteratively in the previous problem, implement it recursively. If you implemented it recursively, implement it iteratively.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. 
Assume the input tree is balanced when calculating time complexity.'''
def leftmost_path_recursive(root):
    leftmost_node = []
    if root:
        leftmost_node.append(root.val)
        leftmost_node += leftmost_path_recursive(root.left)
    return leftmost_node    

'''Problem 6: Documenting Reefs
You are exploring a vast coral reef system. The reef is represented as a binary tree, where each node corresponds to a specific coral formation. 
You want to document the reef as you encounter it, starting from the root or main entrance of the reef.

Write a function explore_reef() that performs a preorder traversal of the reef and returns a list of the names of the coral formations in the order you visited them. 
In a preorder exploration, you explore the current node first, then the left subtree, and finally the right subtree.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. 
Assume the input tree is balanced when calculating time complexity.'''
def explore_reef(root):
    """
    visit the current node
    traverse the current node's left subtree
    traverse the current node's right subtree
    """
    # depth first serach (dfs) - preorder traversal
    preorder_dfs = []
    if root:
        preorder_dfs.append(root.val)
        preorder_dfs += explore_reef(root.left)
        preorder_dfs += explore_reef(root.right)
    return preorder_dfs

'''Problem 7: Coral Count
Due to climate change, you have noticed that coral has been dying in the reef near Atlantis. You want to ensure there is still a healthy level of coral in the reef. 
Given the root of a binary tree where each node represents a coral in the reef, write a function count_coral() that returns the number of corals in the reef.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. 
Assume the input tree is balanced when calculating time complexity.'''
def count_coral(root):
    # base case
    count = 0
    if root is None:
        return count
    
    # recursive case - method 1
    # if root:
    #     count = 1
    #     count += count_coral(root.left)
    #     count += count_coral(root.right)
    # return count

    # recursive case - method 2
    if root.left is None and root.right is None:
            return 1
    return 1 + count_coral(root.left) + count_coral(root.right)

'''Problem 8: Ocean Layers
Given the root of a binary tree that represents different sections of the ocean, write a function count_ocean_layers() that returns the depth of the ocean. 
The depth or height of the tree can be defined as the number of nodes on the longest path from the root node to a leaf node.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. 
Assume the input tree is balanced when calculating time complexity.'''
def ocean_depth_recursive(root):
    # base case
    if root is None:
        return 0
    
    # recursive case
    left_height = ocean_depth_recursive(root.left)
    right_heigth = ocean_depth_recursive(root.right)
    return 1 + max(left_height, right_heigth)
  
def ocean_depth_bfs(root):   
    if root is None:
        return 0
 
    queue = deque([root])
    depth = 0
    while queue:
        levelsize = len(queue)

        # traverse node at current level
        for _ in range(levelsize):
            popped_node = queue.popleft()
            if popped_node.left:
                queue.append(popped_node.left)
            if popped_node.right:
                queue.append(popped_node.right)
        depth += 1
    return depth 

        









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
    print()
    print("------ # Standard Problem Set Version 2 ------ ")
    print("Problem 1: Building an Underwater Kingdom")
    print(print_tree(root)) # Example Output: ['Poseidon', 'Atlantis', 'Oceania', 'Pearl', 'Kelp', 'Reef']
    print()
    print("Problem 2: Are Twins?")
    """
        Mermother
        /    \
    Coral   Coral
    """
    root1 = TreeNode("Mermother", TreeNode("Coral"), TreeNode("Coral"))

    """
        Merpapa
        /    \
    Calypso  Coral
    """
    root2 = TreeNode("Merpapa", TreeNode("Calypso"), TreeNode("Coral"))

    """
        Merenby
            \    
            Calypso  
    """
    root3 = TreeNode("Merenby", None, TreeNode("Calypso"))
    print(mertwins(root1))
    print(mertwins(root2))
    print(mertwins(root3))
    print()
    print("Problem 3: Poseidon's Decision")
    """
            OR
        /    \
        True  False
    """
    expression1 = TreeNode("OR", TreeNode(True), TreeNode(False))

    """
        False
    """
    expression2 = TreeNode(False)
    print(get_decision(expression1))
    print(get_decision(expression2))
    print()
    print("Problem 4: Escaping the Sea Caves")
    """
            CaveA
        /      \
        CaveB    CaveC
        /   \        \
    CaveD CaveE     CaveF  
    """
    system_a = TreeNode("CaveA", 
                    TreeNode("CaveB", TreeNode("CaveD"), TreeNode("CaveE")), 
                            TreeNode("CaveC", None, TreeNode("CaveF")))

    """
    CaveA
        \
        CaveB
            \
            CaveC  
    """
    system_b = TreeNode("CaveA", None, TreeNode("CaveB", None, TreeNode("CaveC")))
    print(leftmost_path_iterative(system_a))
    print(leftmost_path_iterative(system_b))
    print()
    print("Problem 5: Escaping the Sea Caves II")
    print(leftmost_path_recursive(system_a))
    print(leftmost_path_recursive(system_b))
    print()
    print("Problem 6: Documenting Reefs")
    """
            CoralA
            /     \
        CoralB  CoralC
        /   \      
    CoralD CoralE  
    """
    reef = TreeNode("CoralA", 
                    TreeNode("CoralB", TreeNode("CoralD"), TreeNode("CoralE")), 
                            TreeNode("CoralC"))
    print(explore_reef(reef))
    print()
    print("Problem 7: Coral Count")
    """
            Staghorn
            /        \
        Sea Fan      Sea Whip
        /     \       /   
    Bubble  Table  Star
    /
    Fire
    """
    reef1 = TreeNode("Staghorn", 
                    TreeNode("Sea Fan", TreeNode("Bubble", TreeNode("Fire")), TreeNode("Table")),
                            TreeNode("Sea Whip", TreeNode("Star")))

    """
        Fire
        /    \
    Black    Star
            /  
        Lettuce 
            \
            Sea Whip
    """
    reef2 = TreeNode("Fire", 
                    TreeNode("Black"), 
                            TreeNode("Star", 
                                    TreeNode("Lettuce", None, TreeNode("Sea Whip"))))

    print(count_coral(reef1))
    print(count_coral(reef2))    
    print()
    print("Problem 8: Ocean Layers")
    """
                    Sunlight
                /        \
                /          \
            Twilight      Squid
            /       \           \   
        Abyss  Anglerfish    Giant Squid
        /
    Trenches
    """
    ocean = TreeNode("Sunlight", 
                    TreeNode("Twilight", 
                            TreeNode("Abyss", 
                                    TreeNode("Trenches")), TreeNode("Anglerfish")),
                                            TreeNode("Squid", TreeNode("Giant Squid")))

    """
        Spray Zone
        /         \
    /           \ 
    Beach       High Tide
                /  
        Middle Tide
                \
                Low Tide
    """
    tidal_zones = TreeNode("Spray Zone", 
                        TreeNode("Beach"), 
                                TreeNode("High Tide", 
                                        TreeNode("Middle Tide", None, TreeNode("Low Tide"))))

    print(ocean_depth_recursive(ocean))
    print(ocean_depth_recursive(tidal_zones))
    print()
    print(ocean_depth_bfs(ocean))
    print(ocean_depth_bfs(tidal_zones))
    print()



