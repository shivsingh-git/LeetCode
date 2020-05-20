class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        temp = []                               
        temp.append(nums[0])
        for i in range(1,len(nums)):
            r = max(nums[i],temp[i-1]+nums[i])
            temp.append(r)
        return max(temp)
