class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1. find pivot where nums[pivot] < nums[pivot] from right end
        pivot = len(nums)-2
        while pivot >= 0 and not nums[pivot] < nums[pivot+1]:
            pivot -= 1
        print(pivot)

        # case where entire arr is descending
        if pivot == -1:
            nums.reverse()
            return 

        # 2. find successor where nums[successor] > nums[pivot] from right end
        successor = len(nums)-1
        while not nums[successor] > nums[pivot]:
            successor -= 1

        # 3. swap pivot and successor
        nums[pivot], nums[successor] = nums[successor], nums[pivot]

        # 4. reverse the right end of the pivot 
        l, r = pivot + 1, len(nums)-1
        while l <= r:
            nums[l],nums[r] = nums[r], nums[l]
            r -= 1
            l += 1

        return 

        
        

