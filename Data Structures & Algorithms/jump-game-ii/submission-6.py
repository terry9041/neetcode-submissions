class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1: return 0

        boundary = 0
        count = 0
        while boundary < len(nums)-1:
            target = [0,0]
            for i in range(1,nums[boundary]+1):
                if boundary + i >= len(nums)-1:
                    return count + 1
                dist = boundary + i + nums[boundary + i]
                if dist > target[1]:
                    target = [i, dist]

            boundary += target[0]
            count += 1
            
        return count
                