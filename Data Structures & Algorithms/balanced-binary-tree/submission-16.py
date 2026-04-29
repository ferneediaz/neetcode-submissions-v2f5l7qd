class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0
            leftTree = dfs(node.left)
            rightTree = dfs(node.right)

            if leftTree == -1:
                return -1
            if rightTree == -1:
                return -1
            if abs(leftTree - rightTree) > 1:
                return -1
            return max(leftTree, rightTree) + 1
        ans = dfs(root)
        return ans != -1