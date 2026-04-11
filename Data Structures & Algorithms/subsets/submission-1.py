class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()
        
        def backtrack(path, pos):
            res.append(path[:])
            print(path, seen)
            if len(seen) == len(nums):
                return
            
            for i in range(pos, len(nums)):
                num = nums[i]
                if num not in seen:
                    seen.add(num)
                    path.append(num)

                    backtrack(path, i+1)

                    seen.remove(num)
                    path.pop()

        backtrack([], 0)
        return res

        
        