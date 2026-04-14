class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(path, total, idx):
            if total > target:
                return
            if total == target:
                res.append(path[:])
                return
            for i in range(idx, len(nums)):
                path.append(nums[i])
                backtrack(path, total+nums[i], i)
                path.pop()

        backtrack([],0,0)
        return res