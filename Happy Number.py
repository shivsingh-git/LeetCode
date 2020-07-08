class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        square = 0  
        while square != 1:
            square = 0  
            while n > 0: 
                square += (n % 10) ** 2
                n = n//10  
            if square in seen:
                return False
            else: 
                n = square    
                if n < 243:
                    seen.add(n)  
        return True
