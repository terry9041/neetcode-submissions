class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # input: int arr (nums), int (target)
        # output: int pair
        # input edgecase: empty arr? negative number?
        # output constraints: cant return the same indices * 2, always return the smaller indice first, gurantee a pair, one and only

        # naive:
        # 3,4,5,6
        #     i j
        # TC: O(n^2) where n is the length of arr
        # SC: O(1) as we are using constant space to store i,j as loop var

        # hashmap
        # Key: target-nums[i] value: indices
        # 3,4,5,6 target = 7
        # [4:0]
        # return 0, 1

        hashmap = dict()
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[target-nums[i]] = i
            else:
                return [hashmap[nums[i]], i]
        

        
        