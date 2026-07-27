class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
      if nums == []:
        return 0

      best = 0
      curr = 1

      numset = set(nums)

      for num in nums:
        print(num)
        currNum = num
        if num in numset:
            numset.remove(num)
            currNum = num - 1
            while currNum in numset:
                curr += 1
                numset.remove(currNum)
                currNum -= 1
            currNum = num + 1
            while currNum in numset:
                curr += 1
                numset.remove(currNum)
                currNum += 1
            if curr > best:
                best = curr
            curr = 1
        
      return best

        