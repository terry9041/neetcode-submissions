class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # time complexity: O(n)
        # memory complexity: O(n) worst case: every letter is distinct
        hashmap = dict()
        for num in nums: #O(n)
            if num not in hashmap: # O(1)
                hashmap[num] = True # add the num to seen list
            else:
                return True # if seen, then duplicate, return True
        return False

        # # time complexity: O(nlogn)
        # # memory complexity: O(1)
        # nums = sorted(nums)
        # for ind in range(len(nums)-1):
        #     if nums[ind] == nums[ind+1]:
        #         return True
        # return False

        # # time complexity: O(n^2)
        # # memory complexity: O(1)
        # for i in range(len(nums)-1):
        #     for j in range (i+1, len(nums)):
        #         if (nums[i] == nums[j]):
        #             return True
        # return False

