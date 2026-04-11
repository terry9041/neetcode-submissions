class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(path, start):
            res.append(path[:])
            
            for i in range(start, len(nums)):
                path.append(nums[i])

                backtrack(path, i+1)

                path.pop()

        backtrack([], 0)
        return res

        # TC: O(n* 2^n), 2^n strings, each requires O(n) to copy
        # SC: O(n) for max recursion depth

        
        