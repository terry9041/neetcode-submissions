class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = nums[0]
        maxSum = nums[0]
        for i in range(1, len(nums)):
            # if the curr is +ve
            # always add the next num to currSum
            if currSum > 0:
                currSum += nums[i]
            # else if curr is -ve
            # always reset currSum to nums[i]
            else:
                currSum = nums[i]
            maxSum = max(maxSum, currSum)
        return maxSum 
