from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        buckets = [[] for _ in range(len(nums))]
        for num in counts:
            count = counts[num]
            buckets[count-1].append(num)
        res = []
        for i in range(len(buckets)-1,-1,-1):
            j = 0
            while k > 0 and j < len(buckets[i]):
                res.append(buckets[i][j])
                j += 1
                k -= 1
        return res