class Solution:
    def climbStairs(self, n: int) -> int:
        options =  [0,1,2]
        if n > 2:
            for x in range(3, n+1):
                options.append(options[x-1]+options[x-2])
        return options[n]
