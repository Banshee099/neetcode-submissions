class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums[0]==target:
            return 0
        if nums[len(nums)-1]==target:
            return len(nums)-1
        mid = len(nums)//2
        for i in range(len(nums)//2):
            if target==nums[mid]:
                return mid
            if target<nums[mid]:
                mid -=1
            elif target>nums[mid]:
                mid+=1
        else:
            return -1