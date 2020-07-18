class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        square = 0  
        while square != 1:
            square = 0  
            while n > 0: 
                square += (n % 10) ** 2
                n = n//10  
            if square in s:
                return False
            else: 
                n = square    
                if n < 243:
                    s.add(n)  
        return True
