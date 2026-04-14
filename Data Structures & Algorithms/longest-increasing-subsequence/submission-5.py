class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        # Initialize DP table where dp[i] is the LIS ending at index i
        dp = [1] * len(nums)
        
        for i in range(1, len(nums)):
            for j in range(i): # Check ALL previous elements
                if nums[j] < nums[i]:
                    # Update dp[i] if taking nums[j] yields a longer sequence
                    dp[i] = max(dp[i], dp[j] + 1)
        
        # The answer is the maximum value found in the entire DP table
        return max(dp)