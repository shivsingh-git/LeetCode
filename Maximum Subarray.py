class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        temp = []                                                   #creating a list to store the maximum values              
        temp.append(nums[0])                                        #storing the first value in the list
        for i in range(1,len(nums)):
            r = max(nums[i],temp[i-1]+nums[i])                      #getting the sum value of evry subarrays
            temp.append(r)                                          #storing the sums in the temp list
        return max(temp)                                            #returning the maximum value.
