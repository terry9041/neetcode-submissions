class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        temp = list(sorted(nums))
        n = len(temp)
        res = set()
        for i in range(n-1):
            j,k = i+1, n-1
            while j < k:
                s = temp[i] + temp[j] + temp[k]
                if s == 0:
                    res.add((temp[i], temp[j], temp[k]))
                    j += 1
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    k -= 1
        return [list(tup) for tup in res]