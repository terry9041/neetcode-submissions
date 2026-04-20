class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums) {
        nums.sort((a, b) => a - b)

        let res = []
        for (let i = 0; i < nums.length; i++) {
            if ((i > 0) && (nums[i] == nums[i-1])) {
                continue
            }
            let l = i + 1
            let r = nums.length - 1
            while (l < r) {
                let total = nums[i] + nums[l] + nums[r]
                if (total < 0) {
                    l ++
                }
                else if (total > 0) {
                    r --
                }
                else {
                    res.push([nums[i], nums[l], nums[r]])
                    while ((l < r) && (nums[l] == nums[l+1])) {
                        l ++
                    }
                    l ++
                    while ((l < r) && (nums[r] == nums[r-1])) {
                        r --
                    } 
                    r --
                }
            }
        
        }
        
        return res
    }
}
