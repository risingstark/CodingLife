# Given the root of a binary tree and an integer targetSum, 
# return the number of paths where the sum of the values along the path equals targetSum.

# The path does not need to start or end at the root or a leaf, 
# but it must go downwards (i.e., traveling only from parent nodes to child nodes).

# example 1
# Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
# Output: 3
# Explanation: The paths that sum to 8 are shown.

# example 2
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: 3

# Constraints:
# The number of nodes in the tree is in the range [0, 1000].
# -109 <= Node.val <= 109
# -1000 <= targetSum <= 1000
# ==============================================================================================================

# DFS with memoization:
# Use a variable prevSum to record the sum of all node values from the root r to the parent p of the current node.
# Then including the current node, the sum becomes currSum = prevSum + node.val. 
# Now for each node on the path, we can calculate their respective currSum, 
# we use a dictionary rec to record the frequency of all such sums. 
# If the sum of nodes on a path ending with the current node has value sum, 
# it implies that currSum - sum is in rec. 
# Moreover, the number of such paths is rec[currSum - sum]. 
# Then we can do DFS on the left and right child of the current node, with currSum being their prevSum. 
# Also note that we need to do rec[currSum] -= 1 after DFS on the left and right child of the current node,
# because the current node is not on the path of DFSs on other nodes, hence currSum is not available for other DFSs.

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        
        def dfs(root, prevSum, sum):
            if not root:
                return 0
            count = 0
            currSum = prevSum + root.val
            if currSum - sum in rec:
                count += rec[currSum - sum]
            if currSum in rec:
                rec[currSum] += 1
            else:
                rec[currSum] = 1
            count += dfs(root.left, currSum, sum)
            count += dfs(root.right, currSum, sum)
            rec[currSum] -= 1
            return count
            
        rec = {0:1}
        return dfs(root, 0, sum)
    