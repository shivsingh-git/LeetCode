class Solution:
    def maxArea(self, height: List[int]) -> int:
        area=[]
        l=len(height)
        for i in range(0,l):
            for j in range(i+1,l):
                if (height[i]<=height[j]):
                    h=j-i
                    ar=height[i]*h
                    area.append(ar)
                elif(height[i]>height[j]):
                    h=j-i
                    ar=height[j]*h
                    area.append(ar)
        return max(area)           
        
