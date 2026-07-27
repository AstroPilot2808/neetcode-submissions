class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        answer = list()
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        freq = [[] for i in range(len(nums) + 1)]

        for key, value in count.items():
            freq[value].append(key)

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                answer.append(num)
                if len(answer) == k:
                    return answer
                
