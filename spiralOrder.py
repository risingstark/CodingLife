# Given an m x n matrix, return all elements of the matrix in spiral order.
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

class Solution(object):

    # iteratively
    def spiralOrder1(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        res = []
        x0,x1 = 0,len(matrix[0]) 
        y0,y1 = 0,len(matrix)
        
        while x0 < x1 and y0 < y1:
            for i in range(x0,x1-1):
                res.append(matrix[y0][i])
            for j in range(y0,y1):
                res.append(matrix[j][x1-1])
            if y0 + 1 != y1:
                for k in range(x1-2,x0-1,-1):
                    res.append(matrix[y1-1][k])
            if x0 + 1 != x1:
                for t in range(y1-2,y0,-1):
                    res.append(matrix[t][x0])
            x0+=1
            x1-=1
            y0+=1
            y1-=1
        
        return res
    
    # simple solution
    def spiralOrder2(self, matrix):
        return matrix and list(matrix.pop(0)) + self.spiralOrder2(zip(*matrix)[::-1])

#Here's how the matrix changes by always extracting the first row and rotating the remaining matrix counter-clockwise

# |1 2 3|      |6 9|      |8 7|      |4|  =>  |5|  =>  ||
# |4 5 6|  =>  |5 8|  =>  |5 4|  =>  |5|
# |7 8 9|      |4 7|

if __name__ =="__main__":

    s = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(s.spiralOrder1(matrix))
    print(s.spiralOrder2(matrix))