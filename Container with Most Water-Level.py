class Solution:
    def maxArea(self, height: List[int]) -> int:
        area=[]                                                     #creating a new list
        l=len(height)
        for i in range(0,l):                                        #running the two loops from 0 to l and next from i+1 to l
            for j in range(i+1,l):
                    ar=min(height[i],height[j])*(j-i)               #to calculate the every possible recatngle
                    area.append(ar)                                 #storing it in the list
        return max(area)                                            #returnig the max area 
