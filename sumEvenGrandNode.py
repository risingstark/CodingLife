# # Sum of Nodes with Even-Valued Grandparent
# Given the root of a binary tree, return the sum of values of nodes with an even-valued grandparent.
#  If there are no nodes with an even-valued grandparent, return 0.

# A grandparent of a node is the parent of its parent if it exists.

# Example 1:
# Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
# Output: 18
# Explanation: The red nodes are the nodes with even-value grandparent 
# while the blue nodes are the even-value grandparents.

# Example 2:
# Input: root = [1]
# Output: 0

# Constraints:
# The number of nodes in the tree is in the range [1, 104].
# 1 <= Node.val <= 100


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import collections

class Solution(object):
    # BFS, iteratively, straightforward
    def sumEvenGrandparent1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q = collections.deque([root])
        sm = 0
        
        while q:
            node = q.popleft()
            # node val is even
            if node.val % 2 == 0:
                # check current node is grandparent
                if node.left:
                    if node.left.left:
                        sm+= node.left.left.val
                    if node.left.right:
                        sm+= node.left.right.val
                if node.right:
                    if node.right.left:
                        sm+= node.right.left.val
                    if node.right.right:
                        sm+= node.right.right.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return sm
                

    def sumEvenGrandparent2(self, root):
        if not root:
            return 0
    
        def traverse_node(node, parent, grandparent):
            if not node:
                return 0
            if grandparent and grandparent.val % 2 == 0:
                return node.val + traverse_node(node.left, node, parent) + traverse_node(node.right, node, parent)
            return traverse_node(node.left, node, parent) + traverse_node(node.right, node, parent)

        return traverse_node(root, None, None)
        