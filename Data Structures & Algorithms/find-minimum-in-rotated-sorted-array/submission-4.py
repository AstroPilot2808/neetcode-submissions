class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]

        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return min(nums)

        l, r = 0, len(nums) - 1
        m = (l+r)//2

        while nums[l] > nums[r]:
            if nums[m] < nums[m-1]:
                return nums[m]
            if nums[m] > nums[m+1]:
                return nums[m+1]
            if nums[l] < nums[m]:
                l = m
                m = (l+r)//2
            elif nums[m] < nums[r]:
                r = m
                m = (l+r)//2
                