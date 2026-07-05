class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul=1
        new_list=[]
        pre=[]
        post=[0]*len(nums)
        for i in nums:
            mul *=i
            pre.append(int(mul))
        mul=1
        for j in range(len(nums)-1,-1,-1):
            mul = nums[j]*mul
            post[j]=mul
        for k in range(len(nums)):
            if k==0:
                nums[0]=post[1]
            elif k==len(nums)-1:
                nums[len(nums)-1]=pre[-2]
            else:
                nums[k]=pre[k-1]*post[k+1]

        return nums
                