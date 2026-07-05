class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul=1
        new_list=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j!=i:
                    mul*=nums[j]
            new_list.append(mul)
            mul=1
        return new_list
                