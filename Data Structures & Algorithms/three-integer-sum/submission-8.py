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
            # Skip duplicate pivots
            if p > 0 and nums[p] == nums[p-1]:
                continue
            l,r = p + 1, n - 1
            print(p,l,r)
            while l < r:
                total = nums[p] + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0: 
                    r -= 1
                else:
                    res.append([nums[p], nums[l], nums[r]])

                    # Skip duplicate values for l, r
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1 # the while loop stops at the last occurance of dup
                    r -= 1 # the while loop stops at the last occurance of dup
                    # eg [-1, -1, -1, 0, 1, 2]
                    #     p   l  l+1
                    # 1 loop       l
                    # increment       1             
        return res
        