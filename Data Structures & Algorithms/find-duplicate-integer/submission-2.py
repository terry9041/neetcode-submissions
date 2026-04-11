class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # BF: we could check pairs -> TC: O(n^2) SC:O(1)
        # we could use count hashmap -> TC: O(n) SC:O(n)
        # or we could use nums as a hashmap

        for i in range(len(nums)):
            target_idx = abs(nums[i])-1
            if nums[target_idx] < 0:
                return abs(nums[i])
            nums[target_idx] *= -1


