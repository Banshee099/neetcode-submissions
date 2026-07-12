class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        last = len(numbers)-1
        i=0
        while i<last:
            t = numbers[i]+numbers[last]
            if t==target:
                return [i+1,last+1]
            elif (target-t)<0:
                last -=1
            else:
                i+=1