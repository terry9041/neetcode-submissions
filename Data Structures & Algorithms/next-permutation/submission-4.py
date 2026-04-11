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

        # case where it's single num or perm is already on last one -> cycles back
        if pivot == -1:
            nums.reverse()
            return 

        # 2. find successor where nums[successor] > nums[pivot] from right end
        swap = len(nums)-1
        while swap >= 0 and not nums[swap] > nums[pivot]:
            swap -= 1

        print(swap)
        # 3. perform swap
        nums[pivot], nums[swap] = nums[swap], nums[pivot]

        # 4. flip the right end to make sure it's the smallest
        l, r = pivot + 1, len(nums)-1
        while l <= r:
            nums[l],nums[r] = nums[r], nums[l]
            r -= 1
            l += 1

        return 

        
        

