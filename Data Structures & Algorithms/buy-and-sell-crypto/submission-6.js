class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let left = 0
        let res = 0
        for (let right = 0; right < prices.length; right++) {
            if (prices[right] > prices[left]) {
                res = Math.max(res, prices[right] - prices[left])
            }
            else {
                left = right
            }
        }
        return res
    }
}
