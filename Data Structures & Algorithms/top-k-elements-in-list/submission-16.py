class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count, consists of num:count
        counts = {}
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)

        # buckets, consists of count:[num]
        buckets = [[] for _ in range(len(nums))]
        for num in counts:
            count = counts[num]
            buckets[count-1].append(num)
        
        # collect num from buckets reversely
        res = []
        for i in range(len(buckets)-1, -1, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res

        # TC: O(n)
        # SC: O(n)

        # BF: create count table of num:freq, then create list of (freq, num) and sort
        # bad because TC: O(nlogn) because of the sorting, SC: O(n)