class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # input: nums [int]
        # output: [[int]], list of three nums that add up to zero 
        # contraint: from nums, no duplicate triplets

        # edge cases:
        # guranteed at least one sol -> no
        #   possible to have < 3 or just no sol
    
        # brute force:
        # check every triplet to see if add up to zero
        # if yes, sort and add to set to prev dup
        # bad as TC: O(n^3)

        # optimize: 
        # 1. sort the array first => O(nlogn)
        # [-1,0,1,2,-1,-4] -> [-4, -1, -1, 0, 1, 2]
        # 2. loop thro the rest, setting one num as pivot, 
        # look at its right to search for a pair such that
        # pivot + pair == 0 => O(n^2)
        # SC: O(1)

        res = []
        n = len(nums)
        nums.sort() 

        for p in range(n-2):
            if p > 0 and nums[p-1] == nums[p]:
                continue
            l, r = p + 1, len(nums)-1
            while l < r:
                threeSum = nums[p] + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([nums[p], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res
        