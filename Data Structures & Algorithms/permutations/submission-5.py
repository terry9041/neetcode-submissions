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
                        # 1. choose a path
                        path.append(nums[i])
                        seen[i] = True

                        # 2. explore
                        backtrack(path)

                        # 3. backtrack
                        path.pop()
                        seen[i] = False
        backtrack([])
        return res

        # TC: O(n!*n), n! permutations, each require a O(n) operation
        # SC: O(n), recursion tree depth and size of seen
