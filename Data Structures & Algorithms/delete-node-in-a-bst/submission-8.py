# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            # Node to delete found
            if root.left == None:
                return root.right
            elif root.right == None:
                return root.left
            else:
                # Two children: use inorder predecessor (max in left subtree)
                cur = root.left
                while cur.right:
                    cur = cur.right
                # cur is now the predecessor
                root.val = cur.val
                # Delete the predecessor from the left subtree
                root.left = self.deleteNode(root.left, root.val)

        return root
