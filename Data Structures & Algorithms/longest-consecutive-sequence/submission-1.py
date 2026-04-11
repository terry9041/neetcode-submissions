class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        temp = set(nums)
        res = 0
        for i in range(len(nums)):
            if nums[i] - 1 not in temp: # not at the middle of sub
                currLen = 1
                j = 1
                while nums[i] + j in temp:
                    currLen += 1
                    j += 1
                res = max(res,currLen)
        return res