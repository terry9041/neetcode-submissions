class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob(houses):
            rob1, rob2 = 0, 0
            for n in houses:
                rob1, rob2 = rob2, max(rob1+n,rob2)
            return(rob2)
        if len(nums) <= 2:
            return max(nums)
        return max(rob(nums[:len(nums)-1]), rob(nums[1:]))

        
