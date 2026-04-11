class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = dict() # max size of O(n)
        for num in nums: # O(n)
            if num in seen: # O(1) Hashmap contains key
                return True
            else:
                seen[num] = True # O(1)
        return False
