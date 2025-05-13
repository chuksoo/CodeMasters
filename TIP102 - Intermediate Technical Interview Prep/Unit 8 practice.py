###################################################
# Session 1: Binary Trees
###################################################
# Standard Problem Set Version 1
# -------------------------------------------------
from collections import deque 

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

# -------------------------------------------------
# Advanced Problem Set Version 1
# -------------------------------------------------       
'''Problem 1: Ivy Cutting
You have a trailing ivy plant represented by a binary tree. You want to take a cutting to start a new plant using the rightmost vine in the plant. 
Given the root of the plant, return a list with the value of each node in the path from the root node to the rightmost leaf node.

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. 
Assume the input tree is balanced when calculating time and space complexity.'''
def right_vine_recur(root):
    # pattern is preorder dfs  
    rightmost = []
    if root:
        rightmost.append(root.val)
        rightmost += right_vine_recur(root.right)
    return rightmost

'''Problem 2: Ivy Cutting II
If you implemented right_vine() iteratively in the previous problem, implement it recursively. If you implemented it recursively, implement it iteratively.

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. 
Assume the input tree is balanced when calculating time and space complexity.'''
def right_vine_iter(root):
    if root is None:
        return []
    
    if root.right is None:
        return [root.val]
    
    right_most = []
    while root:
        right_most.append(root.val)
        root = root.right
    return right_most

'''Problem 3: Pruning Plans
You have a large overgrown Magnolia tree that's in desperate need of some pruning. Before you can prune the tree, 
you need to do a full survey of the tree to evaluate which sections need to be pruned.

Given the root of a binary tree representing the magnolia, return a list of the values of each node using a postorder traversal. 
In a postorder traversal, you explore the left subtree first, then the right subtree, and finally the root. Postorder traversals 
are often used when deleting nodes from a tree.

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your 
solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity.'''
def survey_tree(root):
    postorder_bfs = []
    if root:
        postorder_bfs += survey_tree(root.left)
        postorder_bfs += survey_tree(root.right)
        postorder_bfs.append(root.val)
    return postorder_bfs


'''Problem 4: Sum Inventory
A local flower shop stores its inventory in a binary tree, where each node represents their current stock of a flower variety. 
Given the root of a binary tree inventory, return the sum of all the flower stock in the store.

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for 
why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity.'''
def sum_inventory(inventory):
    inventory_count = 0
    if inventory:
        inventory_count += inventory.val
        inventory_count += sum_inventory(inventory.left)
        inventory_count += sum_inventory(inventory.right)
    return inventory_count
 
'''Problem 5: Calculating Yield II
You have a fruit tree represented as a binary tree. Given the root of the tree, evaluate the amount of fruit your tree will yield this year. The tree has the following form:

Leaf nodes have an integer value.
Non-leaf nodes have a string value of either "+", "-", "*", or "-".
The yield of a the tree is calculated as follows:

If the node is a leaf node, the yield is the value of the node.
Otherwise evaluate the node's two children and apply the mathematical operation of its value with the children's evaluations.
Return the result of evaluating the root node.

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your 
solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity.'''
def calculate_yield_fruit(apple_tree):
    # base case
    if apple_tree.left is None and apple_tree.right is None:
        return apple_tree.val
    
    # recusive case
    left_val = calculate_yield_fruit(apple_tree.left)
    right_val = calculate_yield_fruit(apple_tree.right)
    
    # apply node's operator
    if apple_tree.val == '+':
        return left_val + right_val
    elif apple_tree.val == '-':
        return left_val - right_val
    elif apple_tree.val == '*':
        return left_val * right_val
    else:
        return None
    
'''Problem 6: Plant Classifications
Given the root of a binary tree used to classify plants where each level of the tree represents a higher degree of specificity, 
return an array with the most specific plant classification categories (aka the leaf node values). Leaf nodes are nodes with no children.

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your 
solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity.'''
def get_most_specific(taxonomy):
    if taxonomy is None:
        return []
    
    # base case
    if taxonomy.left is None and taxonomy.right is None:
        return [taxonomy.val]
    
    # recursive case
    leaf_nodes = []
    if taxonomy.left:
        leaf_nodes.extend(get_most_specific(taxonomy.left))
    if taxonomy.right:
        leaf_nodes.extend(get_most_specific(taxonomy.right))
    return leaf_nodes

'''Problem 7: Count Old Growth Trees
Given the root of a binary tree where each node represents the age of a tree in a forest, write a function count_old_growth() 
that returns the number of old growth trees in the forest. A tree is considered old growth if it has age greater than threshold.

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your 
solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity.'''
def count_old_growth(root, threshold):
    count = 0

    if root is None:
        return count
    # base case
    if root.val > threshold:
        count += 1
    
    count += count_old_growth(root.left, threshold) 
    count += count_old_growth(root.right, threshold)
    return count

'''Problem 8: Twinning Trees
Given the roots of two trees root1 and root2, return True if the trees have identical structures and values and False otherwise.

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your 
solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity.'''
def is_identical(root1, root2):
    # base case
    # if both are empty
    if root1 is None and root2 is None:
        return True
    
    # if one empty, one not
    if root1 is None or root2 is None:
        return False
    
    # both must have same value and identical subtree
    if root1.val != root2.val:
        return False
    
    # recursive case
    left_path = is_identical(root1.left, root2.left)
    right_path = is_identical(root1.right, root2.right)
    return left_path and right_path
        

###################################################
# Session 2: Binary Trees
###################################################
# Standard Problem Set Version 1
# -------------------------------------------------

# Tree Node class
class TreeNode_key:
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
  root = TreeNode_key(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode_key(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode_key(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root

'''Problem 1: Monstera Madness
Given the root of a binary tree where each node represents the number of splits in a leaf of a Monstera plant, return the number of Monstera leaves that have an odd number of splits.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.'''
def count_odd_splits(root):
    count = 0

    # base case
    if root is None:
        return count 
    
    if root.val % 2 != 0:
        count += 1

    count += count_odd_splits(root.left)
    count += count_odd_splits(root.right)
    return count

'''Problem 2: Flower Finding
You are looking to buy a new flower plant for your garden. The nursery you visit stores its inventory in a binary search tree (BST) where each node represents a plant in the store. 
The plants are organized according to their names (vals) in alphabetical order in the BST.

Given the root of the binary search tree inventory and a target flower name, write a function find_flower() that returns True if the flower is present in the garden and False otherwise.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.'''
def find_flower_2(inventory, name):
    # base case
    if not inventory:
        return False
    
    if inventory.val == name:
        return True
    elif name < inventory.val:
        return find_flower_2(inventory.left, name)
    else:
        return find_flower_2(inventory.right, name)
    
'''Problem 3: Flower Finding II
Consider the following function non_bst_find_flower() which accepts the root of a binary tree inventory and a flower name, and returns True if a flower (node) with name exists in the binary tree. 
Unlike the previous problem, this tree is not a binary search tree.

Compare your solution to find_flower() in Problem 2 to the following solution. Discuss with your group: How is the code different? Why?
What is the time complexity of non_bst_find_flower()? How does it compare to the time complexity of find_flower() in Problem 2?
How would the time complexity of find_flower() from Problem 2 change if the tree inventory was not balanced?'''
def non_bst_find_flower(root, name):
    if root is None:
        return False
    
    if root.val == name:
        return True

    return non_bst_find_flower(root.left, name) or non_bst_find_flower(root.right, name)

'''Problem 4: Adding a New Plant to the Collection
You have just purchased a new houseplant and are excited to add it to your collection! Your collection is meticulously organized using a Binary Search Tree (BST) 
where each node in the tree represents a houseplant in your collection, and houseplants are organized alphabetically by name (val).

Given the root of your BST collection and a new houseplant name, insert a new node with value name into your collection. Return the root of your updated collection. 
If another plant with name already exists in the tree, add the new node in the existing node's right subtree.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.'''
def add_plant(collection, name):
    if collection is None:
        return TreeNode(name)
    
    if name < collection.val:
        collection.left = add_plant(collection.left, name)
    else:
        collection.right = add_plant(collection.right, name)
    return collection

'''Problem 5: Sorting Plants by Rarity
You are going to a plant swap where you can exchange cuttings of your plants for new plants from other plant enthusiasts. You want to bring a mix of cuttings from both common and rare plants in your collection. 
You track your plant collection in a BST where each node has a key and a val. The val contains the plant name, and the key is an integer representing the plant's rarity. Plants are organized in the BST by their key.

To help choose which plants to bring, write a function sort_plants() which takes in the BST root collection and returns an array of plant nodes as tuples in the form (key, val) sorted from least to most rare. 
Sorted order can be achieved by performing an inorder traversal of the BST.'''
def sort_plants(collection):
    inorder_bfs = []
    if collection:
        inorder_bfs += sort_plants(collection.left)
        inorder_bfs.append((collection.key, collection.val))
        inorder_bfs += sort_plants(collection.right)
    return inorder_bfs

'''Problem 6: Finding a New Plant Within Budget
You are looking for a new plant and have a max budget. The plant store that you are shopping at stores their inventory in a BST where each node has a key representing the price of the plant and value cntains the plant's name. 
Plants are ordered by their prices. You want to find a plant that is close to but lower than your budget.

Given the root of the BST inventory and an integer budget, write a function pick_plant() that returns the plant with the highest price below budget. If no plant with a price strictly below budget exists, the function should return None.'''
def pick_plant(root, budget):
    current = root
    best_node = None
    # traverse the tree
    while current is not None:
        if current.key < budget:
            # update best node if current node is better
            if best_node is None or current.key > best_node.key:
                best_node = current
            current = current.right
        else:
            # current is too expensive, move left
            current = current.left
    return best_node.val if best_node else None

'''Problem 7: Remove Plant
A plant in your houseplant collection has become infested with aphids, and unfortunately you need to throw it out. Given the root of a BST collection where each node represents a plant in your collection, 
and a plant name, remove the plant node with value name from the collection. Return the root of the modified collection. Plants are organized alphabetically in the tree by value.

If the node with name has two children in the tree, replace it with its inorder predecessor (rightmost node in its left subtree). You do not need to maintain a balanced tree.

Pseudocode has been provided for you.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.'''
def remove_plant(collection, name):
    if collection is None:
        return collection
    
    # Step 1: Find the node to be removed
    if name < collection.val:
        collection.left = remove_plant(collection.left, name)
    elif name > collection.val:
        collection.right = remove_plant(collection.right, name)
    else:
        # Node with the same name found
        # Step 2: Node has no children (leaf node)
        if collection.left is None and collection.right is None:
            return None
        
        # Step 3: Node has one child
        if collection.left is None:
            return collection.right
        elif collection.right is None:
            return collection.left
        
        # Step 4: Node has two children
        # Find the inorder predecessor (rightmost node in the left subtree)
        predecessor = max_value_node(collection.left)
        # Replace the node's value with the predecessor's value
        collection.val = predecessor.val
        # Remove the inorder predecessor
        collection.left = remove_plant(collection.left, predecessor.val)
    
    return collection

def max_value_node(node):
    current = node
    while current.right:
        current = current.right
    return current

    


    





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
    print("------ # Advanced Problem Set Version 2 ------ ")
    print("Problem 1: Ivy Cutting")
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

    print(right_vine_recur(ivy1))
    print(right_vine_recur(ivy2))
    print()
    print("Problem 2: Ivy Cutting II")
    print(right_vine_iter(ivy1))
    print(right_vine_iter(ivy2))  
    print()
    print("Problem 3: Pruning Plans")  
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
    print("Problem 4: Sum Inventory")
    """
        40
        /  \
    5   10
    /   /  \
    20   1   30
    """

    inventory = TreeNode(40, 
                        TreeNode(5, TreeNode(20)),
                                TreeNode(10, TreeNode(1), TreeNode(30)))

    print(sum_inventory(inventory))   
    print()
    print("Problem 5: Calculating Yield II") 
    """
        +
       / \ 
      /   \
     -     *
    / \   / \
    4   2 10  2
    """
    root = TreeNode("+")
    root.left = TreeNode("-")
    root.right = TreeNode("*")
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(2)
    print(calculate_yield_fruit(root))
    print()
    print("Problem 6: Plant Classifications")
    """
            Plantae
            /       \
            /         \
            /           \ 
    Non-flowering     Flowering
    /      \       /        \
    Mosses   Ferns Gymnosperms Angiosperms
                                /     \
                            Monocots  Dicots
    """
    plant_taxonomy = TreeNode("Plantae", 
                            TreeNode("Non-flowering", TreeNode("Mosses"), TreeNode("Ferns")),
                                    TreeNode("Flowering", TreeNode("Gymnosperms"), 
                                            TreeNode("Angiosperms", TreeNode("Monocots"), TreeNode("Dicots"))))
    print(get_most_specific(plant_taxonomy))    
    print()
    print("Problem 7: Count Old Growth Trees")
    """
        100
        /  \
        /    \
    1200  1500
    /     /  \
    20    700  2600
    """
    forest = TreeNode(100, 
                    TreeNode(1200, TreeNode(20)),
                            TreeNode(1500, TreeNode(700), TreeNode(2600)))
    print(count_old_growth(forest, 1000))
    print()
    print("Problem 8: Twinning Trees")
    """
        1                1
        / \              / \
        2   3            2   3  
    """
    root1 = TreeNode(1, TreeNode(2), TreeNode(3))
    root2 = TreeNode(1, TreeNode(2), TreeNode(3))

    """
        1                1
        /                  \
        2                    2  
    """
    root3 = TreeNode(1, TreeNode(2))
    root4 = TreeNode(1, None, TreeNode(2))
    print(is_identical(root1, root2))
    print(is_identical(root3, root4))
    print()
    print("-------- # Session 2: Binary Trees -------- ")
    print("------ # Standard Problem Set Version 1 ------ ")
    print("Problem 1: Monstera Madness")
    """
        2
        / \
        /   \
    3     5
    / \     \
    6   7     12
    """

    # Using build_tree() function included at top of page
    values = [2, 3, 5, 6, 7, None, 12]
    monstera = build_tree(values)
    print(count_odd_splits(monstera))
    print(count_odd_splits(None))
    print()
    print("Problem 2: Flower Finding")
    """
            Rose
            /    \
        Lilac  Tulip
        /  \       \
    Daisy Lily   Violet
    """

    # using build_tree() function at top of page
    values = ["Rose", "Lilac", "Tulip", "Daisy", "Lily", None, "Violet"]
    garden = build_tree(values)
    print(find_flower_2(garden, "Lilac"))  
    print(find_flower_2(garden, "Sunflower")) 
    print()
    print("Problem 3: Flower Finding II")
    """
            Daisy
            /    \
        Lily   Tulip
        /  \       \
    Rose  Violet  Lilac
    """
    # using build_tree() function at top of page
    values = ["Rose", "Lily", "Tulip", "Daisy", "Lilac", None, "Violet"]
    garden = build_tree(values)
    print(non_bst_find_flower(garden, "Lilac"))  
    print(non_bst_find_flower(garden, "Sunflower"))  
    print()
    print("Problem 4: Adding a New Plant to the Collection")
    """
                Money Tree
            /              \
    Fiddle Leaf Fig    Snake Plant
    """
    # Using build_tree() function at the top of page
    values = ["Money Tree", "Fiddle Leaf Fig", "Snake Plant"]
    collection = build_tree(values)
    # Using print_tree() function at the top of page
    print_tree(add_plant(collection, "Aloe"))
    print()
    print("Problem 5: Sorting Plants by Rarity")
    """
            (3, "Monstera")
            /               \
    (1, "Pothos")     (5, "Witchcraft Orchid")
            \                 /
    (2, "Spider Plant")   (4, "Hoya Motoskei")
    """

    # Using build_tree() function at the top of page
    values = [(3, "Monstera"), (1, "Pothos"), (5, "Witchcraft Orchid"), None, (2, "Spider Plant"), (4, "Hoya Motoskei")]
    collection = build_tree(values)
    print(sort_plants(collection))
    print()
    print("Problem 6: Finding a New Plant Within Budget")
    """
                (50, "Fiddle Leaf Fig")
                /                       \
        (25, "Monstera")           (70, "Snake Plant")
        /        \                   /         \
    (15, "Aloe")  (40, "Pothos")  (60, "Fern")  (80, "ZZ Plant")
    """

    # Using build_tree() function at the top of page
    values = [(50, "Fiddle Leaf Fig"), (25, "Monstera"), (70, "Snake Plant"), (15, "Aloe"), 
                (40, "Pothos"), (60, "Fern"), (80, "ZZ Plant")]
    inventory = build_tree(values)
    print(pick_plant(inventory, 50)) 
    print(pick_plant(inventory, 25)) 
    print(pick_plant(inventory, 15)) 
    print()
    print("Problem 7: Remove Plant")
    """
                Money Tree
                /         \
            Hoya        Pilea
                \        /   \
                Ivy    Orchid  ZZ Plant
    """

    # Using build_tree() function at the top of page
    values = ["Money Tree", "Hoya", "Pilea", None, "Ivy", "Orchid", "ZZ Plant"]
    collection = build_tree(values)
    # Using print_tree() function at the top of page
    print_tree(remove_plant(collection, "Pilea"))
    print()

