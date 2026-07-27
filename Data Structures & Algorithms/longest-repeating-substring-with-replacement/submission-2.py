class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        bestAnswer = 0
        count = dict()

        start = 0

        for end, char in enumerate(s):
            count[char] = count.get(char, 0) + 1
            if (end - start + 1) - max(count.values()) <= k:
                bestAnswer = max(bestAnswer, end - start + 1)
            else:
                count[s[start]] -= 1
                start += 1
            
        return bestAnswer