class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        start = 0
        end = 1

        while start < len(nums) - 1:
            end = start + 1
            while end < len(nums):
                if (nums[start] + nums[end] == target):
                    return [start, end]
                else:
                    end += 1
            start += 1
        

        