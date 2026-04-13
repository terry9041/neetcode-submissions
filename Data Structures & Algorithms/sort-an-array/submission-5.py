class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(low, high):
            mid = (low+high)//2
            nums[mid], nums[high] = nums[high], nums[mid]
            pivot = nums[high]
            i = low
            for j in range(low, high):
                if nums[j] <= pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[high], nums[i] = nums[i], nums[high]
            return i


        def quickSort(low, high):
            if low < high:
                pi = partition(low, high)
                quickSort(low, pi - 1)
                quickSort(pi+1, high)
        quickSort(0, len(nums)-1)
        return nums