class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()

        # value: value, key: ind
        # we calculate the complement to current elem
        # and if complemenet to current elem exists,
            # then return [ind, hashmap[complement]]
        # else hashmap[nums[i]]

        # for i in range(len(nums)):
        #     complement = target-nums[i]
        #     if complement not in hashmap:
        #         hashmap[nums[i]] = i
        #     else:
        #         return [hashmap[complement],i]

        # value: ind, key: its complement
        # if an elem is found as complement
        # then we return ind of the elem and ind where it is matched as complement
        # else hashmap[target-nums[i]] = i
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[target-nums[i]] = i
            else:
                return [hashmap[nums[i]],i]