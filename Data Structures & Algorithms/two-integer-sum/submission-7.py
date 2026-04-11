class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # input: [int] called nums, int called target
        # output: [int] containing two indices tht sums up to target
        # edge case:
        # empty list? not possible
        # guranteed pair? yes
        # unique pair? yes
        # return order for indices? both way work
        # num can be repeated? yes

        # walk through
        # nums = [3,4,5,6], target = 7
        # [0,1]

        # naive:
        # check every single pair of numbers using nested loops
        # if they sum up to target
        # if yes return their indices
        # bad becos it's n^2 for the nested loops
        
        # improved:
        # hashmap: 
        # key: elem val: its indice in nums
        # eg [3,4,5,6] -> 3:0, 4:1, 5:2, 6:3

        # single loop
        # if no match with the elem in hm -> add that to HM
        # if yes -> return indices

        mappings = dict()

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in mappings:
                return [mappings[diff], i]
            mappings[nums[i]] = i
        
        # TC: O(n), scan thro each elem once doing O(1) hm operations
        # SC: O(n) for extra hashmap, worst case when all nums are unique and pair is at the last two indices
