class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(lst, seen):
            if len(lst) == len(nums):
                print(lst)
                res.append(lst)
                return
            for i in range(len(nums)):
                if not seen[i]:
                    seen[i] = True
                    dfs(lst + [nums[i]], seen)
                    seen[i] = False

        dfs([],[False]*len(nums))
        return res