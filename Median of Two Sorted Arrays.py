class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=nums1+nums2.             #adding the two given lists
        nums.sort().                  #sorting the list
        l=len(nums)
        if((l%2)!=0):.                #if its length is odd
            n=math.floor(l/2)
            return(nums[n])
        else:
            n1=int(l/2).              #if its lenght is odd
            return((nums[n1]+nums[n1-1])/2)#return the median according to the formula

