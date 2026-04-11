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
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res