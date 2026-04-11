class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # two pointer approach

        # l -> buying, r -> selling
        # 2 scenario of lr,

            # 1. buy is higher than sell => we try to move out of it, l := r as r is lower, r++
                # why not l++? we need l to the lowest pt we have in this window, not just random val
                # we let the new lowest slip away if we do l++

            # 2. sell is higher than buy => hows the profit? if greater than max, then update
                # regardless of higher than max or not, try to move to r again
                    # when r moves, if it reaches higher then we can have higher profit
                    # if it reaches lower, then we can have scenario 1
                    # again, we dun need to save the indexes, just return the max profit

        l = 0
        r = 1
        max = 0
        while (r<len(prices)):
            curr = prices[r] - prices[l]
            if curr < 0:
                l = r # move the buy day to the lowest we hv so far
                r += 1
            else:
                if curr > max:
                    max = curr
                r += 1 # move the selling day forward
        return max