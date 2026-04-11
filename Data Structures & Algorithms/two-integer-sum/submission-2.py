class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for i in range(len(nums)):
            complement = target-nums[i]
            if complement not in hashmap:
                hashmap[nums[i]] = i
            else:
                return [hashmap[complement],i]