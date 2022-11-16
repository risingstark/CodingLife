# Letter Tile Possibilities

# You have n  tiles, where each tile has one letter tiles[i] printed on it.
# Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.
 
# Example 1:
# Input: tiles = "AAB"
# Output: 8
# Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".

# Example 2:
# Input: tiles = "AAABBC"
# Output: 188

# Example 3:
# Input: tiles = "V"
# Output: 1
 
# Constraints:
# 1 <= tiles.length <= 7
# tiles consists of uppercase English letters.


class Solution:
    
    def numTilePossibilities1(self, tiles: str) -> int:
        n = len(tiles)
        visited = [False] * n
        used = set()

        def dfs(ans):
            if len(ans) > 0:
                used.add("".join(ans))
            if len(ans) >= n:
                return
            for i in range(n):
                if visited[i]: 
                    continue
                visited[i] = True
                dfs(ans + [tiles[i]])                
                visited[i] = False
                
        dfs([])
        return len(used)
    
    # simpler version of using DFS
    def numTilePossibilities2(self, tiles: str) -> int:

        res = set()
        def dfs(path, t):
            if path not in res:
                if path:
                    res.add(path)
                for i in range(len(t)):
                    dfs(path+t[i], t[:i] + t[i+1:])
                
        dfs('', tiles)
        return len(res)


if __name__ == "__main__":

    s = Solution()
    tiles = "AAB"
    print(s. numTilePossibilities2(tiles))