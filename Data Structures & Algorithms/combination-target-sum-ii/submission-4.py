class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
    
        def backtrack(path, total, idx):
            if total > target:
                return
            if total == target:
                res.append(path[:])
                return
            for i in range(idx, len(nums)):
                # 1. i > idx: This ensures we are not at the very first element of the current loop.
                # 2. nums[i] == nums[i-1]: This detects a duplicate.
                # for the previous element at the SAME level of the tree.
                if i > idx and nums[i] == nums[i-1]:
                    continue

                path.append(nums[i])
                backtrack(path, total+nums[i], i+1)
                path.pop()
                    

        backtrack([],0,0)
        return res