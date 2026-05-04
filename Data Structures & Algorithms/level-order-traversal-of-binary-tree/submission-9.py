# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # res will store the final result: a list of levels,
        # where each level is itself a list of node values at that level.
        res = []

        # q is our queue (first-in, first-out data structure) used for breadth-first traversal.
        # We use deque from collections because it supports efficient pops from the left.
        q = collections.deque()
        # We start by putting the root of the tree into the queue.
        # If root is None (empty tree), this will put None into the queue.
        q.append(root)
        # We process nodes level by level until there are no more nodes in the queue.
        while q:
            # qLen stores how many nodes are in the current level.
            # This is important to separate the current level from the next level.
            qLen = len(q)
            # level will collect the values of all nodes at the current level.
            level = []
            # We iterate exactly qLen times to process all nodes at the current level.
            for i in range(qLen):
                # Remove the leftmost node from the queue (FIFO order).
                node = q.popleft()

                # We check if the popped item actually represents a real node.
                # In this implementation, we sometimes enqueue None children.
                # If node is not None, we process it; otherwise, we skip it.
                if node:
                    # node.val is the value stored at this tree node.
                    level.append(node.val)
                    # Enqueue the left child of this node.
                    # If the left child is None, we will enqueue None as a placeholder.
                    q.append(node.left)
                    # Enqueue the right child of this node.
                    # If the right child is None, we will enqueue None as a placeholder.
                    q.append(node.right)
            # After processing all nodes at the current level, we have collected
            # all their values in 'level'. If the level had at least one real node,
            # we add it to the result. If the entire level was made of None nodes
            # (which should not happen for a proper binary tree), 'level' would be empty.
            if level:
                res.append(level)
        # After the loop ends, res contains the level-order traversal:
        # each sublist corresponds to one level, from top to bottom, left to right.
        return res