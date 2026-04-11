class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = [False] * len(nums)
        
        def dfs(lst):
            if len(lst) == len(nums):
                res.append(lst)
                return
            for i in range(len(nums)):
                if not seen[i]:
                    seen[i] = True
                    dfs(lst + [nums[i]])
                    seen[i] = False

        dfs([])
        return res