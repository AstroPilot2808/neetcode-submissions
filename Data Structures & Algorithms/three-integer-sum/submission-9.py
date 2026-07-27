class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)
        prevSolutions = set()
        answer = list(list())
        for i, num in enumerate(nums):

            start = i+1
            end = len(nums) - 1

            while start < end:
                if num + nums[start] + nums[end] > 0:
                    end -= 1
                elif num + nums[start] + nums[end] < 0:
                    start += 1
                elif num + nums[start] + nums[end] == 0:
                    if tuple([num, nums[start], nums[end]]) not in prevSolutions:
                        answer.append([num, nums[start], nums[end]])
                        prevSolutions.add(tuple([num, nums[start], nums[end]]))
                    start += 1

        return answer



    