from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        total = 0
        count = 0

        for num in nums:
            total += num
            if total == k:
                count += 1
            if total - k in prefix  :
                count += prefix[total-k]
            prefix[total] += 1
        return count


