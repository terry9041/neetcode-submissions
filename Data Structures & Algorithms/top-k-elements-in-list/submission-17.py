from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count, consists of num:count
        count = defaultdict(int)
        for n in nums:
            count[n] += 1


        freq = [[] for _ in range(len(nums)+1)]
        for n in count:
            freq[count[n]].append(n)

        res = []
        for i in range(len(freq)-1, -1, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        

