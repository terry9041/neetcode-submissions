from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(N), O(N)
        counts = Counter(nums)
        buckets = [[] for _ in range(len(nums)+1)]
        for elem, freq in counts.items():
            buckets[freq].append(elem)
        res = []
        for ind in range(len(buckets)-1, -1, -1):
            nums = buckets[ind]
            for num in nums:
                if len(res) < k:
                    res.append(num)
                else:
                    return res
        return res

        