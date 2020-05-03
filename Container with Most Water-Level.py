class Solution:
    def maxArea(self, height: List[int]) -> int:
        area=[]
        l=len(height)
        for i in range(0,l):
            for j in range(i+1,l):
                    ar=min(height[i],height[j])*(j-i)
                    area.append(ar)
        return max(area)           
        
