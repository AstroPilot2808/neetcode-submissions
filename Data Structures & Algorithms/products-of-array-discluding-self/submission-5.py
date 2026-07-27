class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        answer = [1] * len(nums)

        prefix = 1
        i = 1
        while i < len(nums):
            answer[i] = nums[i-1] * prefix
            prefix = prefix * nums[i-1]
            i += 1

        suffix = 1
        i = len(nums) - 2
        while i >= 0:
            answer [i] = nums[i+1] * suffix * answer[i]
            suffix = suffix * nums[i+1]
            i -= 1

        return answer