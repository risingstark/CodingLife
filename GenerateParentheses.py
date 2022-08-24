# Givcen an integer n, generate all the valid
# combinations of n pairs of parentheses

# time: , space:

class Solution():
    def generate(self,n):
        def rec(n,diff,comb,combs):
            if diff < 0 or n < 0:
                return
            elif n == 0 and diff == 0:
                return combs.append(''.join(comb))
            else:
                comb.append('(')
                rec(n-1,diff+1,comb,combs)
                comb.pop()
                comb.append(')')
                rec(n-1,diff-1,comb,combs)
                comb.pop()
        
        combs = []
        rec(2*n,0,[],combs)
        return combs


if __name__=="__main__":
    s = Solution()
    n = 2
    print(s.generate(n))
