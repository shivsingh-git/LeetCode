class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i] != val :             #checking if the value of the val is not equal to the list element
                nums[count] = nums[i].      #allot the value to the list
                count +=1.                  #increase the value of count
        return count
