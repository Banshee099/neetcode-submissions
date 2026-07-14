class Solution:
    def trap(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        lm=height[i]
        rm=height[j]
        sub=0
        max_area=0
        area=0
        while(i<j):
            if height[i]<height[j]:
                i+=1
                lm=max(lm,height[i])
                max_area =max_area+ (lm-height[i])
            else:
                j-=1
                rm=max(rm,height[j])
                max_area = max_area+(rm-height[j])
            
        return max_area
