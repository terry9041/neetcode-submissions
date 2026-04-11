class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # BF: O(n^2)

        contains = set(nums)
        res = 0

        for num in nums:
            temp = 1
            while num + 1 in contains:
                temp += 1
                num += 1
            res = max(res,temp)
        
        return res