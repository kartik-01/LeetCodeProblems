# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # Base case: if the current node is None, return 0
        if root is None:
            return 0
        
        # Recursively calculate the depth of the left and right subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        # The maximum depth of the current node is 1 (for itself) plus the greater of its two children's depths
        return 1 + max(left_depth, right_depth)

# Example usage:
# Constructing a simple binary tree:
#         3
#        / \
#       9   20
#          /  \
#         15   7

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

solution = Solution()
print(solution.maxDepth(root))  # Output: 3
