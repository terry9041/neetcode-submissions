class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # BF: O(n^2)

        contains = set(nums)
        res = 0

        for num in nums:
            # only do check when it's an optimal start to maximize length
            if num-1 not in contains:
                length = 1
                while num + length in contains:
                    length += 1
                res = max(res,length)
        
        return res