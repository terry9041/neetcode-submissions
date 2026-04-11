from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        mapping = defaultdict(int)
        total = 0

        for num in nums:
            total += num
            if total == k:
                count += 1
            if (total-k) in mapping:
                count += mapping[total-k]
            mapping[total] += 1
        return count
            
