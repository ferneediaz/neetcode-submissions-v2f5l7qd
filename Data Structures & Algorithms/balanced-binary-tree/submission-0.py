# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return [True, 0] 
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            # A node is balanced if left is balanced, right is balanced, 
            # AND the height difference is no more than 1
            balanced = (left[0] and right[0] and 
                        abs(left[1] - right[1]) <= 1)
            
            # The height is 1 + the tallest child's height
            current_height = 1 + max(left[1], right[1])
            
            return [balanced, current_height]

        # Call the helper and return only the boolean (index 0)
        return dfs(root)[0]
