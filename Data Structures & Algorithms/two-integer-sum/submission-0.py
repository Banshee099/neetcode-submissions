class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        sub = 0
        n = len(nums)
        for i in range(n):
            sub = target - nums[i]
            if sub in s:
                return [s[sub],i]
            s[nums[i]] = i
        return[]