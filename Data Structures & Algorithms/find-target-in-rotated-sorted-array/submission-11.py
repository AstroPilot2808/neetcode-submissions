class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if nums[0] == target:
            return 0
        elif len(nums) == 2 and nums[1] == target:
            return 1

        l, r = 0, len(nums) - 1

        m = (l+r)//2
    
        minIndex = 0

        if nums[0] < nums[-1]:
            while l<r:
                if nums[l] == target:
                    return l
                if nums[r] == target:
                    return r
                if nums[m] == target:
                    return m
                if nums[m] < target:
                    l = m+1
                    m = (l+r)//2
                elif nums[m] > target:
                    r = m-1
                    m = (l+r)//2

        while nums[l] > nums[r]:
            if nums[l] == target:
                return l
            elif nums[m] == target:
                return m
            elif nums[r] == target:
                return r
            if nums[m] > nums[m+1]:
                minIndex = m+1
                print(minIndex)
                break
            if nums[m] < nums[m-1]:
                minIndex = m
                print(minIndex)
                break
            if nums[l] < nums[m]:
                l = m
                m = (l+r)//2
            elif nums[m] < nums[r]:
                r = m
                m = (l+r)//2
        
        if nums[0] <= target <= nums[minIndex - 1]:
            l = 0
            r = minIndex-1
        elif nums[minIndex] <= target <= nums[-1]:
            l = minIndex
            r = len(nums) - 1

        m = (l+r)//2
        while l<r:
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r
            if nums[m] == target:
                return m
            if nums[m] < target:
                l = m+1
                m = (l+r)//2
            elif nums[m] > target:
                r = m-1
                m = (l+r)//2
        return -1                
        

            