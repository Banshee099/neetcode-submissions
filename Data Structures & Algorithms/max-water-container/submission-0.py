class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxi=0
        area=0
        i=0
        j=len(heights)-1
        while i<j:
            area = min(heights[i],heights[j])*(j-i)
            maxi=max(maxi,area)
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return max(maxi,area)