class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = dict()
        for i in range(len(nums)):
            n = nums[i]
            if target-n in mapping:
                return [mapping[target-n], i]
            mapping[n] = i
        