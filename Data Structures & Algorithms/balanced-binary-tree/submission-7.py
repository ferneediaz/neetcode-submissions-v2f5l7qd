# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getHeight(node):
            if not node:
                return 0
            leftTree = getHeight(node.left)
            rightTree = getHeight(node.right)
            if leftTree == -1 or rightTree == -1:
                return -1

            if abs(rightTree - leftTree) > 1:
                return -1
            return 1 + max(leftTree, rightTree)

        return getHeight(root) != -1