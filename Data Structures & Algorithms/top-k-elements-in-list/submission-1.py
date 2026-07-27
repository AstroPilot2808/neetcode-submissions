class Solution:
    def get_value(item):
        return item[1]
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        answer = list()

        for num in nums:
            if num in count:
                count[num] += 1
            else: 
                count[num] = 1
        
        sortedCount = dict(sorted(count.items(), key=Solution.get_value, reverse=True))

        return list(sortedCount.keys())[0:k]
    