class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        masterdict = dict()

        for char in s:
            if char in masterdict:
                masterdict[char] += 1
            else:
                masterdict[char] = 1

        for char in t:
            if char in masterdict:
                masterdict[char] -= 1
            else: 
                return False
        
        for char in masterdict:
            if masterdict[char] != 0:
                return False
        
        return True

        