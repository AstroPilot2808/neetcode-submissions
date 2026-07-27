class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 0:
            return 0


        bestScore = 1;
        visited = set()

        start, end = 0, 1
        
        visited.add(s[start])

        while end < len(s):
            if s[end] in visited:
                while s[start] != s[end]:
                    visited.remove(s[start])
                    start += 1
                visited.remove(s[start])
                start += 1
            else:
                bestScore = max(bestScore, end - start + 1)
                visited.add(s[end])
                end += 1 
        return bestScore

