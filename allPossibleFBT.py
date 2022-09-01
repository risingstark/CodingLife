# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        if N % 2 == 0:
            return []
        elif N == 1:
            return [TreeNode(0)]
        res = []
        l = N-2
        r = 1
        while l > 0:
            tempL = self.allPossibleFBT(l)
            tempR = self.allPossibleFBT(r)
            L = len(tempL)
            R = len(tempR)
            for i in range(L):
                for j in range(R):
                    root = TreeNode(0)
                    root.left = tempL[i]
                    root.right = tempR[j]
                    res.append(root)
            l -= 2
            r += 2
        return res

if __name__ == "__main__":

    s = Solution()
    print(s.allPossibleFBT(5))