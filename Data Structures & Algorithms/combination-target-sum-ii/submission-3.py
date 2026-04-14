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
                # check i-1 as eg i+1 will miss case of [2,2] for target == 4
                if i > idx and nums[i] == nums[i-1]:
                    continue

                path.append(nums[i])
                backtrack(path, total+nums[i], i+1)
                path.pop()
                    

        backtrack([],0,0)
        return res