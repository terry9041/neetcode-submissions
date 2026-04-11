class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected_total = ((len(nums)+1) * len(nums))/2
        curr_total = sum(nums)
        return int(expected_total - curr_total)
            