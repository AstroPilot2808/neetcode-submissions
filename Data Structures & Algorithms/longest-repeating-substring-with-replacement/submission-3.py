class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        bestAnswer = 0
        count = dict()
        maxq = 0

        start = 0

        for end, char in enumerate(s):
            count[char] = count.get(char, 0) + 1
            maxq = max(maxq, count[char])
            if (end - start + 1) - maxq <= k:
                bestAnswer = max(bestAnswer, end - start + 1)
            else:
                count[s[start]] -= 1
                start += 1
            
        return bestAnswer