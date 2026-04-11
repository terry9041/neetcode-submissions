class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # eg [0,3,1] len = 3 [0,1,2,3] - [0,3,1]
        res = len(nums)
        for i in range(len(nums)):
            res += i - nums[i]
        return res