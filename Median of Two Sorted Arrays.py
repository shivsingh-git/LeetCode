class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=nums1+nums2
        nums.sort()
        l=len(nums)
        if((l%2)!=0):
            n=math.floor(l/2)
            return(nums[n])
        else:
            n1=int(l/2)
            return((nums[n1]+nums[n1-1])/2)
