class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # time complexity: O(logn)
        # space complexity: O(1)
        # rmb to -+1 to skip the mid, where it doesnt match

        # Without these adjustments (-1 and +1), the search could get stuck in an infinite loop, repeatedly checking the same mid element.
        # eg (1+2)//2 = 1, then if target is greater than nums[1], then l would be set to 1 again!
        l = 0
        r = len(nums)-1
        while (l<=r):
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid-1
            else:
                l = mid+1
        return -1