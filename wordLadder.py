# A transformation sequence from word beginWord to word endWord 
# using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, 
# return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

# Example 1:
# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

# Example 2:
# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
 
# Constraints:
# 1 <= beginWord.length <= 10
# endWord.length == beginWord.length
# 1 <= wordList.length <= 5000
# wordList[i].length == beginWord.length
# beginWord, endWord, and wordList[i] consist of lowercase English letters.
# beginWord != endWord
# All the words in wordList are unique.

import collections 

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # initialize word list dictionary
        w_dict = {}
        for word in wordList:
            w_dict[word] = 1
        
        # base check
        if endWord not in wordList:
            return 0
        
        # DFS
        q = collections.deque([beginWord])
        res = 1
        visited = set([beginWord])
        while q:
            iter = len(q)
            for i in range(iter):
                word = q.popleft()
                if word == endWord:
                    return res
                
                for j in range(len(word)):
                    tmp_word = word
                    for c_ascii in range(ord('a'),ord('z')+1):
                        tmp_word = tmp_word[:j] + chr(c_ascii) + tmp_word[j+1:]
                        if tmp_word in w_dict and tmp_word not in visited:
                            visited.add(tmp_word)
                            q.append(tmp_word)
            res+=1
            if len(q) == 0:
                return 0
        return res

if __name__ =="__main__":
    s = Solution()
    beginWord = 'hot'
    endWord = 'dog'
    wordList = ['hot', 'dog']
    print(s.ladderLength(beginWord, endWord, wordList))