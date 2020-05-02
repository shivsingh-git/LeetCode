class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i
        for i in range(len(nums)):
            t = target - nums[i]
            if not (d.get(t) is None) and d[t] != i:
                return [i, d[t]]
            
