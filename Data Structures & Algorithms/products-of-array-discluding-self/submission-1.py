class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)
        answer = [0] * len(nums)

        i = 0
        while i < len(nums):
            if i == 0:
                prefix[i] = 1
                i += 1
            else:
                prefix[i] = prefix[i-1] * nums[i-1]
                i += 1

        i = len(nums) - 1   
        while i >= 0:
            if i == len(nums) - 1:
                suffix[i] = 1
                i -= 1
            else:
                suffix[i] = suffix[i + 1] * nums[i + 1]
                i -= 1

        print(prefix)
        print(suffix)
        
        i = 0;
        while i < len(nums):
            answer[i] = prefix[i] * suffix[i]
            i += 1
        
        return answer

        
