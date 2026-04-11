class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def get_hour(rate, piles):
            res = 0
            for pile in piles:
                res += -(-pile//rate)
            return res
        low, high = 1, max(piles)
        while low < high:
            mid = (low+high)//2
            curr_hour = get_hour(mid, piles)
            if curr_hour > h:
                low = mid + 1
            else:
                high = mid
        return low