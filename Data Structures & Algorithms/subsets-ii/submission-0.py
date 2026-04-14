class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        
        def backtrack(path, idx):
            res.append(path[:])
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtrack(path, i+1)
                path.pop()
            return

        backtrack([],0)
        return res
