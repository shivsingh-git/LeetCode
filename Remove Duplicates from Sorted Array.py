class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        while(i<len(nums)):
            if(nums.count(nums[i])>1):
                nums.remove(nums[i])
            else:
                i+=1
