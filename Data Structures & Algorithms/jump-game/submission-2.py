class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # BF: check every jump combination -> max O(2^n)
        target = len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if i + nums[i] >= target:
                target = i
        return target == 0

        # TC: O(n)
        # SC: O(1)