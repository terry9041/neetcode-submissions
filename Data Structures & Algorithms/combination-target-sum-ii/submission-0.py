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
            seen = set()
            for i in range(idx, len(nums)):
                if nums[i] not in seen:
                    seen.add(nums[i])
                    path.append(nums[i])
                    backtrack(path, total+nums[i], i+1)
                    path.pop()
                    

        backtrack([],0,0)
        return res