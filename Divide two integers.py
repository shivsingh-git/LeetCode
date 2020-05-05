class Solution:
    def divide(self, dividend: int, divisor: int) -> int: 
        x = abs(dividend)//abs(divisor)
        if(dividend < 0):
            x = -x
        if(divisor < 0):
            x = -x
        if(x >= -2**31 and x < 2**31):
            return x
        else:
            return 2**31 - 1
        
