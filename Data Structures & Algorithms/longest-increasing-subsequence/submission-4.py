class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(1,len(nums)):
            dp[i] = 1 + max([dp[j] if nums[j] < nums[i] else 0 for j in range(i)], default = 0)
        return max(dp)
