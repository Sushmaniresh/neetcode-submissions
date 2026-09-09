# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.max_diameter = 0
        
        def dfs(node):
            if not node:
                # The height of an empty node is 0
                return 0
            
            # Recursively find the height of left and right subtrees
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            
            # The diameter at the current node is the sum of left and right heights
            current_diameter = left_height + right_height
            
            # Update the global maximum diameter if the current one is larger
            self.max_diameter = max(self.max_diameter, current_diameter)
            
            # Return the height of the current node to its parent
            return 1 + max(left_height, right_height)
        
        dfs(root)
        return self.max_diameter
