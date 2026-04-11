class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l1 = [1]
        l2 = [1]
        t1 = 1
        t2 = 1
        res = []
        for i in range(len(nums)):
            t1*= nums[i]
            l1.append(t1)
            t2 *= nums[-i-1]
            l2.append(t2)
        l1.append(1)
        l2.append(1)
        l2 = list(reversed(l2))
        print(l1)
        print(l2)
        for i in range(len(nums)):
            res.append(l1[i]*l2[i+2])
        return res
            
        
        