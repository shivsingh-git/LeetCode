class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)
        





class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        c=0  
        for i in nums:
            if(nums.count(i)>1):
                c+=1
        if(c>1):
            return(True)
        else:
            return(False)
        
