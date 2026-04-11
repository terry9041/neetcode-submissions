class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        # seen arr for keeping track of elem used so far 
        seen = [False] * n

        def backtrack(path):
            # base case
            if len(path) == n:
                res.append(path[:])
                return
            else:
                for i in range(n):
                    if not seen[i]:
                        # add to path
                        path.append(nums[i])
                        seen[i] = True

                        # explore
                        backtrack(path)

                        # backtrack
                        path.pop()
                        seen[i] = False
        backtrack([])
        return res
