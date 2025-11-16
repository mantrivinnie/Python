# Program to check if a Binary Tree is balanced


#Definition:
#A binary tree is balanced if for every node, the difference in height between the left and right subtrees is no more than 1.
#(i.e., |height(left) - height(right)| ≤ 1 for all nodes)

# Node class for the binary tree
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


# Function to check if tree is balanced
def is_balanced(root):
    # Helper function returns (isBalanced, height)
    def check(node):
        if node is None:
            return True, 0  # Empty tree is balanced with height 0

        # Recursively check left and right subtrees
        left_balanced, left_height = check(node.left)
        right_balanced, right_height = check(node.right)

        # Current node's balance condition
        balanced = (left_balanced and right_balanced and abs(left_height - right_height) <= 1)
        height = max(left_height, right_height) + 1

        return balanced, height

    result, _ = check(root)
    return result


# Example tree construction
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(6)   # Extra depth to make it unbalanced

# Check if balanced
if is_balanced(root):
    print("The binary tree is balanced.")
else:
    print("The binary tree is not balanced.")


'''

If you remove root.left.left.left = Node(6) (so both sides have nearly equal depth):
The binary tree is balanced.

Explanation:
The helper function check(node) computes both:
The height of each subtree.
Whether the subtree is balanced.
It uses post-order traversal (left → right → root) so that each node is checked only once.
 Time Complexity: O(n) — every node is visited once.
 Space Complexity: O(h) — for recursion stack, where h is the height of the tree.

'''